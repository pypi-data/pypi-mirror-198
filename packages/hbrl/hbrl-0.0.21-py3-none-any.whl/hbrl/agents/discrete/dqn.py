# Goal conditioned deep Q-network
from ..utils import scale_tensor
from ..value_based_agent import ValueBasedAgent
from ..utils.mlp import MLP
import copy
import numpy as np
import torch
from torch import optim
from torch.nn import ReLU, Tanh
from gym.spaces import Box, Discrete
from typing import Union


class DQN(ValueBasedAgent):
    """
    An agent that learn an approximated Q-Function using a neural network.
    This Q-Function is used to find the best action to execute in a given observation.
    """

    name = "DQN"

    def __init__(self, state_space: Union[Box, Discrete], action_space: Union[Box, Discrete], **params):
        """
        @param state_space: Environment's state space.
        @param action_space: Environment's action_space.
        @param params: Optional parameters.
        """

        super().__init__(state_space, action_space, **params)

        self.gamma = params.get("gamma", 0.95)
        self.epsilon_min = params.get("epsilon_min", 0.01)
        self.epsilon_max = params.get("epsilon_max", 1.)
        self.epsilon_decay_delay = params.get("epsilon_decay_delay", 20)
        self.epsilon = None
        self.epsilon_decay_period = params.get("epsilon_decay_period", 1000)

        #  NEW, goals will be stored inside the replay buffer. We need a specific one with enough place to do so
        self.learning_rate = params.get("learning_rate", 0.001)
        self.steps_before_target_update = params.get("steps_before_target_update", 1)
        self.steps_since_last_target_update = 0
        self.tau = params.get("tau", 0.001)
        self.nb_gradient_steps = params.get("nb_gradient_steps", 1)

        self.epsilon_step = (self.epsilon_max - self.epsilon_min) / self.epsilon_decay_period
        self.total_steps = 0

        # NEW, The input observation size is multiplied by two because we need to also take the goal as input
        model_layers = params.get("model_layers", [64, ReLU(), 64, ReLU(), 64, ReLU()])
        model_activation = params.get("model_activation", Tanh())
        assert isinstance(model_activation, torch.nn.Module)
        self.model = MLP(self.state_size, *model_layers, self.nb_actions, model_activation,
                         learning_rate=self.learning_rate, optimizer_class=optim.Adam, device=self.device).float()

        self.criterion = torch.nn.SmoothL1Loss()
        self.target_model = copy.deepcopy(self.model).to(self.device)
        self.epsilon = self.epsilon_max

    def get_value(self, observations, actions=None):
        with torch.no_grad():
            values = self.model(observations)
            if actions is None:
                values = values.max(-1).values
            else:
                if not isinstance(actions, torch.Tensor):
                    actions = torch.tensor(actions)
                values = values.gather(1, actions.to(torch.long).unsqueeze(1))
        return values.detach().numpy()

    def action(self, state, explore=True):
        if self.simulation_time_step_id > self.epsilon_decay_delay:
            self.epsilon = max(self.epsilon_min, self.epsilon - self.epsilon_step)

        if explore and not self.under_test and np.random.rand() < self.epsilon:  # Epsilon greedy
            action = np.random.randint(self.nb_actions)
        else:
            # greedy_action(self.model, observation) function in RL5 notebook
            with torch.no_grad():
                q_values = self.model(state)
                action = torch.argmax(q_values).item()

        action = scale_tensor(action, Box(-1, 1, (self.nb_actions,)), self.action_space)
        return action

    def learn(self):
        assert not self.under_test
        for _ in range(self.nb_gradient_steps):
            if len(self.replay_buffer) > self.batch_size:
                states, actions, rewards, new_states, dones = self.sample_training_batch()
                q_prime = self.target_model(new_states).max(1)[0].detach()
                update = rewards + self.gamma * (1 - dones) * q_prime
                q_s_a = self.model(states).gather(1, actions.to(torch.long).unsqueeze(1))
                loss = self.criterion(q_s_a, update.unsqueeze(1))
                self.model.learn(loss)

        self.steps_since_last_target_update += 1
        if self.steps_since_last_target_update >= self.steps_before_target_update:
            self.target_model.converge_to(self.model, self.tau)
            self.steps_since_last_target_update = 0
