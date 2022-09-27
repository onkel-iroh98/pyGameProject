import pygame
from settings import *
import time

class Textbox(pygame.Surface): #vllt gibts noch bessere Erbung
    def __init__(self, text):
        super().__init__((GAME_WIDTH, TEXTBOX_HEIGHT))
        self.fill((38, 81, 100))
        self.text = text
        self.charCount = len(self.text)
        self.charinRow = 65

        self.iterator = 1
        self.startTime = time.time()
        self.displayText_1 = self.text[0]
        self.displayText_2 = ""
        self.font = pygame.font.SysFont(None, 30)
        self.text_sur_1 = self.font.render(self.displayText_1, True, "WHITE")
        self.text_sur_2 = None
        self.textprinted = False




        self.rowOffset = 20

    def run(self):
        self.update()
        self.draw()

    def update(self):
        if time.time() - self.startTime >= 0.01 and self.textprinted == False:
            self.startTime = time.time()
            if self.iterator <= self.charinRow:
                self.displayText_1 += self.text[self.iterator]
                self.text_sur_1 = self.font.render(self.displayText_1, True, "WHITE")
            if self.iterator > self.charinRow:
                self.displayText_2 += self.text[self.iterator]
                self.text_sur_2 = self.font.render(self.displayText_2, True, "WHITE")
            self.iterator += 1
            if self.iterator == self.charCount:
                self.textprinted = True

    def draw(self):
        self.blit(self.text_sur_1, (0,self.rowOffset*1))
        if self.text_sur_2 != None:
            self.blit(self.text_sur_2, (0, self.rowOffset*3))







