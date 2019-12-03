from src.Constants import ROWS, COLUMNS, colors
import cv2
import numpy as np
import random
from PIL import Image
from src.Constants import tetrominoes
from src.objects.Tetromino import Tetrominoe


class Grid:

    def __init__(self, grid=None):
        self.OBSERVATION_SPACE_VALUES = (ROWS, COLUMNS, 3)
        self.ACTION_SPACE_SIZE = 6
        if grid is not None:
            self.grid = grid
        else:
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
                print(f'Delete row: {row}')
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

    @staticmethod
    def _count_gaps(grid):
        gaps = 0
        zeros = grid == 0
        for row in range(0, 10):
            start_counting = False
            for column in range(0, 20):
                if not zeros[column][row]:
                    start_counting = True
                if start_counting and zeros[column][row]:
                    gaps += 1
        return gaps

    @staticmethod
    def _count_heights(grid):
        heights = []
        zeros = grid == 0
        for row in range(0, 10):
            for column in range(0, 20):
                if not zeros[column][row]:
                    heights.append(ROWS - column)
                    break
        if heights:
            heights = np.array(heights)
        else:
            heights = None
        return heights

    @staticmethod
    def calc_reward(grid):
        heights = Grid._count_heights(grid)
        if heights is not None:
            min_h, max_h, avg_h = np.argmax(heights), np.argmin(heights), np.average(heights)
            diff_h = abs(max_h) - abs(min_h)
            return - (min_h + max_h + min_h + 2 * avg_h + diff_h + (Grid._count_gaps(grid) ** 2))
        return - (Grid._count_gaps(grid) ** 2)

    def update(self, figure, done):
        score = 0
        if not figure.update(1, 0, self.grid):
            self.place_tetromino_in_grid(figure)
            score += self.delete_row()
            figure = Tetrominoe(random.choice(tetrominoes))
            if not figure.valid(figure.row, figure.column, self.grid):
                done = True
        return score, figure, done
