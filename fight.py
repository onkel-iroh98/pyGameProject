import pygame
from settings import *

from textbox import Textbox

class Fight():
    def __init__(self, handler, trainer, pokemon):
        self.handler = handler
        self.display_surface = pygame.display.get_surface()

        self.pokemon = pokemon  #Class Pokemon Array oder nicht
        self.trainer = trainer #Bool

        self.textbox = Textbox(True)

    def run(self):
        self.input()
        self.handleTextbox()
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
        keys = pygame.key.get_pressed()#das hier noch über menu
        if (keys[pygame.K_SPACE]):
            self.option_run()
    def handleTextbox(self):
        font = pygame.font.SysFont(None, 30)
        img = font.render('FIGHT against ' + self.pokemon, True, "WHITE")
        lala = font.render("Space to escape", True, "WHite")
        self.textbox.blit(img, (10, 20))
        self.textbox.blit(lala, (10, 70))
