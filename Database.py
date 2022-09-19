import pygame
import pandas as pd
import csv
import os
import json

DATA_BASE = 'dataBase.csv'

def key_press_timer(key):
    clock = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == key:
                return int(chr(key)), (pygame.time.get_ticks() - clock) // 1000

def create_data_dict(data_dict):
    return data_dict

def init_data_base():
    if not os.path.exists(DATA_BASE):
        df = pd.DataFrame()
        df.to_csv(DATA_BASE, columns=['num_button','Solider_location','Bushes_locations','Mines_locations'], mode='w')





cols = []
rows = []
dict_save = {}
file_name = "saved.csv"
# i need to check this
# df = pd.DataFrame.from_dict(dict_save)
# df.to_csv (r'saved.csv', index = False, header=True)

def init_Database(file_name):
    if os.path.exists(file_name):
        print("File exists") #should open it and add
        file_reader(file_name)
    else:
        print("File does not exist") #should create one
        """
        df = pd.DataFrame()
        df.columns = ['num_button', 'Solider_location', 'Bushes_locations', 'Mines_locations']
        csv_file= df.to_csv(file_name, mode='w')"""

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