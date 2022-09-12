import pygame

from level import Level

class Handler:
    def __init__(self):
        self.level = Level()

    def handle(self):
        self.run()

    def run(self):
        self.level.run()


