import numpy as np
from gym.spaces import Box
from hbrl.agents.goal_conditioned_wrappers.her import HER


class TILO(HER):
    """
    A global agent class for goal conditioned agents. The # NEW tag indicate differences between Agent class and this
    one.
    """

    def __init__(self, reinforcement_learning_agent_class, state_space, action_space, **params):
        assert isinstance(state_space, Box), "The state space should be an instance of gym.spaces.Box. " \
                                             "Discrete state space is not supported."

        super().__init__(reinforcement_learning_agent_class, state_space, action_space, **params)
        self.name = self.reinforcement_learning_agent.name + " + TILO"

    @property
    def feature_space(self):
        if isinstance(self.state_space, Box):
            return Box(low=self.state_space.low - self.state_space.high,
                       high=self.state_space.high - self.state_space.low)
        else:
            return self.state_space

    def get_features(self, states, goals):

        if len(states.shape) == 1 and len(goals.shape) == 2:
            states = np.repeat(states, goals.shape[0]).reshape(states.shape[0], goals.shape[0])
        elif len(goals.shape) == 1 and len(states.shape) == 2:
            goals = np.repeat(goals, states.shape[0]).reshape(goals.shape[0], states.shape[0])
        assert states.shape[:-1] == goals.shape[:-1]

        features = states.copy()
        if len(states.shape) == 1:
            state_goal_diff = goals - states[self.state_to_goal_filter]
            features[self.state_to_goal_filter] = state_goal_diff
        else:
            state_goal_diff = goals - states[:, self.state_to_goal_filter]
            features[:, self.state_to_goal_filter] = state_goal_diff
        return features
