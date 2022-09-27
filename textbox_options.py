import pygame
from settings import *
from textbox import Textbox
class Textbox_options(Textbox):
    def __init__(self, text, options):
        super().__init__(text)

        self.charinRow = 45
        self.options = options

        self.optionsCount = len(options)

        if self.optionsCount == 2:
            self.optionBool = True
            self.optionsSur = pygame.Surface((GAME_WIDTH/4, TEXTBOX_HEIGHT))
        elif self.optionsCount == 4:
            self.optionBool = False
            self.optionsSur = pygame.Surface((GAME_WIDTH/3, TEXTBOX_HEIGHT))


        self.optionCreateArray = []
        if self.optionBool==False:
            for option in range(self.optionsCount):
                self.optionCreateArray.append(self.font.render((option, None, "BLACK")))
            for x in range(len(self.optionCreateArray)):
                self.blit(x, (0,0))#hier alarm hier gehts weiter

    def run(self):

        self.update()
        self.draw()
    def draw(self):
        Textbox.draw(self)

    def update(self):
        Textbox.update(self)



##############################################################################################
    #ab hier überartbeiten
    """
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
    """