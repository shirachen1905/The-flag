import screen
import consts
import pygame, sys

def solider_move(screen, col, row):
    img = pygame.image.load(consts.SOLIDER_IMAGE).convert()
    img.set_colorkey(consts.BACKGROUND_GREEN)
    screen.blit(img, (col*consts.SLOT_SIZE, row*consts.SLOT_SIZE))
    pygame.display.flip()


def foot_index_calculation(col, row):
    foot_list = []
    tuple1 = (row+3 , col)
    tuple2 = (row+3 , col+1)
    foot_list.append(tuple1)
    foot_list.append(tuple2)
    return foot_list

def foot_on_mines(foot_list,matrix_mines):
    for row in matrix_mines:
        for foot in foot_list:
            x = row[1]
            y = row[1]
            x_foot = foot[0]
            y_foot = foot[1]
            if row == foot:
                return True
            elif x == x_foot and y_foot == y+1:
                return True
            elif x == x_foot and y_foot == y+2:
                return True
    return False

def body_index_calculation(col, row):
    body_list = []
    for i in range(0,3):
        for j in range(0,2):
            new_tuple = (row+i, col+j)
            body_list.append(new_tuple)
    return body_list

def flag_index_calculation():
    flag_list = []
    row = 21
    col = 46
    for i in range(0,3):
        for j in range(0,4):
            new_tuple = (row+i, col+j)
            flag_list.append(new_tuple)
    return flag_list


def touching_flag(col,row):#המיקום של החייל
    body_list = body_index_calculation(col, row)
    flag_list = flag_index_calculation()
    for i in flag_list:
        for j in body_list:
            if i == j:
                return True
    return False


def move_right(screen, col, row):
    if col+1 <= 48:
        solider_move(screen, col+1, row) # להציג את החייל שם ולהחזיר את האינדקס שלו
        return [row, col +1]
    else:
        return False

def move_left(screen, col, row):
    if col-1 >= 0:
        solider_move(screen, col - 1, row)  # להציג את החייל שם ולהחזיר את האינדקס שלו
        return [row, col - 1]
    else:
        return False

def move_up(screen, col, row):
    if row -1 >= 0:
        solider_move(screen, col, row-1)  # להציג את החייל שם ולהחזיר את האינדקס שלו
        return [row - 1, col]
    else:
        return False

def move_down(screen, col, row):
    if row +1 <= 21:
        solider_move(screen, col, row + 1)  # להציג את החייל שם ולהחזיר את האינדקס שלו
        return [row + 1, col]
    else:
        return False



