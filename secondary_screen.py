import pygame, sys
import consts
from pygame.locals import *
import random



def set_matrix():
    grid = []
    for row in range(25):
        grid.append([])
        for column in range(50):
            grid[row].append(0)
    return grid


def set_slots(screen2):
    for row in range(25):
        for column in range(50):
            color = consts.SECONDELY_BLACK
            pygame.draw.rect(screen2,
                             color,
                             [(consts.SECONDELY_MARGIN + consts.SECONDELY_WIDTH) * column + consts.SECONDELY_MARGIN ,
                              (consts.SECONDELY_MARGIN  + consts.SECONDELY_HEIGHT) * row + consts.SECONDELY_MARGIN ,
                              consts.SECONDELY_WIDTH,
                              consts.SECONDELY_HEIGHT])


def save_mines(screen2, matrix_mines):
    for i in range(20):
        x = random.randint(0, 47)
        y = random.randint(0, 22)
        new_tuple = (y,x)
        show_mines(screen2, x*(consts.SECONDELY_MARGIN + consts.SECONDELY_WIDTH), y*(consts.SECONDELY_MARGIN  + consts.SECONDELY_HEIGHT))
        matrix_mines.append(new_tuple)
    return matrix_mines

def show_mines(screen2, x,y):
    img = pygame.image.load(consts.MINES_IMAGE).convert()
    img.set_colorkey(consts.BACKGROUND_GREEN)
    screen2.blit(img, (x, y))
    pygame.display.flip()

def show_dark_solider(screen2, x,y):
    img = pygame.image.load(consts.SOLIDER_NIGHT_IMAGE).convert()
    img.set_colorkey(consts.BACKGROUND_GREEN)
    screen2.blit(img, (x*(consts.SECONDELY_MARGIN + consts.SECONDELY_WIDTH), y*(consts.SECONDELY_MARGIN  + consts.SECONDELY_HEIGHT)))
    pygame.display.flip()


def show_mines_screen(): #צריך להוסיף קבלה של המיקום של החייל
    matrix_mines = []
    pygame.init()
    size = [1000, 500]
    screen2 = pygame.display.set_mode(size)
    pygame.display.set_caption("secondely screen")
    screen2.fill(consts.SECONDELY_GREEN)
    set_slots(screen2)
    show_dark_solider(screen2, 0,0)
    save_mines(screen2, matrix_mines)

    grid = []
    grid = set_matrix()


    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
    pygame.display.flip()

show_mines_screen()