import pygame


class Handler:
    def __init__(self):
        pass

    def handle(self, input):
        self.update(input)
        self.render()

    def update(self, input):
        pass

    def render(self):
        pass
