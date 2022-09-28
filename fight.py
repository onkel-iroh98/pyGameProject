import pygame
from settings import *

from textbox import Textbox
from textbox_options import Textbox_options

class Fight():
    def __init__(self, handler, trainer, pokemon):
        self.handler = handler
        self.display_surface = pygame.display.get_surface()

        self.pokemon = pokemon  #Class Pokemon Array oder nicht
        self.trainer = trainer  #Bool

        self.background = pygame.image.load("graphics/0.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (GAME_WIDTH, GAME_HEIGHT-TEXTBOX_HEIGHT))


        self.textbox = Textbox_options("Ein Wilder Hurensohn.  Was willst du tun", ["Kampf", "Beutel", "Pokemon", "Flucht"])

    def run(self):
        sel = self.textbox.run()
        if sel != None:
            self.input(sel)
        self.draw()


    def draw(self):
        self.display_surface.blit(self.background, (0, 0))
        self.display_surface.blit(self.textbox, (0, GAME_HEIGHT-TEXTBOX_HEIGHT))
    def menu(self):
        pass
    def option_fight(self):
        print("Auswahl Fight")
    def option_run(self):
        self.handler.wonFight()
    def option_bag(self):
        print("Auswahl Beutel")
    def option_pkmn(self):
        print("Auswahl Pokemon")

    def input(self, sel):
        if sel == 0:
            self.option_fight()
        if sel == 1:
            self.option_bag()
        if sel == 2:
            self.option_pkmn()
        if sel == 3:
            self.option_run()


