import pygame
from settings import *

class Pokemon():
    def __init__(self, pokemon, lvl, sex, kp, attack, defense, specialattack, specialdefense, initiative, exp, moves):
        #reicht erst mal für den construktor später vllt noch wesen, evs, ivs, legendär?, shiny?,
        self.level = lvl
        self.kp = kp
        self.exp = exp
        self.moves = moves
        self.name = pokemon
        self.sex = sex
        self.image = pygame.image.load("graphics/Pokemon Sprites/Normal/normal_"+self.name+".png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (160, 160))