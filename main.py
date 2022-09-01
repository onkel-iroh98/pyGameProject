import time

import pygame, sys
from settings import *



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption("Nils Nicklas Game")
        self.clock = pygame.time.Clock()

        def run(self):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                pygame.display.update()
                self.clock.tick(FPS)
try:
    if __name__ == "__main__":
        time.sleep(5)
        game = Game()
        game.run()
except Exception as e:
    print(e)
    time.sleep(3)