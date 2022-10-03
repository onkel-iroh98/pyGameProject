import pygame
import time
from settings import *

from textbox import Textbox
from textbox_options import Textbox_options
from fight_ui import Fight_ui
from pokemon import Pokemon
from support import *

class Fight():
    def __init__(self, handler, trainer, pokemon):
        self.handler = handler
        self.display_surface = pygame.display.get_surface()
        self.time = time.time()

        self.trainer = trainer  # Bool

        self.enemy_pokemon = pokemon  #Class Pokemon Array oder nicht
        self.enemy_pokemon_frame = 0
        self.player_pokemon = Pokemon(False, randomPokemon(), 100, "male", 400, 50, 50,50,50,50,99999,None)
        self.player_pokemon_frame = 0

        self.background = pygame.image.load("graphics/0.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (GAME_WIDTH, GAME_HEIGHT-TEXTBOX_HEIGHT))


        self.textbox = Textbox_options("Ein wildes "+self.enemy_pokemon.name+" erscheint.  Was willst du tun", ["Kampf", "Beutel", "Pokemon", "Flucht"])
        self.enemyFightUi = Fight_ui(self.enemy_pokemon.name)
        self.playerFightUi = Fight_ui(self.player_pokemon.name)
        #self.playerFightUi = Fight_ui()



    def run(self):
        sel = self.textbox.run()
        if sel != None:
            self.input(sel)
        self.draw()


    def draw(self):
        #hintergrund
        self.display_surface.blit(self.background, (0, 0))
        #enemy pokemon
        self.animateEnemyPokemon()
        #player pokemon
        self.animatePlayerPokemon()
        #enemy UI
        self.display_surface.blit(self.enemyFightUi, (GAME_WIDTH/8*5,(GAME_HEIGHT-TEXTBOX_HEIGHT)/4*3))
        #player UI
        self.display_surface.blit(self.playerFightUi, (GAME_WIDTH / 8 * 1, (GAME_HEIGHT - TEXTBOX_HEIGHT) / 4 * 1))
        # textbox
        self.display_surface.blit(self.textbox, (0, GAME_HEIGHT - TEXTBOX_HEIGHT))
        #self.display_surface.blit(self.playerFightUi, (GAME_WIDTH/10, (GAME_HEIGHT-TEXTBOX_HEIGHT)/10))
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


    def animateEnemyPokemon(self):
        if not self.enemy_pokemon.animated:
            self.display_surface.blit(self.enemy_pokemon.image, (GAME_WIDTH/8*5, (GAME_HEIGHT-TEXTBOX_HEIGHT)/4))
        if time.time() - self.time > 0.05:
            self.time = time.time()
            self.enemy_pokemon_frame += 1
            self.player_pokemon_frame += 1
        if self.enemy_pokemon_frame >= len(self.enemy_pokemon.image)-1:
            self.enemy_pokemon_frame = 0
        if self.enemy_pokemon.animated:
            self.display_surface.blit(self.enemy_pokemon.image[self.enemy_pokemon_frame], (GAME_WIDTH/16*10, (GAME_HEIGHT-TEXTBOX_HEIGHT)/16*5))


    def animatePlayerPokemon(self):
        if not self.enemy_pokemon.animated:
            self.display_surface.blit(self.enemy_pokemon.image,
                                      (GAME_WIDTH / 8 * 5, (GAME_HEIGHT - TEXTBOX_HEIGHT) / 4))
        if time.time() - self.time > 0.05:
            self.time = time.time()
            self.enemy_pokemon_frame += 1
            self.player_pokemon_frame += 1
        if self.player_pokemon_frame >= len(self.enemy_pokemon.image)-1:
            self.player_pokemon_frame = 0
        if self.player_pokemon.animated:
            self.display_surface.blit(self.player_pokemon.image[self.player_pokemon_frame],
                                      (GAME_WIDTH / 16 * 2, (GAME_HEIGHT - TEXTBOX_HEIGHT - self.player_pokemon.image[self.player_pokemon_frame].get_height() + 50)))
