from dataclasses import dataclass
from src.Constants import ROWS, COLUMNS
import cv2
import numpy as np


class Grid:
    ACTION_SPACE_SIZE: int = 5
    grid: list = [0] * COLUMNS * ROWS

    def __init__(self):
        self.OBSERVATION_SPACE_VALUES = (ROWS, COLUMNS, 3)

    def reset(self):
        self.grid = [0] * COLUMNS * ROWS

    def update_grid(self, figure):
        for index, color in enumerate(figure.tet):
            if color > 0:
                row = figure.row + index // 4
                column = figure.column + index % 4
                self.grid[row * COLUMNS + column] = color

    def delete_row(self):
        rows = 0
        for row in range(ROWS):
            for column in range(COLUMNS):
                if self.grid[row * COLUMNS + column] == 0:
                    break
            else:
                del self.grid[row * COLUMNS:row * COLUMNS + COLUMNS]
                self.grid[0:0] = [0] * COLUMNS
                rows += 1
        return rows ** 2 * 100

    def step(self, action, figure):
        figure.actions(action, self.grid)
        return 1, np.array(figure.get_image(self.grid))

    def render(self, figure):
        img = figure.get_image(self.grid)
        img = img.resize((200, 400))  # resizing so we can see our agent in all its glory.
        cv2.imshow("image", np.array(img))  # show it!
        cv2.waitKey(1)

    def _count_gaps(self):
        gap_count = 0
        heights = []
        array = np.array(self.grid.copy()).reshape((20, 10))
        for index, row in enumerate(array):
            for index_2, column in enumerate(row):
                if column > 0:
                    while not index + 1 > len(array) - 1:
                        if array[index + 1][index_2] == 0:
                            gap_count += 1
                        index += 1
        for index, column in enumerate(array[19]):
            height = 0
            if column > 0:
                for index_2 in reversed(range(0, 20)):
                    if array[index_2][index] > 0:
                        height += 1
            heights.append(height)

        return gap_count, heights

    def calc_reward(self):
        gaps, height = self._count_gaps()
        height = np.array(height)
        highest = height[height.argmax()]
        avg = np.average(height)
        return gaps + highest + avg

