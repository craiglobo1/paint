import pygame
import time
import concurrent.futures as cf
from util.settings import *
from util.canvas import *
from util.toolbar import *


class Game:
    def __init__(self):
        pygame.font.init()
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Paint")
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # create a sprite group for all sprites
        self.all_sprites = pygame.sprite.Group()

        # create canvas
        self.canvas = Canvas(20, 20, 200, 200)
        self.all_sprites.add(self.canvas)

        # create toolbar
        self.toolbar = Toolbar(
            (SIZE[0]*0.03, SIZE[1]*0.1), [BLUE, RED, GREEN])
        self.all_sprites.add(self.toolbar)

        self.run()

    def events(self):
        keysPressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            # zooming using the scroll wheel
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 4:
                    self.canvas.scale(20)
                if event.button == 5:
                    self.canvas.scale(-20)

        # Do action on the left click
        if pygame.mouse.get_pressed()[0]:
            mousePos = pygame.mouse.get_pos()
            if self.canvas.isInCanvas(mousePos):
                self.canvas.pencil(mousePos)

    def update(self):

        # Update all sprites
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)

        self.toolbar.draw()
        pygame.display.flip()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
pygame.quit()
