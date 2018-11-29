#!/usr/bin/env python

import pygame, glob
from pygame import *

class Asteroid:
    '''
    Classe que cuida das animações dos asteroids
    '''

    def __init__(self, game):
        self.screen = game.screen
        self.WINDOW = game.WINDOW
        self.speed = 1
        self.ani = glob.glob("recursos/asteroids/a1000*.png")
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani)-1
        self.ani_speed_init = 200
        self.ani_speed = self.ani_speed_init
        # self.img = pygame.image.load("recursos/asteroids/a10000.png")
        self.img = pygame.image.load(self.ani[self.ani_pos])
        self.update()



    def update(self):
        self.ani_speed -= 1
        if self.ani_speed == 0:
            self.img = pygame.image.load(self.ani[self.ani_pos])
            self.ani_speed = self.ani_speed_init
            if self.ani_pos == self.ani_max:
                self.ani_pos = 0
            else:
                self.ani_pos += 1

        self.screen.blit(self.img, (10, 10))