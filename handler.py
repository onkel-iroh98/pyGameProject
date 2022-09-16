import pygame

from level import Level
from fight import Fight

class Handler:
    def __init__(self):
        self.level = Level(self)
        self.fight = None
        self.fighting = False

    def handle(self):   #StartSceen zB. hier händeln
        self.run()

    def run(self):
        if self.fighting:
            self.fight.run()
        else:
            self.level.run()


    def triggerFight(self, trainer, pokemon):
        self.fighting = True
        self.fight = Fight(self, trainer, pokemon)
    def wonFight(self):
        self.fight = None
        self.fighting = False
