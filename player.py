#!/usr/bin/env python

import pygame, glob
from pygame import *

class Player:
    def __init__(self, game):
        self.screen = game.screen
        self.WINDOW = game.WINDOW

        self.movimento = {
            'up': False,
            'down': False,
            'left': False,
            'right': False,
        }

        self.ani = {
            'up': glob.glob("recursos/player/nave-up-*.png"),
            'left': glob.glob("recursos/player/nave-left-*.png"),
            'right': glob.glob("recursos/player/nave-right-*.png"),
        }
        self.direcao = "up"

        self.ani["up"].sort()
        self.ani["left"].sort()
        self.ani["right"].sort()
        self.speed = 1
        self.ani_pos = 0
        self.ani_max = len(self.ani[self.direcao])-1
        self.ani_speed_init = 50
        self.ani_speed = self.ani_speed_init
        self.img = pygame.image.load(self.ani[self.direcao][self.ani_pos]).convert()
        self.x = (self.WINDOW[0]/2)-self.img.get_height()/2
        self.y = self.WINDOW[1]-self.img.get_width()
        self.update()



    # Método que atualiza a nave frame a frame
    def update(self):
        self.ani_speed -= 1
        if self.ani_speed == 0:
            self.img = pygame.image.load(self.ani[self.direcao][self.ani_pos]).convert()
            self.ani_speed = self.ani_speed_init
            if self.ani_pos == self.ani_max:
                self.ani_pos = 0
            else:
                self.ani_pos += 1

        if self.movimento["up"]:
            if self.y > 0:
                self.y -= self.speed

        if self.movimento["down"]:
            if self.y < self.WINDOW[1]-self.img.get_width():
                self.y += self.speed

        if self.movimento["left"]:
            self.direcao = "left"
            if self.x > 0:
                self.x -= self.speed

        if self.movimento["right"]:
            self.direcao = "right"
            if self.x < self.WINDOW[0] - self.img.get_height():
                self.x += self.speed

        self.screen.blit(self.img, (self.x, self.y))

    def dano(self):
        pass

    def get_rect(self):
        pass