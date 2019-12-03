import numpy as np
import pygame as pg

WIDTH, COLUMNS, ROWS = 400, 10, 20
DISTANCE = WIDTH // COLUMNS
HEIGHT = DISTANCE * ROWS
TETROMINODOWM = pg.USEREVENT + 1
SPEEDUP = TETROMINODOWM + 1

colors = {
    1: (64, 224, 208),
    2: (34, 139, 34),
    3: (238, 221, 130),
    4: (178, 34, 34),
    5: (255, 127, 80),
    6: (138, 43, 226),
    7: (238, 238, 0)
}

tetrominoes = np.array([
    np.array([
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]),
    np.array([
        [0, 0, 0, 0],
        [3, 3, 3, 3],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]),
    np.array([
        [0, 0, 0, 0],
        [5, 5, 5, 0],
        [0, 0, 5, 0],
        [0, 0, 0, 0]]),
    np.array([
        [0, 0, 7, 0],
        [7, 7, 7, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]),
    np.array([
        [0, 2, 2, 0],
        [2, 2, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]),
    np.array([
        [4, 4, 0, 0],
        [0, 4, 4, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]),
    np.array([
        [0, 0, 0, 0],
        [6, 6, 6, 0],
        [0, 6, 0, 0],
        [0, 0, 0, 0]])
])
