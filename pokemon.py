import pygame
from settings import *

class Pokemon():
    def __init__(self, pokemon, lvl, kp, attack, defense, specialattack, specialdefense, initiative, exp, moves):
        #reicht erst mal für den construktor später vllt noch wesen evs und ivs
        self.level = lvl
        self.kp = kp
        self.exp = exp
        self.moves = moves
        self.name = pokemon
        self.image =