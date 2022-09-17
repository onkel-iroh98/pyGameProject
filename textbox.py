import pygame
from settings import *

class Textbox(pygame.Surface): #vllt gibts noch bessere Erbung
    def __init__(self, fighoptions = False, desition = False):
        super().__init__((GAME_WIDTH, TEXTBOX_HEIGHT))
        self.fill((38, 81, 100))
        self.fightoptions = fighoptions
        self.fightsur_width = int(GAME_WIDTH / 3)
        if self.fightoptions:
            self.locs = {
                "fight": (int(self.fightsur_width / 10), int(TEXTBOX_HEIGHT / 4)),
                "bag": (int(self.fightsur_width / 10 * 6), int(TEXTBOX_HEIGHT / 4)),
                "pkmn": (int(self.fightsur_width / 10), int(TEXTBOX_HEIGHT / 4 * 3)),
                "run": (int(self.fightsur_width / 10 * 6), int(TEXTBOX_HEIGHT / 4 * 3))
            }
            self.selection = "fight"
            self.blitFightOptions()



    def update(self):
        self.blitFightOptions()
        self.update_selectionCursor()
        self.draw()

    def draw(self):
        self.blit(self.fightsur, (GAME_WIDTH / 3 * 2, 0))
    def blitFightOptions(self):
        self.fightsur = pygame.Surface((self.fightsur_width, TEXTBOX_HEIGHT))
        self.fightsur.fill("white")
        t_fight = "KAMPF"
        t_bag = "BEUTEL"
        t_pkmn = "POKEMON"
        t_run = "FLUCHT"
        font = pygame.font.SysFont(None, 20)
        sur_fight = font.render(t_fight, True, "BLACK")
        sur_bag = font.render(t_bag, True, "BLACK")
        sur_pkmn = font.render(t_pkmn, True, "BLACK")
        sur_run = font.render(t_run, True, "BLACK")

        self.fightsur.blit(sur_fight, self.locs["fight"])
        self.fightsur.blit(sur_bag, self.locs["bag"])
        self.fightsur.blit(sur_pkmn, self.locs["pkmn"])
        self.fightsur.blit(sur_run, self.locs["run"])
    def update_selectionCursor(self):
        self.chooseCursor = pygame.Surface((10, 15))
        self.chooseCursor.fill("black")
        self.fightsur.blit(self.chooseCursor, ((self.locs[self.selection][0] - 20), self.locs[self.selection][1]))

    def fightinput(self, input):
        if self.selection == "fight":
            if input.x == 1:
                self.selection = "bag"
                return pygame.Vector2(1, 0)
            elif input.y == -1:
                self.selection = "pkmn"
                return pygame.Vector2(0, 1)
        elif self.selection == "bag":
            if input.x == -1:
                self.selection = "fight"
                return pygame.Vector2(0, 0)
            if input.y == -1:
                self.selection = "run"
                return pygame.Vector2(1, 1)
        elif self.selection == "pkmn":
            if input.x == 1:
                self.selection = "run"
                return pygame.Vector2(1, 1)
            if input.y == 1:
                self.selection="fight"
                return pygame.Vector2(0, 0)
        elif self.selection == "run":
            if input.x == -1:
                self.selection= "pkmn"
                return pygame.Vector2(0, 1)
            if input.y == 1:
                self.selection= "bag"
                return pygame.Vector2(1,0)
        if self.selection == "fight":
            return pygame.Vector2(0, 0)
        if self.selection == "bag":
            return pygame.Vector2(1, 0)
        if self.selection == "pkmn":
            return pygame.Vector2(0, 1)
        if self.selection == "run":
            return pygame.Vector2(1, 1)




