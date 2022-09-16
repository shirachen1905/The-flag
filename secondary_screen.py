import pygame, sys
import consts
from pygame.locals import *
import random

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH = 10
HEIGHT = 10
MARGIN = 2
# set the array
grid = []
for row in range(25):
    grid.append([])
    for column in range(50):
        grid[row].append(0)
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[0][0] = 1

pygame.init()

# Set the width and height of the screen [width, height]
size = [1000, 500]
screen = pygame.display.set_mode(size)
# set the tittle of the game
pygame.display.set_caption("My Array Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
# while not done:
# --- Main event loop
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    # Draw the grid
    for row in range(25):
        for column in range(50):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
