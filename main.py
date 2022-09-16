import pygame, sys
import time

from settings import *
from debug import *
from handler import Handler


"""
englische variablennamen
kommentare deutsch
scriptnamen klein
"""
#englische Variablennamen
#kommentare deutsch


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))#self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) for Fullscreen
        pygame.display.set_caption("Nils Nicklas Game")
        self.clock = pygame.time.Clock()
        ########################################################
        self.handler = Handler() #so gut wie alles hier rüber
        ########################################################


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")
            ############################################################
            self.handler.handle() #LOGIK

            ############################################################
            pygame.display.update()
            self.clock.tick(FPS)


try:
    if __name__ == "__main__":
        game = Game()
        game.run()
except Exception as e:  #falls was schief läuft wird in der Konsole angezeigt dann schliest es sich, also damit man es lesen kann das sleep
    print(e)
    time.sleep(3)