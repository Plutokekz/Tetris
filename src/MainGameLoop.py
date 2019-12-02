import pygame as pg
import random
from src.objects.Tetromino import Tetrominoe
from src.objects.Grid import Grid
from src.Constants import HEIGHT, WIDTH, COLUMNS, DISTANCE, colors, SPEEDUP, TETROMINODOWM


speed = 500
tetrominoes = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0],
               [0, 0, 7, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [4, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 6, 6, 6, 0, 0, 6, 0, 0, 0, 0, 0, 0]]


def main():
    # Pygame initialisations Screen size Events, Clock and Key repeat
    pg.init()
    screen = pg.display.set_mode([WIDTH, HEIGHT])
    pg.time.set_timer(TETROMINODOWM, speed)
    pg.time.set_timer(SPEEDUP, 30_000)
    pg.key.set_repeat(1, 100)
    clock = pg.time.Clock()

    # Game variables initialisation
    score, level, run = 0, 0, True
    grid = Grid()

    # Create first Tetrominoe
    figure = Tetrominoe(random.choice(tetrominoes))

    # Main Game loop
    while run:
        clock.tick(60)
        # Get the Pygame Events and make the corresponding actions
        for event in pg.event.get():
            # Check for the quit event
            if event.type == pg.QUIT:
                run = False
            # Check for the TETROMINODOWM event and update the grid and if needed the score and spawn a new one
            if event.type == TETROMINODOWM:
                if not figure.update(1, 0, grid.grid):
                    grid.update_grid(figure)
                    score += grid.delete_row()
                    figure = Tetrominoe(random.choice(tetrominoes))
                    print(grid._count_gaps())
                    if not figure.valid(figure.row, figure.column, grid.grid):
                        run = False
            # Check for the SPEEDUP event which increases the speed and the level
            if event.type == SPEEDUP:
                pg.time.set_timer(TETROMINODOWM, int(speed*0.8))
                level += 1
            # Check for the Keyboard inputs
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    figure.update(0, -1, grid.grid)
                if event.key == pg.K_RIGHT:
                    figure.update(0, 1, grid.grid)
                if event.key == pg.K_DOWN:
                    figure.update(1, 0, grid.grid)
                if event.key == pg.K_LCTRL:
                    figure.rotate(grid.grid)
        # Fill the screen with Black to reset him
        screen.fill((0, 0, 0))
        # Render the Tetromino
        figure.show(screen)
        # Render the placed Tetrominos
        for index, color in enumerate(grid.grid):
            if color > 0:
                x = index % COLUMNS * DISTANCE
                y = index // COLUMNS * DISTANCE
                pg.draw.rect(screen, colors.get(color), (x, y, DISTANCE, DISTANCE))
        # Render Level and Score
        text_surface = pg.font.SysFont('impact', 40).render(f'{score:,}', False, (255, 255, 255))
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 5))
        text_surface = pg.font.SysFont('impact', 40).render(f'Level: {level}', False, (150, 150, 150))
        screen.blit(text_surface, (WIDTH - text_surface.get_width() - 10, 5))
        # Show the rendered screen
        pg.display.flip()
    print(f"Score: {score:,}, Level: {level}")
    pg.quit()


if __name__ == "__main__":
    main()
