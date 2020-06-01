import pygame
from math import floor
from .settings import *


class Toolbar(pygame.sprite.Sprite):
    def __init__(self, position, colors):

        self.colors = colors
        self.width, self.height = SIZE[0]*0.1, SIZE[1]*0.8

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GREY)

        self.rect = self.image.get_rect()
        self.rect.topleft = position
        super().__init__()

    def draw(self):
        for i, color in enumerate(self.colors):
            columnNo = i % 2
            rowNo = int(floor(i / 2))

            boxSize = int(floor(self.width/2))

            box = pygame.Surface((boxSize, boxSize))
            box.fill(color)
            self.image.blit(box, (columnNo*(self.width//2),
                                  rowNo*(self.width//2)))
