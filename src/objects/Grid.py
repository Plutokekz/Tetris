from dataclasses import dataclass
from src.Constants import ROWS, COLUMNS, colors
import cv2
import numpy as np
import random
from PIL import Image
from src.Constants import tetrominoes
from src.objects.Tetromino import Tetrominoe


class Grid:

    def __init__(self):
        self.OBSERVATION_SPACE_VALUES = (ROWS, COLUMNS, 3)
        self.ACTION_SPACE_SIZE = 6
        self.grid = np.zeros((ROWS, COLUMNS))

    def reset(self):
        self.grid = np.zeros((ROWS, COLUMNS))

    def place_tetromino_in_grid(self, figure):
        for row, column, color in figure.grid_coord_color():
            self.grid[row][column] = color

    def delete_row(self):
        rows = 0
        for index, row in enumerate(self.grid):
            for column in row:
                if column == 0:
                    break
            else:
                self.grid = np.concatenate((np.zeros((1, 10)), np.delete(self.grid, index, axis=0)))
                rows += 1
        return rows ** 2 * 100

    def get_image(self, figure):
        img = np.zeros((ROWS, COLUMNS, 3), dtype=np.uint8)
        for index_row, row in enumerate(self.grid):
            for index_column, color in enumerate(row):
                if color > 0:
                    img[index_row][index_column] = colors.get(color)
        for row, column, color in figure.grid_coord_color():
            img[row][column] = colors.get(color)
        img = Image.fromarray(img, 'RGB')
        return img

    def render(self, figure):
        img = self.get_image(figure)
        img = img.resize((200, 400))  # resizing so we can see our agent in all its glory.
        cv2.imshow("image", np.array(img))  # show it!
        cv2.waitKey(1)

    def _count_gaps(self):
        gaps = 0
        zeros = self.grid == 0
        for row in range(0, 10):
            start_counting = False
            for column in range(0, 20):
                if not zeros[column][row]:
                    start_counting = True
                if start_counting and zeros[column][row]:
                    gaps += 1
        return gaps

    def _count_heights(self):
        heights = []
        zeros = self.grid == 0
        for row in range(0, 10):
            for column in range(0, 20):
                if not zeros[column][row]:
                    heights.append(ROWS - column)
                    break
        return np.array(heights)

    def update(self, figure, done, train_score=False):
        score = 0
        if not figure.update(1, 0, self.grid):
            self.place_tetromino_in_grid(figure)
            score += self.delete_row()
            figure = Tetrominoe(random.choice(tetrominoes))
            if train_score:
                heights = self._count_heights()
                min_h, max_h, avg_h = np.argmax(heights), np.argmin(heights), np.average(heights)
                diff_h = abs(max_h) - abs(min_h)
                if max_h >= 10 or avg_h > 6 or diff_h > 3:
                    score -= min_h + max_h + min_h + 2*avg_h + diff_h + (self._count_gaps() ** 2)
            if not figure.valid(figure.row, figure.column, self.grid):
                done = True
        return score, figure, done
