import pygame
from settings import *

class Fight_ui(pygame.Surface):
    def __init__(self, pokemon_name):
        self.width = GAME_WIDTH/8*2.5
        self.height = GAME_HEIGHT/8
        self.pokemon = pokemon_name
        super().__init__((self.width, self.height))
        self.fill("white")
        #pokemon Name
        self.font = pygame.font.SysFont(None, 30)
        self.pkmn_name_sur = self.font.render(self.pokemon, True, "BLACK")
        self.blit(self.pkmn_name_sur, (0,0))





