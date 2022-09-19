import pygame
import pandas as pd
import csv
import os


DATA_BASE = 'dataBase.csv'
df = pd.DataFrame(columns=['Solider_location', 'Bushes_locations', 'Mines_locations'],
                      index=[1, 2, 3, 4, 5, 6, 7, 8, 9])


def key_press_timer(key):
    clock = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == key:
                return int(chr(key)), (pygame.time.get_ticks() - clock) // 1000


def create_dict(key,index_list,matrix_bushes,matrix_mines):
    data_dict1 = {}
    data_dict1[key] = [index_list,matrix_bushes,matrix_mines]
    return data_dict1

"""לסדר את הפונקציה הזאת כי זה אותו דבר"""
def init_dict(key,index_list,matrix_bushes,matrix_mines):
    data_dict = create_dict(key, index_list, matrix_bushes, matrix_mines)
    if not os.path.exists(DATA_BASE):
        df.loc[key] = data_dict[key]
        csv_data = df.to_csv()
        print('\nCSV String:\n', csv_data)

    else:
        df.loc[key] = data_dict[key]
        csv_data = df.to_csv()
        print('\nCSV String:\n', csv_data)

def get_bushes(key):
    return df.loc[key]['Bushes_locations']
def get_mines(key):
    return df.loc[key]['Mines_locations']
def get_row(key):
    return df.loc[key]['Solider_location'][0]
def get_col(key):
    return df.loc[key]['Solider_location'][1]
"""



init_Database(file_name)

# writing to csv file
def create_file(file_name):
    with open(file_name, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the cols
        csvwriter.writerow(cols)

        # writing the data rows
        csvwriter.writerows(rows)

# read the file
def file_reader(file_name):
    with open(file_name, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        cols = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
"""