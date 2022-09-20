import pygame
import csv
from pathlib import Path



DATA_BASE = 'data_b.csv'


def key_press_timer(key):
    clock = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == key:
                return int(chr(key)), (pygame.time.get_ticks() - clock) // 1000


def create_list(key,index_list,matrix_bushes,matrix_mines):
    data_list= []
    data_list= [key, index_list,matrix_bushes,matrix_mines]
    return data_list


def init_data(key,index_list,matrix_bushes,matrix_mines):
    my_file = Path(DATA_BASE)
    if not my_file.is_file():
        with open(DATA_BASE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["number",'Solider_location', 'Bushes_locations', 'Mines_locations'])
            writer.writerow(create_list(key,index_list,matrix_bushes,matrix_mines))
    else:
        with open(DATA_BASE, 'a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(create_list(key,index_list,matrix_bushes,matrix_mines))



def get_data(key):
    with open(DATA_BASE, 'r',newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == str(key[0]):
                return row
    return False





