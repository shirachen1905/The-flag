import screen
import solider
import MineField
import consts
import pygame, sys
import secondary_screen
from pygame.locals import *



matrix_bushes = screen.set_screen()



pygame.init()
size = (consts.WINDOE_WIDTH, consts.WINDOW_HEIGHT)
screen1 = pygame.display.set_mode(size)
pygame.display.set_caption("the flag shira & agam")
screen.green_background(screen1)
screen.show_flag(screen1)
screen.show_bushes(screen1, matrix_bushes)
screen.show_text(screen1)
col=0
row=0
solider.solider_move(screen1, row,col)
pygame.display.flip()



matrix_mines = secondary_screen.set_mines_screen()
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if solider.move_right(screen1, col, row) != False:
                    index_list = solider.move_right(screen1, col, row)
                    row = index_list[0]
                    col = index_list[1]
                    screen.show_screen(screen1, matrix_bushes, row, col)
            elif event.key == pygame.K_LEFT:
                if solider.move_left(screen1, col, row ) != False:
                    index_list1 = solider.move_left(screen1, col, row )
                    row = index_list1[0]
                    col = index_list1[1]
                    screen.show_screen(screen1, matrix_bushes, row, col)
            elif event.key == pygame.K_UP:
                if solider.move_up(screen1, col, row) != False:
                    index_list2 = solider.move_up(screen1, col, row)
                    row = index_list2[0]
                    col = index_list2[1]
                    screen.show_screen(screen1, matrix_bushes, row, col)
            elif event.key == pygame.K_DOWN:
                if solider.move_down(screen1, col, row) != False:
                    index_list3 = solider.move_down(screen1, col, row)
                    row = index_list3[0]
                    col = index_list3[1]
                    screen.show_screen(screen1, matrix_bushes, row, col)
            elif event.key == pygame.K_RETURN:#לא עובד
                secondary_screen.show_mines_screen(matrix_mines, col, row)
                screen.show_screen(screen1, matrix_bushes, row, col)
        foot_list = solider.foot_index_calculation(col, row)
        if solider.foot_on_mines(foot_list, matrix_mines) == True:  # פיצוץ
            screen.explosion(screen1, row, col)
            screen.lose_text(screen1)
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()
        if solider.touching_flag(col,row) == True:
            screen.win_text(screen1)
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()
        if event.type == pygame.QUIT:
            finish = True

    #pygame.display.flip()

pygame.quit()
