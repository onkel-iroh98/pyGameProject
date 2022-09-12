import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):

        super().__init__(groups)
        self.image = pygame.image.load("graphics/test.png").convert_alpha()#arvorinha
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)  # mit -10 wird zB. auf beiden Seiten -5