import screen
import solider
import MineField
import consts
import pygame, sys

from pygame.locals import *

#יצירת מסך שבןדק אם האירוע הוא יציאה
pygame.init()
size = (consts.WINDOE_WIDTH, consts.WINDOW_HEIGHT)
screen1 = pygame.display.set_mode(size)
pygame.display.set_caption("the flag shira & agam")
#fill screen and show
screen.green_background(screen1)
#show solider
screen.show_solider(screen1)
screen.show_flag(screen1)
screen.Place_bushes(screen1)
pygame.display.flip()
"""
counter = 0
while counter !=50:
    solider.solider_move(screen1, 1, 0)
    pygame.display.flip()
    counter +=1
"""
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
pygame.quit()
