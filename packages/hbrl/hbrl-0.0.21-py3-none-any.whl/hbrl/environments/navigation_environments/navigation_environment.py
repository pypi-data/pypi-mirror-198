import abc
import importlib
import random
from typing import Union
from enum import Enum
from scipy.spatial import distance
from skimage.draw import line_aa
import numpy as np
from gym.spaces import Box, Discrete
from gym.vector.utils import batch_space
from hbrl.environments.goal_reaching_environment import GoalReachingEnv
from ..environment import Environment
from .maps.maps_index import MapsIndex

class Colors(Enum):
    EMPTY = [250, 250, 250]
    WALL = [50, 54, 51]
    TILE_BORDER = [50, 54, 51]
    START = [213, 219, 214]
    AGENT = [0, 0, 255]
    REWARD = [73, 179, 101]
    GOAL = [73, 179, 101]
    TERMINAL_FAIL = [255, 31, 31]


class TileType(Enum):
    EMPTY = 0
    WALL = 1
    START = 2
    REWARD = 3
    TERMINAL_FAIL = 4


def load_builtin_map(map_index: MapsIndex) -> np.ndarray:
    """
    Load the map with the given index and return it as a numpy array.
    """
    return np.array(importlib.import_module("hbrl.environments.maps." + map_index.value).maze_array)


class NavigationEnv(Environment, abc.ABC):

    """
    An environment where the agent navigate inside a maze.
    It will load a map and is able to render image that show a maze representation.
    """

    name = "Default navigation environment"

    def __init__(self, maze_map: np.ndarray, state_space: Union[Box, Discrete], action_space: Union[Box, Discrete],
                 reset_anywhere=False):
        """
        @param maze_map: A row major numpy array where each element is a tile value following TileType enum.
                        Some builtin maps can be found in hbrl.environments.navigation_environments.maps and can be
                        loaded using load_builtin_map above.
        """

        self.maze_map = maze_map
        self.height, self.width = self.maze_map.shape
        self.state = None
        self.reset_anywhere = reset_anywhere

        high = np.array([self.width, self.height]) / 2
        low = - high

        self.state_space = Box(low=np.concatenate((low, state_space.low)),
                               high=np.concatenate((high, state_space.high)))
        self.action_space = action_space

        super().__init__(self.state_space, self.action_space)

    def get_state_from_coordinates(self, x, y, uniformly_sampled=True):
        """
        Return a numpy array (state) that belongs to X and Y coordinates in the grid.
        If uniformly_sampled == True, the result state is a state uniformly sampled in the area
        covered by tile at coordinate x, y.
        """
        assert self.is_valid_coordinates(x, y)
        x_value = x + .5 - self.width / 2
        y_value = - (y + .5 - self.height / 2)
        if isinstance(x, np.ndarray):
            state = batch_space(self.state_space, x_value.shape[0]).sample()
        else:
            state = self.state_space.sample()

        state[..., :2] = np.asarray([x_value, y_value]).T
        if uniformly_sampled:
            state[:2] += np.random.uniform(-0.5, 0.5, (2,))
        return state

    def get_coordinates(self, state):
        """
        return the coordinates of the tile where the given state is inside.
        """
        return round(state[0].item() -.5 + self.width / 2), round(- state[1].item() - .5 + self.height / 2)

    def is_valid_coordinates(self, x: Union[np.ndarray, int], y: Union[np.ndarray, int]) -> bool:
        if isinstance(x, np.ndarray) and x.shape[0] > 1:
            assert isinstance(y, np.ndarray)
            assert len(x.shape) == 1
            assert y.shape == x.shape
            return (0 <= x).all() and (x < self.width).all() and (0 <= y).all() and (y < self.height).all()
        return 0 <= x < self.width and 0 <= y < self.height

    def is_valid_state(self, state):
        return self.state_space.contains(state.astype(self.state_space.dtype))

    def reachable(self, state):
        return self.is_valid_state(state) and self.get_tile_type(*self.get_coordinates(state)) != TileType.WALL

    def get_tile_type(self, x: int, y: int) -> TileType:
        assert self.is_valid_coordinates(x, y)
        return TileType(self.maze_map[y][x].item())

    def get_reward_done(self, state) -> (float, bool):
        tile_type = self.get_tile_type(*self.get_coordinates(state))
        done = tile_type == TileType.TERMINAL_FAIL
        if tile_type == TileType.TERMINAL_FAIL:
            reward = -10
        elif tile_type == TileType.REWARD:
            reward = 1
        else:
            reward = 0
        return reward, done

    @abc.abstractmethod
    def step(self, action):
        pass

    def reset(self):
        if self.reset_anywhere:
            self.state = self.sample_reachable_state()
        else:
            start_tile = np.flip(random.choice(np.argwhere(self.maze_map == 2)))
            self.state = self.get_state_from_coordinates(*start_tile, uniformly_sampled=False)
        return self.state

    """
    Rendering functions
    """
    def get_color(self, x, y, ignore_agent=False, ignore_rewards=False) -> list:
        agent_x, agent_y = self.get_coordinates(self.state)
        if (agent_x, agent_y) == (x, y) and not ignore_agent:
            return Colors.AGENT.value
        else:
            tile_type = self.get_tile_type(x, y)
            if tile_type == TileType.REWARD:
                return Colors.EMPTY.value if ignore_rewards else Colors.REWARD.value
            else:
                try:
                    return Colors.__getattr__(tile_type.name).value
                except AttributeError:
                    raise AttributeError("Unknown tile type")

    def set_tile_color(self, image_array: np.ndarray, x, y, color, tile_size=10, border_size=0) -> np.ndarray:
        """
        Set a tile color with the given color in the given image as a numpy array of pixels
        :param image_array: The image where the tile should be set
        :param x: X coordinate of the tile to set
        :param y: Y coordinate of the tile to set
        :param color: new color of the tile : numpy array [Red, Green, Blue]
        :param tile_size: size of the tile in pixels
        :param border_size: size of the tile's border in pixels
        :return: The new image
        """
        tile_img = np.zeros(shape=(tile_size, tile_size, 3), dtype=np.uint8)

        if border_size > 0:
            tile_img[:, :, :] = Colors.TILE_BORDER.value
            tile_img[border_size:-border_size, border_size:-border_size, :] = color
        else:
            tile_img[:, :, :] = color

        y_min = y * tile_size
        y_max = (y + 1) * tile_size
        x_min = x * tile_size
        x_max = (x + 1) * tile_size
        image_array[y_min:y_max, x_min:x_max, :] = tile_img
        return image_array

    def get_environment_background(self, tile_size=10, ignore_rewards=False) -> np.ndarray:
        """
        Return an image (as a numpy array of pixels) of the environment background.
        :return: environment background -> np.ndarray
        """
        # Compute the total grid size
        width_px = self.width * tile_size
        height_px = self.height * tile_size

        img = np.zeros(shape=(height_px, width_px, 3), dtype=np.uint8)

        # Render the grid
        for y in range(self.height):
            for x in range(self.width):
                cell_color = self.get_color(x, y, ignore_agent=True, ignore_rewards=ignore_rewards)
                img = self.set_tile_color(img, x, y, cell_color)
        return img

    def get_oracle(self) -> list:
        """
        Return an oracle as a list of every reachable states inside the environment.
        """
        reachable_coordinates = np.argwhere(self.maze_map != 1).tolist()
        return [self.get_state_from_coordinates(x, y) for x, y in reachable_coordinates]

    def sample_reachable_state(self):
        start_tile = np.flip(random.choice(np.argwhere(self.maze_map != 1)))
        return self.get_state_from_coordinates(*start_tile)

    def render(self, ignore_agent=False, ignore_rewards=False):
        """
        Render the whole-grid human view
        """
        if self.state is None:
            self.reset()
        img = self.get_environment_background(ignore_rewards=ignore_rewards)
        if not ignore_agent:
            self.place_point(img, self.state, Colors.AGENT.value)
        return img

    def place_point(self, image: np.ndarray, state, color: Union[np.ndarray, list], width=5):
        """
        Modify the input image
        param image: Initial image that will be modified.
        param x: x coordinate in the state space of the point to place.
        param y: y coordinate in the state space of the point to place.
        param color: Color to give to the pixels that compose the point.
        param width: Width of the circle (in pixels).
        """
        assert isinstance(state, np.ndarray)
        assert len(state.shape) == 1
        state = state[:2]

        if isinstance(color, list):
            color = np.array(color)

        state_space_range = (self.state_space.high - self.state_space.low)[:2]
        center = (state - self.state_space.low[:2]) / state_space_range
        center[1] = 1 - center[1]
        center_y, center_x = (image.shape[:2] * np.flip(center)).astype(int)

        # Imagine a square of size width * width, with the coordinates computed above as a center. Iterate through
        # each pixel inside this square to
        radius = width
        for i in range(center_x - radius, center_x + radius):
            for j in range(center_y - radius, center_y + radius):
                dist = distance.euclidean((i, j), (center_x, center_y))
                if dist < radius and 0 <= i < image.shape[1] and 0 <= j < image.shape[0]:
                    image[j, i] = color
        return image

    def place_edge(self, image: np.ndarray, state_1, state_2, color: Union[np.ndarray, list]):
        """
        Modify the input image
        param image: Initial image that will be modified.
        param x: x coordinate in the state space of the point to place.
        param y: y coordinate in the state space of the point to place.
        param color: Color to give to the pixels that compose the point.
        param width: Width of the circle (in pixels).
        """
        assert isinstance(state_1, np.ndarray)
        assert len(state_1.shape) == 1
        assert isinstance(state_2, np.ndarray)
        assert len(state_2.shape) == 1
        state_1 = state_1[:2]
        state_2 = state_2[:2]
        if isinstance(color, list):
            color = np.array(color)
        state_space_range = (self.state_space.high - self.state_space.low)[:2]

        center = (state_1 - self.state_space.low[:2]) / state_space_range
        center[1] = 1 - center[1]
        center_y_1, center_x_1 = (image.shape[:2] * np.flip(center)).astype(int)

        center = (state_2 - self.state_space.low[:2]) / state_space_range
        center[1] = 1 - center[1]
        center_y_2, center_x_2 = (image.shape[:2] * np.flip(center)).astype(int)

        rr, cc, val = line_aa(center_y_1, center_x_1, center_y_2, center_x_2)
        old = image[rr, cc]
        extended_val = np.tile(val, (3, 1)).T
        image[rr, cc] = (1 - extended_val) * old + extended_val * color


class GoalReachingNavEnv(GoalReachingEnv, NavigationEnv):

    """
    This environment wrap an hbrl.environment.NavigationEnvironment instance to make it goal-conditioned.
    at each reset, a goal is sampled from reachable states in the NavigationEnvironment map, and the reward depends if
    the sampled goal has been reached or not.
    """

    name = "GoalReachingNavEnv Default"

    def __init__(self, wrapped_environment, goal_space: Union[None, Box, Discrete]=None, sparse_reward=True):
        assert isinstance(wrapped_environment, NavigationEnv)
        GoalReachingEnv.__init__(self, wrapped_environment, goal_space, sparse_reward)

    def sample_goal(self):
        goal_coordinates = np.flip(random.choice(np.argwhere(self.maze_map != 1)))
        return self.get_goal_from_state(
            self.get_state_from_coordinates(*goal_coordinates, uniformly_sampled=True)
        )

    """
    Rendering functions
    """

    def render(self, ignore_agent=False, ignore_goal=False):
        """
        Render the whole-grid human view
        """
        image = self.wrapped_environment.render(ignore_agent=ignore_agent, ignore_rewards=True)
        if not ignore_goal:
            self.place_point(image, self.goal, Colors.GOAL.value)
        return image