import pygame
from random import choice
from settings import *
from debug import debug
from tile import Tile
from player import Player
from support import *

class Level:
    def __init__(self):
        #ref auf Display Surface
        self.display_surface = pygame.display.get_surface()
        #sprites
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()


        ###
        self.create_map()

    def create_map(self):
        layouts = {
            "boundary": import_csv_layout("levels/001/_coll.csv"),
            #"floor": import_csv_layout("levels/000/_boden.csv"),
            "bridge": import_csv_layout("levels/000/_bridge.csv"),
            "tower": import_csv_layout("levels/000/_burg.csv"),
            "bush": import_csv_layout("levels/000/_bush.csv"),
            "flower": import_csv_layout("levels/000/_flowers.csv"),
            "water": import_csv_layout("levels/000/_wasser.csv"),

        }
        graphics = {
            "flower": import_folder("graphics/tiles/flower")
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == "boundary":
                            Tile((x, y), [self.obstacle_sprites], "invisible")
                        #if style == "flower":
                        #    random_flower_image = choice(graphics["flower"])
                        #    Tile((x,y), [self.visible_sprites], "flower", random_flower_image)
                        """KOMMENTAR NICHT LÖSCHEN
                           TEILE DAVON IN "TILE" wenn ein object größer als 64x64 (oder was eingetragen ist als Tilesize) muss es einen offset geben
                        if style == "object":
                            surf = graphics["objects][int(col)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], "object", surf)
                        """
        self.player = Player((780, 40), [self.visible_sprites], self.obstacle_sprites)
    def run(self):
        self.draw()
    def draw(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] //2
        self.offset = pygame.math.Vector2()

        #creating the floor
        self.floor_surf = pygame.image.load("levels/001/Map.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0,0))
    def custom_draw(self, player):
        #getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)


        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery): #sorted dafür das spieler nicht hinter tiles ist
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)