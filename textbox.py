import pygame
from settings import *

class Textbox(pygame.Surface): #vllt gibts noch bessere Erbung
    def __init__(self, fighoptions = False):
        super().__init__((GAME_WIDTH, TEXTBOX_HEIGHT))
        self.fill((38, 81, 100))
        self.fightoptions = fighoptions
        if self.fightoptions:
            fightsur_width = int(GAME_WIDTH/3)
            fightsur = pygame.Surface((fightsur_width, TEXTBOX_HEIGHT))
            fightsur.fill("white")
            chooseCursor = pygame.Surface((10, 15))
            chooseCursor.fill("black")

            t_fight = "KAMPF"
            t_bag = "BEUTEL"
            t_pkmn = "POKEMON"
            t_run = "FLUCHT"
            font = pygame.font.SysFont(None, 20)
            sur_fight = font.render(t_fight, True, "BLACK")
            sur_bag = font.render(t_bag, True, "BLACK")
            sur_pkmn = font.render(t_pkmn, True, "BLACK")
            sur_run = font.render(t_run, True, "BLACK")
            locs = {
                "fight": (int(fightsur_width/10), int(TEXTBOX_HEIGHT/4)),
                "bag": (int(fightsur_width/10*6), int(TEXTBOX_HEIGHT/4)),
                "pkmn": (int(fightsur_width/10), int(TEXTBOX_HEIGHT/4*3)),
                "run": (int(fightsur_width/10*6), int(TEXTBOX_HEIGHT/4*3))
            }
            fightsur.blit(sur_fight, locs["fight"])
            fightsur.blit(sur_bag, locs["bag"])
            fightsur.blit(sur_pkmn, locs["pkmn"])
            fightsur.blit(sur_run, locs["run"])
            fightsur.blit(chooseCursor, ((locs["fight"][0] - 20), locs["fight"][1]))
            self.blit(fightsur, (GAME_WIDTH/3*2, 0))




