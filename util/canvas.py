import pygame
import numpy as np
from PIL import Image
from .settings import *
import copy


class Canvas(pygame.sprite.Sprite):
    def __init__(self, x, y, height, width):

        self.brush = RED
        # initialize size
        self.size = self.height, self.width = height, width

        # initialize the array of valuea
        self.canvas = self.OldCanvas = np_array = np.full(
            (height, width, 3), [*WHITE]).astype(np.uint8)

        # save the image
        im = Image.fromarray(self.canvas)
        im.save("canvas.png")

        # create image and position it
        self.image = pygame.image.load('canvas.png').convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

        super().__init__()

    def scale(self, amount):
        if self.height + amount > 1 and self.width + amount > 1:
            self.height += amount
            self.width += amount
            self.image = pygame.transform.scale(
                pygame.image.load(
                    'canvas.png').convert(), (self.height, self.width))

            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def pencil(self, mousePos):
        # gets position relative to canvas
        position = mousePos[0] - self.rect.left, mousePos[1] - self.rect.top

        # get the position relative to the size of the canvas
        gap = self.width / self.size[0]
        x = int(position[1] // gap)
        y = int(position[0] // gap)

        # print(f'x:{x}   y:{y}')

        # assign click to the brush color
        self.canvas[x][y] = [*self.brush]

        # save the changes to img and resize the picture to previous size
        im = Image.fromarray(self.canvas)
        im.save("canvas.png")
        self.image = pygame.transform.scale(pygame.image.load(
            'canvas.png').convert(), (self.height, self.width))

    # is the position in the canvas
    def isInCanvas(self, pos):
        if pos[0] > self.rect.left and pos[0] < self.rect.right:
            if pos[1] > self.rect.top and pos[1] < self.rect.bottom:
                return True

        return False
