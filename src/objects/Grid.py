from dataclasses import dataclass
from src.Constants import ROWS, COLUMNS


class Grid:
    grid: list = [0] * COLUMNS * ROWS

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
