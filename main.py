import pygame
import numpy as np

RULE = 110

CELL_SIZE = 10

WIDTH, HEIGHT = 600, 600

ROWS, COLS = int(HEIGHT/CELL_SIZE), int(WIDTH/CELL_SIZE)

WIN = pygame.display.set_mode((HEIGHT, WIDTH))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.display.set_caption("Conway's Game of Life")

first_gen = np.random.randint(2, size=(ROWS, COLS))

#current_gen = np.zeros((ROWS, COLS))

current_gen = first_gen.copy()

def drawGeneration():
    for x in range(ROWS):
        for y in range(COLS):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = WHITE if current_gen[x][y] == 1 else BLACK
            pygame.draw.rect(WIN, color, rect)

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        WIN.fill(BLACK)

        drawGeneration()

        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()