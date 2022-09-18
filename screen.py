import pygame, sys
import consts
from pygame.locals import *
import random
import solider


def green_background(screen):
    screen.fill(consts.BACKGROUND_GREEN)

def set_screen():
    matrix_bushes = []
    Place_bushes(matrix_bushes)
    return matrix_bushes

def show_screen(screen1, matrix_bushes, row, col):
    pygame.init()
    size = (consts.WINDOE_WIDTH, consts.WINDOW_HEIGHT)
    screen1 = pygame.display.set_mode(size)
    pygame.display.set_caption("the flag shira & agam")
    green_background(screen1)
    show_flag(screen1)
    show_bushes(screen1, matrix_bushes)
    solider.solider_move(screen1, col, row)
    pygame.display.flip()

def show_solider(screen):
    img = pygame.image.load(consts.SOLIDER_IMAGE).convert()
    img.set_colorkey(consts.BACKGROUND_GREEN)
    screen.blit(img, (0, 0))
    pygame.display.flip()

def show_flag(screen,):
    img = pygame.image.load(consts.FLAG_IMAGE).convert()
    img.set_colorkey(consts.BACKGROUND_GREEN)
    screen.blit(img, (940,440 ))
    pygame.display.flip()


def show_bushes(screen1, matrix_bushes):
    for row in matrix_bushes:
        y = row[0]
        x = row[1]
        img = pygame.image.load(consts.BUSH_IMAGE).convert()
        img.set_colorkey(consts.BACKGROUND_GREEN)
        screen1.blit(img, (x*(consts.SECONDELY_MARGIN + consts.SECONDELY_WIDTH), y*(consts.SECONDELY_MARGIN  + consts.SECONDELY_HEIGHT)))
        pygame.display.flip()


def Place_bushes (matrix_bushes):
    for i in range(20):
        x = random.randint(0, 47)
        y = random.randint(0, 22)
        new_tuple = (y, x)
        matrix_bushes.append(new_tuple)
    return matrix_bushes


def show_text(screen):
    font1 = pygame.font.SysFont("Welcome to The Flag game:", 25)
    img1 = font1.render("Welcome to The Flag game:", True, consts.WHITE)
    screen.blit(img1, (40, 20))
    font2 = pygame.font.SysFont("Have fun!", 25)
    img2 = font2.render("Have fun!", True, consts.WHITE)
    screen.blit(img2, (40, 40))


def lose_text(screen):
    font = pygame.font.SysFont("You lose", 100)
    lose = font.render("You lose", True, consts.WHITE)
    screen.blit(lose, (350, 300))
    pygame.display.flip()
    pygame.display.update()


def win_text(screen):
    font = pygame.font.SysFont("You won!!", 100)
    win = font.render("You won!!", True, consts.WHITE)
    screen.blit(win, (350, 300))
    pygame.display.flip()
    pygame.display.update()

def explosion(screen, row, col):
    img = pygame.image.load(consts.INJURY_IMAGE).convert()
    img.set_colorkey(consts.BACKGROUND_GREEN)
    screen.blit(img, (col * consts.SLOT_SIZE, (row) * consts.SLOT_SIZE))
    img2 = pygame.image.load(consts.EXPLOTION_IMAGE).convert()
    img2.set_colorkey(consts.BACKGROUND_GREEN)
    screen.blit(img2, (col * consts.SLOT_SIZE, (row+3) * consts.SLOT_SIZE))
    pygame.display.flip()