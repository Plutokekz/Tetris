from dataclasses import dataclass
import pygame as pg
from src.Constants import DISTANCE, COLUMNS, ROWS, colors, WIDTH, HEIGHT
import numpy as np
from PIL import Image
import cv2


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

    def get_image(self, grid):
        copy_grid = grid.copy()
        img = np.zeros((ROWS, COLUMNS, 3), dtype=np.uint8)
        for index, color in enumerate(self.tet):
            if color > 0:
                row = self.row + index // 4
                column = self.column + index % 4
                copy_grid[row * COLUMNS + column] = color
        testing = np.array(copy_grid).reshape((20, 10))
        #print(testing)
        for index, color in enumerate(copy_grid):
            if color > 0:
                x = index % COLUMNS
                y = index // COLUMNS
                img[y][x] = colors.get(color)
        img = Image.fromarray(img, 'RGB')
        #img = img.resize((200, 400))  # resizing so we can see our agent in all its glory.
        #cv2.imshow("image", np.array(img))  # show it!
        #cv2.waitKey(1)
        #breakpoint()
        return img

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

    def actions(self, choice, grid):
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

