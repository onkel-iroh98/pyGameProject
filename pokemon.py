import pygame
from settings import *
from support import *

class Pokemon():
    def __init__(self, front, pokemon, lvl, sex, kp, attack, defense, specialattack, specialdefense, initiative, exp, moves):
        #reicht erst mal für den construktor später vllt noch wesen, evs, ivs, legendär?, shiny?,
        #Logik
        self.front = front
        self.animated = True

        #Pokemon Attributes
        self.level = lvl
        self.kp = kp
        self.exp = exp
        self.moves = moves
        self.name = pokemon
        self.sex = sex


        if self.animated:
            if self.front:
                self.image = import_folder("graphics/Pokemon Sprites/front_anim/"+self.name)
                for img in range(len(self.image)):
                    self.image[img] = pygame.transform.scale(self.image[img], (self.image[img].get_size()[0]*2, self.image[img].get_size()[1]*2))
                    #self.image = pygame.transform.scale(self.image, (160, 160))
            if not self.front:
                self.image = import_folder("graphics/Pokemon Sprites/back_anim/" + self.name)
                for img in range(len(self.image)):
                    self.image[img] = pygame.transform.scale(self.image[img], (self.image[img].get_size()[0] * 2, self.image[img].get_size()[1] * 2))
                    # self.image = pygame.transform.scale(self.image, (160, 160))

