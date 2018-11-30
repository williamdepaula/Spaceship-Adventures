#!/usr/bin/env python

import pygame, glob, random
from pygame import *

class Asteroid:
    '''
    Classe que cuida das animações dos asteroids
    '''

    def __init__(self, game, x=0, y=0):
        self.screen = game.screen
        self.WINDOW = game.WINDOW
        self.speed_init = random.randint(1, 20)
        self.speed = self.speed_init
        self.life = 1
        self.ani_imgs = {
            'normal-1': glob.glob("recursos/asteroids/a1*.png"),
            'normal-2': glob.glob("recursos/asteroids/c1*.png"),
            'normal-3': glob.glob("recursos/asteroids/m1*.png"),
            'medio-1': glob.glob("recursos/asteroids/m4*.png"),
            'medio-2': glob.glob("recursos/asteroids/m5*.png"),
            'duro-1': glob.glob("recursos/asteroids/m3*.png"),
        }

        # Escolhe um asteroide aleatoriamente e define a vida dele.
        index = random.randint(0, 100)
        if index < 25:
            self.ani = self.ani_imgs['normal-1']
            self.life = 1
        elif index < 50:
            self.ani = self.ani_imgs['normal-2']
            self.life = 1
        elif index < 75:
            self.ani = self.ani_imgs['normal-3']
            self.life = 1
        elif index < 85:
            self.ani = self.ani_imgs['medio-1']
            self.life = 2
        elif index < 95:
            self.ani = self.ani_imgs['medio-2']
            self.life = 2
        else:
            self.ani = self.ani_imgs['duro-1']
            self.life = 3


        # Define aleatoriamente a rotação para direita ou esquerda
        self.ani.sort(reverse=True) if random.choice([True, False]) else self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani)-1
        self.ani_speed_init = random.randint(50, 300)
        self.ani_speed = self.ani_speed_init
        self.img = pygame.image.load(self.ani[self.ani_pos]).convert_alpha()
        self.x = x
        self.y = y
        self.update()



    def update(self):
        self.ani_speed -= 1
        if self.ani_speed == 0:
            self.img = pygame.image.load(self.ani[self.ani_pos]).convert_alpha()
            self.ani_speed = self.ani_speed_init
            if self.ani_pos == self.ani_max:
                self.ani_pos = 0
            else:
                self.ani_pos += 1

        self.speed -= 1
        if self.speed == 0:
            self.y += 1
            self.speed = self.speed_init

        self.screen.blit(self.img, (self.x, self.y))

    def destroy(self):
        del self
