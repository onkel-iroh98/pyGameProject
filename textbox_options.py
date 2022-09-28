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
            self.optionsWidth = GAME_WIDTH/3
            self.optionsSur = pygame.Surface((self.optionsWidth, TEXTBOX_HEIGHT))
            self.optionsSur.fill((38, 81, 100))
            self.locs = [(0 + 20, 10), (self.optionsWidth / 2 + 20, 10), (0 + 20, TEXTBOX_HEIGHT / 2 + 10),
                         (self.optionsWidth / 2 + 20, TEXTBOX_HEIGHT / 2 + 10)]
            self.createOptionSur()



        if self.optionBool==False:


            self.selection = pygame.Surface((5, 5))
            self.selection.fill("White")
            self.selectionCurrentPosition = 0

    def run(self):

        sel = self.update()
        if sel != None:
            return sel
        self.draw()
    def draw(self):
        Textbox.draw(self)
        self.blit(self.optionsSur, (GAME_WIDTH / 3 * 2, 0))


    def update(self):
        Textbox.update(self)

        keys = pygame.key.get_pressed()
        if self.selectionCurrentPosition == 0:
            if (keys[pygame.K_RIGHT]):
                self.selectionCurrentPosition = 1
                self.createOptionSur()
                self.optionsSur.blit(self.selection, (self.locs[self.selectionCurrentPosition][0], self.locs[self.selectionCurrentPosition][1]+5))
            if (keys[pygame.K_DOWN]):
                self.selectionCurrentPosition = 2
                self.createOptionSur()
                self.optionsSur.blit(self.selection, (self.locs[self.selectionCurrentPosition][0], self.locs[self.selectionCurrentPosition][1]+5))
        if self.selectionCurrentPosition == 1:
            if (keys[pygame.K_LEFT]):
                self.selectionCurrentPosition = 0
                self.createOptionSur()
                self.optionsSur.blit(self.selection, (self.locs[self.selectionCurrentPosition][0], self.locs[self.selectionCurrentPosition][1]+5))
            if (keys[pygame.K_DOWN]):
                self.selectionCurrentPosition = 3
                self.createOptionSur()
                self.optionsSur.blit(self.selection, (self.locs[self.selectionCurrentPosition][0], self.locs[self.selectionCurrentPosition][1]+5))
        if self.selectionCurrentPosition == 2:
            if (keys[pygame.K_RIGHT]):
                self.selectionCurrentPosition = 3
                self.createOptionSur()
                self.optionsSur.blit(self.selection, (self.locs[self.selectionCurrentPosition][0], self.locs[self.selectionCurrentPosition][1]+5))
            if (keys[pygame.K_UP]):
                self.selectionCurrentPosition = 0
                self.createOptionSur()
                self.optionsSur.blit(self.selection, (self.locs[self.selectionCurrentPosition][0], self.locs[self.selectionCurrentPosition][1]+5))
        if self.selectionCurrentPosition == 3:
            if (keys[pygame.K_LEFT]):
                self.selectionCurrentPosition = 2
                self.createOptionSur()
                self.optionsSur.blit(self.selection, (self.locs[self.selectionCurrentPosition][0], self.locs[self.selectionCurrentPosition][1]+5))
            if (keys[pygame.K_UP]):
                self.selectionCurrentPosition = 1
                self.createOptionSur()
                self.optionsSur.blit(self.selection, (self.locs[self.selectionCurrentPosition][0], self.locs[self.selectionCurrentPosition][1]+5))
        if keys[pygame.K_SPACE]:
            return self.selectionCurrentPosition

    def createOptionSur(self):
        self.optionsSur.fill((38, 81, 100))
        for option in range(self.optionsCount):
            tmp = self.font.render(self.options[option], None, "White")

            self.optionsSur.blit(tmp, (self.locs[option][0] + 20, self.locs[option][1]))


