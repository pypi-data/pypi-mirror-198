import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation


class SokobanVisualizer:
    
    """
    A Module to Help Visualize Sokoban Environment

    Description
        - vis_state_snapshot: A function that takes one state as input and draws a gridworld image.
        - vis_state_animation: A function that converts the sequence of states into gridworld image animation.
        - get_image_numpy: A function that converts a state into a 3-D numpy image. If you want to customize
                           the visualization part, you just need to save the data through this function.
    """

    def __init__(self):
        self.legend_elements = [Line2D([0], [0], linestyle='', marker='s', color='blue', label='Player', markersize=10),
                                Line2D([0], [0], linestyle='', marker='s', color='red', label='Box', markersize=10),
                                Line2D([0], [0], linestyle='', marker='s', color='green', label='Storage', markersize=10)]
        self.image_obj = None
        return
    
    @staticmethod
    def get_image_numpy(state):

        """
        A function that converts dictionary-type state into numpy ndarray image forms.
        """

        nrow = state['nrow']
        ncol = state['ncol']
        player_position = state['player_position']
        box_position = state['box_position']
        storage_position = state['storage_position']
        wall_position = state['wall_position']

        image = np.ones((nrow, ncol, 3))
        for position, rgb_code in zip([storage_position, [player_position], box_position, wall_position],
                                      [[0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 0, 0]]):
            for pos in position:
                image[pos // ncol, pos % ncol, :] = rgb_code
        return image

    def vis_state_snapshot(self, state, figsize=None, grid=True):

        """
        A function that takes one state as input and draws a gridworld image.

        Parameters
        ----------
        state : dict
            A state sampled by Sokoban sampler. See help(BaseSampler).
        figsize : tuple(float) or None
            Width, height in inches. Set default if None.
        grid : bool
            If True, it draws grid.
        """

        if figsize is not None:
            plt.figure(figsize=figsize)
        image = self.get_image_numpy(state)
        plt.imshow(image)
        plt.xticks([i - 0.5 for i in range(state['ncol'])], [])
        plt.yticks([i - 0.5 for i in range(state['nrow'])], [])
        if grid:
            plt.grid()
        plt.legend(handles=self.legend_elements, loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        plt.show()
        return
    
    def vis_state_animation(self, history, figsize=None, grid=True):

        """
        A function that takes one state as input and draws a gridworld image.

        Parameters
        ----------
        history : list[dict]
            A list of consecutive states. Each state should fit the format provided by the sampler, see help(BaseSampler) for more information.
        figsize : tuple(float)
            Width, height in inches. Set default if None.
        grid : bool
            If True, it draws grid.
        """

        frames = []
        for state in history:
            frame = self.get_image_numpy(state)
            frames.append(frame)

        rc('animation', html='jshtml')
        if figsize is not None:
            plt.figure(figsize=figsize)
        fig, _ = plt.subplots()
        self.image_obj = plt.imshow(np.ones((state['nrow'], state['ncol'], 3)))
        plt.xticks([i - 0.5 for i in range(state['ncol'])], [])
        plt.yticks([i - 0.5 for i in range(state['nrow'])], [])
        if grid:
            plt.grid()
        plt.legend(handles=self.legend_elements, loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        ani = FuncAnimation(fig, self.update, frames=frames)
        return ani

    def update(self, frame):
        self.image_obj.set_data(frame)
        return self.image_obj
