import screen
import solider
import MineField
import consts
import pygame, sys




def solider_move(screen, col, row):
    img = pygame.image.load(consts.SOLIDER_IMAGE).convert()
    img.set_colorkey(consts.BACKGROUND_GREEN)
    screen.blit(img, (col*consts.SLOT_SIZE, row*consts.SLOT_SIZE))
    #pygame.display.flip()