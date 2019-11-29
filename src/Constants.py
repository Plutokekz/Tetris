import pygame as pg

WIDTH, COLUMNS, ROWS = 400, 10, 20
DISTANCE = WIDTH // COLUMNS
HEIGHT = DISTANCE * ROWS
TETROMINODOWM = pg.USEREVENT + 1
SPEEDUP = TETROMINODOWM + 1

colors = {
    1: (255, 0, 255),
    2: (255, 50, 255),
    3: (255, 100, 255),
    4: (255, 0, 0),
    5: (0, 0, 255),
    6: (5, 0, 70),
    7: (255, 255, 23)
}