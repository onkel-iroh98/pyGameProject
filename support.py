from csv import reader
from os import walk
from random import randint
from csv import DictReader
import pygame


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter= ",")
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder_tutorial(path):
    surface_list = []
    for _,__,img_files in walk(path):   #die ersten beiden um an die datei zu kommen
        for img in img_files:
            full_path = path + "/" + img
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)

    return surface_list
def import_folder(path):
    surface_list = []
    iter = 0
    for _,__,x in walk(path):
        for img in x:
            full_path = path +"/" + str(iter) + ".png"
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)
            iter += 1
    return surface_list
def randomPokemon():
    path = "graphics/Pokemon Sprites/Pokemon.csv"
    rand=randint(1,649)
    with open(path, newline='') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            if int(row["ID"]) == rand:
                return row['Name'].lower()
