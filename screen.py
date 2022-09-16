import pygame, sys
import consts
from pygame.locals import *
import random


def green_background(screen):
    screen.fill(consts.BACKGROUND_GREEN)

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

def Place_bushes (screen):
    for i in range(20):
        x = random.randint(40, 920)
        y = random.randint(60, 420)
        img = pygame.image.load(consts.BUSH_IMAGE).convert()
        img.set_colorkey(consts.BACKGROUND_GREEN)
        screen.blit(img, (x, y))
        pygame.display.flip()
