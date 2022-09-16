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
        self.visible_tiles = YSortCameraGroup()
        self.obstacle_tiles = pygame.sprite.Group()
        self.player_sprite = YSortCameraGroup() #Das hier ist die Lösung damit der Spieler nie hinter den Sprites ist


        ###
        self.create_map()

    def create_map(self):
        layouts = {
            "boundary": import_csv_layout("levels/001/_coll.csv"),
            #"floor": import_csv_layout("levels/000/_boden.csv"),
            "ground": import_csv_layout("levels/001/_ground.csv"),

            "tree": import_csv_layout("levels/001/_trees.csv"),
            "object": import_csv_layout("levels/001/_objects.csv")


        }
        graphics = {
            "biomeGraphics": import_folder("graphics/tiles/biomes")
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == "boundary":
                            Tile((x, y), [self.obstacle_tiles], "invisible")
                        if style == "ground":
                            tmp_tile = graphics["biomeGraphics"][int(col)]
                            Tile((x,y), [self.visible_tiles], "",tmp_tile)
                        if style == "tree":
                            tmp_tile = graphics["biomeGraphics"][int(col)]
                            Tile((x, y), [self.visible_tiles], "", tmp_tile)
                        if style == "object":

                            tmp_tile = graphics["biomeGraphics"][int(col)]
                            Tile((x, y), [self.visible_tiles], "", tmp_tile)
                        #if style == "flower":
                        #    random_flower_image = choice(graphics["flower"])
                        #    Tile((x,y), [self.visible_tiles], "flower", random_flower_image)
                        """KOMMENTAR NICHT LÖSCHEN
                           TEILE DAVON IN "TILE" wenn ein object größer als 64x64 (oder was eingetragen ist als Tilesize) muss es einen offset geben
                        if style == "object":
                            surf = graphics["objects][int(col)]
                            Tile((x,y), [self.visible_tiles, self.obstacle_tiles], "object", surf)
                        """
        self.player = Player((780, 40), [self.player_sprite],  self.obstacle_tiles)
    def run(self):
        self.draw()
    def draw(self):
        self.visible_tiles.custom_draw(self.player)
        self.visible_tiles.update()

        self.player_sprite.custom_draw(self.player)   #Das hier ist die Lösung damit der Spieler nie hinter den Sprites ist
        self.player_sprite.update()                   #Das hier ist die Lösung damit der Spieler nie hinter den Sprites ist

        debug((self.player.status))



class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] //2
        self.offset = pygame.math.Vector2()

        #creating the floor
        #self.floor_surf = pygame.image.load("levels/001/Map.png").convert()
        #self.floor_rect = self.floor_surf.get_rect(topleft=(0,0))
    def custom_draw(self, player):
        #getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #drawing the floor
        #floor_offset_pos = self.floor_rect.topleft - self.offset
        #self.display_surface.blit(self.floor_surf, floor_offset_pos)


        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery): #sorted dafür das spieler nicht hinter tiles ist
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

