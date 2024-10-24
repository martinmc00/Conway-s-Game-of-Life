import pygame
import numpy as np

CELL_SIZE = 8            #The size of each cell

WIDTH, HEIGHT = 800, 800 #Width and height of the screen

#Number of rows and collumns that are going to be in the matrix
ROWS, COLS = int(HEIGHT/CELL_SIZE), int(WIDTH/CELL_SIZE)

WIN = pygame.display.set_mode((HEIGHT, WIDTH))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.display.set_caption("Conway's Game of Life")

#First generation, random matrix with values between 0 and 1
first_gen = np.random.randint(2, size=(ROWS, COLS))

current_gen = first_gen.copy() #Establish the first generation as the current one

#Draws each cell of the grid, black or white depending on the value in the matrix
def drawGeneration():
    for x in range(ROWS):
        for y in range(COLS):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = WHITE if current_gen[x][y] == 1 else BLACK
            pygame.draw.rect(WIN, color, rect)

#Sums the number of living neighbors of a given cell
def countNeighbours(mat, i, j):
    c = 0
    for row in range(-1, 2, 1):
        for col in range (-1, 2, 1):
            if not(row == 0 and col == 0):
                if mat[((i+row)+ROWS)%ROWS][((j+col)+COLS)%COLS] == 1:
                    c += 1
    return c

#Creates the next generation
def getNextGen():
    c = 0

    #Next generation matrix initialized as all zeros
    next_gen = np.zeros((ROWS, COLS))
    
    for row in range(ROWS):
        for col in range(COLS):
            c = countNeighbours(current_gen, row, col)
            if(current_gen[row][col] == 1): #For a living cell
                if(c >= 2 and c < 4):       #If it has 2 or 3 living neighbors
                    next_gen[row][col] = 1  #the cell continues living
            else:                           #For a dead cell
                if(c == 3):                 #If it has 3 living neighbors
                    next_gen[row][col] = 1  #the cell lives

                                            #Otherwise it stays at 0
    return next_gen

def main():
    global current_gen

    run = True

    clock = pygame.time.Clock()

    while run:
        clock.tick(15)  #Evolution speed (15 FPS)

        #Checking for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        next_gen = getNextGen()         #Create the next generation
        current_gen = next_gen.copy()   #Substitute the current generation by the new one
    
        WIN.fill(BLACK)

        drawGeneration()

        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()