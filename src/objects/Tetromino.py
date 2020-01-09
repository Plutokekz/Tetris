import pygame as pg
from Constants import DISTANCE, COLUMNS, ROWS, colors
import numpy as np


class Tetrominoe:

    def __init__(self, tetromino):
        self.tetromino = tetromino
        self.row = 0
        self.column = 3

    def show(self, screen):
        for index_row, index_column, color in self.grid_coord_color():
            y = index_row * DISTANCE
            x = index_column * DISTANCE
            pg.draw.rect(screen, colors.get(color), (x, y, DISTANCE, DISTANCE))

    def grid_coord_color(self):
        coord_colors = []
        for index_row, row in enumerate(self.tetromino):
            for index_column, column in enumerate(row):
                if column > 0:
                    coord_colors.append((self.row + index_row, self.column + index_column, column))
        return np.array(coord_colors)

    def valid(self, current_row, current_column, grid):
        for index_row, row in enumerate(self.tetromino):
            for index_column, column in enumerate(row):
                if column > 0:
                    row_1 = current_row + index_row
                    column_1 = current_column + index_column
                    if row_1 >= ROWS or column_1 < 0 or column_1 >= COLUMNS or grid[row_1][column_1]> 0:
                        return False
        return True

    def update(self, row_off, column_off, grid):
        if self.valid(self.row + row_off, self.column + column_off, grid):
            self.row += row_off
            self.column += column_off
            return True
        return False

    def rotate(self, grid):
        copy = self.tetromino.copy()
        self. tetromino = np.rot90(self.tetromino)
        if not self.valid(self.row, self.column, grid):
            self.tetromino = copy.copy()

    def hard_drop(self, grid):
        while self.update(1, 0, grid):
            pass

    def copy(self):
        copy = Tetrominoe(self.tetromino)
        copy.row = self.row
        copy.column = self.column
        return copy

    def step(self, choice, grid):
        if choice == 0:
            self.update(0, 0, grid)
        elif choice == 1:
            self.update(0, 1, grid)
        elif choice == 2:
            self.update(0, -1, grid)
        elif choice == 3:
            self.update(1, 0, grid)
        elif choice == 4:
            self.rotate(grid)
        elif choice == 5:
            self.hard_drop(grid)

