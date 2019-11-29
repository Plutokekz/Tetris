from dataclasses import dataclass
import pygame as pg
from src.Constants import DISTANCE, COLUMNS, ROWS, colors


@dataclass
class Tetrominoe:
    tet: list
    row: int = 0
    column: int = 3

    def show(self, screen):
        for index, color in enumerate(self.tet):
            if color > 0:
                y = (self.row + index // 4) * DISTANCE
                x = (self.column + index % 4) * DISTANCE
                pg.draw.rect(screen, colors.get(color), (x, y, DISTANCE, DISTANCE))

    def valid(self, row, column, grid):
        for index, color in enumerate(self.tet):
            if color > 0:
                row_1 = row + index // 4
                column_1 = column + index % 4
                if row_1 >= ROWS or column_1 < 0 or column_1 >= COLUMNS or grid[row_1 * COLUMNS + column_1] > 0:
                    return False
        return True

    def update(self, row_off, column_off, grid):
        if self.valid(self.row + row_off, self.column + column_off, grid):
            self.row += row_off
            self.column += column_off
            return True
        return False

    def rotate(self, grid):
        copy = self.tet.copy()
        for index, color in enumerate(copy):
            row = index // 4
            column = index % 4
            self.tet[(2-column)*4+row] = color
        if not self.valid(self.row, self.column, grid):
            self.tet = copy.copy()

