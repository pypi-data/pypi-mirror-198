from typing import Union
import numpy as np
import torch

from hbrl.agents.agent import Agent
from abc import ABC, abstractmethod
from gym.spaces import Box, Discrete
from hbrl.agents.utils.replay_buffer import ReplayBuffer


class ValueBasedAgent(Agent, ABC):

    def __init__(self, state_space: Union[Box, Discrete], action_space: Union[Box, Discrete], **params):
        """
        @param state_space: Environment's state space.
        @param action_space: Environment's action_space.
        @param params: Optional parameters.
        """
        super().__init__(state_space, action_space, **params)

        self.batch_size = params.get("batch_size", 100)
        self.buffer_max_size = params.get("buffer_max_size", int(1e6))
        self.replay_buffer = ReplayBuffer(self.buffer_max_size, self.device)

    @abstractmethod
    def get_value(self, features, actions=None):
        return 0

    @abstractmethod
    def learn(self):
        pass

    def save_interaction(self, *interaction_data):
        """
        Function that is called to ask our agent to learn about the given interaction. This function is separated from
        self.on_action_stop(**interaction_data) because we can imagine agents that do not learn on every interaction, or
        agents that learn on interaction they didn't make (like HER that add interaction related to fake goals in their
        last trajectory).
        on_action_stop is used to update variables likes self.last_state or self.simulation_time_step_id, and
        learn_interaction is used to know the set of interactions we can learn about.

        Example: Our implementation of HER show a call to 'learn_interaction' without 'on_action_stop'
        (two last lines of 'her' file).
        """
        assert not self.under_test
        self.replay_buffer.append(interaction_data)

    def sample_training_batch(self, batch_size=None):
        batch_size = self.batch_size if batch_size is None else batch_size
        return self.replay_buffer.sample(batch_size)

    def process_interaction(self, action, reward, new_state, done, learn=True):
        if learn and not self.under_test:
            self.save_interaction(self.last_state, action, reward, new_state, done)
            self.learn()
        super().process_interaction(action, reward, new_state, done, learn=learn)
