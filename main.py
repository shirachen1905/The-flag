import screen
import solider
import MineField
import consts
import pygame, sys
import secondary_screen
from pygame.locals import *




def first_screen():
    pygame.init()
    size = (consts.WINDOE_WIDTH, consts.WINDOW_HEIGHT)
    screen1 = pygame.display.set_mode(size)
    pygame.display.set_caption("the flag shira & agam")
    screen.green_background(screen1)
    screen.show_flag(screen1)
    screen.show_bushes(screen1, matrix_bushes)
    screen.show_text(screen1)
    solider.solider_move(screen1, 0,0)
    pygame.display.flip()
    return screen1

def lose(screen1, row, col):
    screen.explosion(screen1, row, col)
    screen.lose_text(screen1)
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

def win(screen1):
    screen.win_text(screen1)
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

def solider_move_right(screen1, index_list):
    if solider.move_right(screen1, index_list[1], index_list[0]) != False:
        index_list = solider.move_right(screen1, index_list[1], index_list[0])
        row = index_list[0]
        col = index_list[1]
        screen.show_screen(screen1, matrix_bushes, row, col)
    return index_list

def solider_move_left(screen1,index_list):
    if solider.move_left(screen1, index_list[1], index_list[0]) != False:
        index_list = solider.move_left(screen1, index_list[1], index_list[0])
        row = index_list[0]
        col = index_list[1]
        screen.show_screen(screen1, matrix_bushes, row, col)
    return index_list

def solider_move_up(screen1,index_list):
    if solider.move_up(screen1, index_list[1], index_list[0]) != False:
        index_list = solider.move_up(screen1, index_list[1], index_list[0])
        row = index_list[0]
        col = index_list[1]
        screen.show_screen(screen1, matrix_bushes, row, col)
    return index_list

def solider_move_down(screen1,index_list):
    if solider.move_down(screen1, index_list[1], index_list[0]) != False:
        index_list = solider.move_down(screen1, index_list[1], index_list[0])
        row = index_list[0]
        col = index_list[1]
        screen.show_screen(screen1, matrix_bushes, row, col)
    return index_list



index_list = [0,0]
matrix_bushes = screen.set_screen()
screen1 = first_screen()
matrix_mines = secondary_screen.set_mines_screen()

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                secondary_screen.show_mines_screen(matrix_mines, index_list[1], index_list[0])
                screen.show_screen(screen1, matrix_bushes, index_list[0], index_list[1])
            elif event.key == pygame.K_RIGHT:
                index_list = solider_move_right(screen1, index_list)
            elif event.key == pygame.K_LEFT:
                index_list = solider_move_left(screen1,index_list)
            elif event.key == pygame.K_UP:
                index_list = solider_move_up(screen1,index_list)
            elif event.key == pygame.K_DOWN:
                index_list = solider_move_down(screen1,index_list)
        foot_list = solider.foot_index_calculation(index_list[1], index_list[0])
        if solider.foot_on_mines(foot_list, matrix_mines) == True:  # פיצוץ
            lose(screen1, index_list[0], index_list[1])
        if solider.touching_flag(index_list[1], index_list[0]) == True:
            win(screen1)
        if event.type == pygame.QUIT:
            finish = True
pygame.quit()

