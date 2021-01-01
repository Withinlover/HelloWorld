import pygame
from ..components import info
from .. import  constants as C

class LoadScreen:
    def __init__(self):
        self.finished = False
        self.next = 'SinglePlayer'
        self.timer = 0
        self.info = info.Info('LoadScreen')

    def update(self, surface, keys):
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
            if C.mode[3] == 0:
                self.next = 'SinglePlayer'
            elif C.mode[3] == 1:
                self.next = 'MultiPlayer'
            elif C.mode[3] == 2:
                self.next = 'Auto'
            elif C.mode[3] == 3:
                self.next = 'ManAI'


        elif pygame.time.get_ticks() - self.timer > 2000:
            self.finished = True
            self.timer = 0

        self.draw(surface)


    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.info.update()
        self.info.draw(surface)