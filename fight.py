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
        self.textbox.update()
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
        #wo der cursor aktuell steht
        if (keys[pygame.K_LEFT]):
            self.selectionCursor = self.textbox.fightinput(pygame.Vector2(-1, 0))
            print(self.selectionCursor)
        if (keys[pygame.K_RIGHT]):
            self.selectionCursor = self.textbox.fightinput(pygame.Vector2(1, 0))
            print(self.selectionCursor)
        if (keys[pygame.K_UP]):
            self.selectionCursor = self.textbox.fightinput(pygame.Vector2(0, 1))
            print(self.selectionCursor)
        if (keys[pygame.K_DOWN]):
            self.selectionCursor = self.textbox.fightinput(pygame.Vector2(0, -1))
            print(self.selectionCursor)


        if (keys[pygame.K_SPACE]) and self.selectionCursor == (1, 1):
            self.option_run()

