import pygame
from random import randint
from pokemon import Pokemon
from support import *
from settings import *

class WildPokemon_Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, handler, player, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -1)

        self.handler = handler
        self.player = player
        self.can_encounter = True
        self.noTrainer = False

    def collision(self):
        if self.hitbox.colliderect(self.player.hitbox):
            if self.can_encounter:
                encounter = randint(0,19)     #5% chance auf WildesPokemon
                if encounter == 0:            #5% chance auf WildesPokemon
                    pokemon = Pokemon(True, randomPokemon(), 100, "male", 400, 50, 50,50,50,50,99999,None)
                    self.handler.triggerFight(self.noTrainer, pokemon)
                    self.can_encounter = False
                else:
                    self.can_encounter = False

        else:
            self.can_encounter = True
    def update(self):
        self.collision()
