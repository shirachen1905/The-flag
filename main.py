import screen
import solider
import MineField
import consts
import pygame, sys
import secondary_screen
from pygame.locals import *

pygame.init()
size = (consts.WINDOE_WIDTH, consts.WINDOW_HEIGHT)
screen1 = pygame.display.set_mode(size)
pygame.display.set_caption("the flag shira & agam")
screen.green_background(screen1)
#בדיקת משבצות
#secondary_screen.set_slots(screen1)
screen.show_flag(screen1)
screen.Place_bushes(screen1)
screen.show_text(screen1)
x=0
y=0

solider.solider_move(screen1, y,x)
pygame.display.flip()



finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    pygame.display.flip()

pygame.quit()
