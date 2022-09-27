import pygame
from settings import *

from textbox import Textbox
from textbox_options import Textbox_options

class Fight():
    def __init__(self, handler, trainer, pokemon):
        self.handler = handler
        self.display_surface = pygame.display.get_surface()

        self.pokemon = pokemon  #Class Pokemon Array oder nicht
        self.trainer = trainer #Bool

        self.textbox = Textbox_options("Ein Wilder Hurensohn.  Was willst du tun", ["Kampf", "Beutel", "Pokemon", "Flucht"])

    def run(self):
        self.input()
        self.textbox.run()
        self.draw()


    def draw(self):
        self.display_surface.blit(self.textbox, (0,GAME_HEIGHT-TEXTBOX_HEIGHT))
    def menu(self):
        pass
    def option_fight(self):
        pass
    def option_run(self):
        self.handler.wonFight()
    def option_bag(self):
        pass
    def option_pkmn(self):
        pass

    def input(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_SPACE]):
            self.option_run()

