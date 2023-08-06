# Goal conditioned deep Q-network

import copy
import pickle

import numpy as np
import torch
from gym.spaces import Box
from torch.nn import ReLU, Tanh
from torch.nn.functional import normalize

from hbrl.agents.utils import scale_tensor
from hbrl.agents.utils.mlp import MLP
from hbrl.agents.value_based_agent import ValueBasedAgent
from torch import optim
from torch.nn import functional
from torch.distributions.normal import Normal
from gym.spaces import Box, Discrete
from typing import Union

from hbrl.utils import create_dir


class SAC(ValueBasedAgent):

    name = "SAC"

    def __init__(self, state_space: Union[Box, Discrete], action_space: Union[Box, Discrete], **params):
        """
        @param state_space: Environment's state space.
        @param action_space: Environment's action_space.
        @param params: Optional parameters.
        """

        super().__init__(state_space, action_space, **params)

        self.actor_lr = params.get("actor_lr", 0.0005)
        self.critic_lr = params.get("critic_lr", 0.0005)
        alpha = params.get("alpha", None)
        self.critic_alpha = params.get("critic_alpha", 0.6)
        self.actor_alpha = params.get("actor_alpha", 0.05)
        if alpha is not None:
            self.critic_alpha = alpha
            self.actor_alpha = alpha
        self.gamma = params.get("gamma", 0.99)
        self.tau = params.get("tau", 0.005)
        self.reward_scale = params.get("reward_scale", 15)

        self.policy_update_frequency = 2
        self.learning_step = 1

        self.min_std = -20
        self.max_std = 2

        actor_layers = params.get("actor_layers", [64, ReLU(), 64, ReLU(), 64, ReLU()])
        actor_activation = params.get("actor_activation", Tanh())
        assert isinstance(actor_activation, torch.nn.Module)
        self.actor = MLP(self.state_size, *actor_layers, 2 * self.nb_actions, actor_activation,
                         learning_rate=self.actor_lr, optimizer_class=optim.Adam, device=self.device).float()
        self.target_actor = copy.deepcopy(self.actor)

        critic_layers = params.get("critic_layers", [64, ReLU(), 64, ReLU(), 64, ReLU()])
        self.critic = MLP(self.state_size + self.nb_actions, *critic_layers, 1,
                          learning_rate=self.critic_lr, optimizer_class=optim.Adam, device=self.device).float()
        self.target_critic = copy.deepcopy(self.critic)

        self.passed_logs = []

    def get_q_value(self, state):
        with torch.no_grad():
            state = torch.from_numpy(state).to(self.device) if isinstance(state, np.ndarray) else state

            next_actions, _ = self.sample_action(state, use_target_network=True)
            critic_input = torch.concat((state, next_actions), dim=-1)
            q_values = self.target_critic.forward(critic_input).view(-1)
        return q_values

    def sample_action(self, actor_input, use_target_network=False, explore=True):
        actor_network = self.target_actor if use_target_network else self.actor

        if isinstance(actor_input, np.ndarray):
            actor_input = torch.from_numpy(actor_input).to(self.device)
        actor_input = normalize(actor_input, p=2., dim=-1) # Tensor torch.float64

        # Forward
        actor_output = actor_network(actor_input)
        if len(actor_input.shape) > 1:  # It's a batch
            actions_means = actor_output[:, :self.nb_actions]
            actions_log_stds = actor_output[:, self.nb_actions:]
        else:
            actions_means = actor_output[:self.nb_actions]
            actions_log_stds = actor_output[self.nb_actions:]

        actions_log_stds = torch.clamp(actions_log_stds, min=self.min_std, max=self.max_std)
        actions_stds = torch.exp(actions_log_stds)
        actions_distribution = Normal(actions_means, actions_stds)

        raw_actions = actions_distribution.rsample() if explore or self.under_test else actions_means

        log_probs = actions_distribution.log_prob(raw_actions)
        actions = torch.tanh(raw_actions)
        log_probs -= torch.log(1 - actions.pow(2) + 1e-6)
        log_probs = log_probs.sum(-1)
        actions = scale_tensor(actions, Box(-1, 1, (self.nb_actions,)), self.action_space)
        return actions, log_probs

    def action(self, state, explore=True):
        with torch.no_grad():
            action, _ = self.sample_action(state, explore=explore)
        return action.cpu().detach().numpy()

    def get_value(self, observations, actions=None):
        with torch.no_grad():
            if actions is None:
                actions, _ = self.sample_action(observations)
            elif isinstance(actions, np.ndarray):
                actions = torch.tensor(actions)
            if isinstance(observations, np.ndarray):
                observations = torch.tensor(observations)
            critic_value = self.critic(torch.concat((observations, actions), dim=-1))
        if len(critic_value.shape) > 1:
            critic_value = critic_value.squeeze()
        return critic_value.detach().numpy()

    def learn(self):
        if not self.under_test and len(self.replay_buffer) > self.batch_size:
            states, actions, rewards, new_states, done = self.sample_training_batch()

            # Training critic
            with torch.no_grad():
                next_actions, next_log_probs = \
                    self.sample_action(new_states, use_target_network=True)
                critic_input = torch.concat((new_states, next_actions), dim=-1)
                self.passed_logs.append(next_log_probs)
                next_q_values = \
                    self.target_critic(critic_input).view(-1)

            q_hat = self.reward_scale * rewards + self.gamma * (1 - done) * \
                (next_q_values - self.critic_alpha * next_log_probs)
            q_values = self.critic(torch.concat((states, actions), dim=-1)).view(-1)
            critic_loss = functional.mse_loss(q_values, q_hat)
            self.critic.learn(critic_loss)
            self.target_critic.converge_to(self.critic, tau=self.tau)

            if self.learning_step % self.policy_update_frequency == 0:
                for _ in range(self.policy_update_frequency):
                    # Train actor
                    actions, log_probs = self.sample_action(states)
                    log_probs = log_probs.view(-1)
                    critic_values = self.critic(torch.concat((states, actions), dim=-1)).view(-1)

                    actor_loss = self.actor_alpha * log_probs - critic_values
                    actor_loss = torch.mean(actor_loss)
                    self.actor.learn(actor_loss, retain_graph=True)
                    self.target_actor.converge_to(self.actor, tau=self.tau)
            self.learning_step += 1

    def save(self, directory):
        if directory[-1] != "/":
            directory += "/"
        create_dir(directory)

        torch.save(self.critic, directory + "critic.pt")
        torch.save(self.target_critic, directory + "target_critic.pt")

        torch.save(self.actor, directory + "actor.pt")
        torch.save(self.target_actor, directory + "target_actor.pt")

        with open(directory + "replay_buffer.pkl", "wb") as f:
            pickle.dump(self.replay_buffer, f)

    def load(self, directory):
        if directory[-1] != "/":
            directory += "/"
        directory = directory[:-1]
        directory += "/"
        create_dir(directory)

        self.critic = torch.load(directory + "critic.pt")
        self.target_critic = torch.load(directory + "target_critic.pt")

        self.actor = torch.load(directory + "actor.pt")
        self.target_actor = torch.load(directory + "target_actor.pt")

        with open(directory + "replay_buffer.pkl", "rb") as f:
            self.replay_buffer = pickle.load(f)