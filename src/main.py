import numpy as np


class Field:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = np.full((self.height, self.width), 0, dtype=np.uint8)

    def _clear_row(self):
        for index, row in enumerate(self.field):
            if np.count_nonzero(row) == 10:
                self.field = np.delete(self.field, index, axis=0)
                self.field = np.concatenate([np.zeros((1, 10)), self.field])

    def drop(self, brick, row=5):
        pass

    def move_left(self, brick):
        pass

    def move_right(self, brick):
        pass





field = Field(10, 20)
field.field[19] = np.array([1,1,1,1,1,1,1,1,1,1])
field._clear_row()
