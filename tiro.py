#!/usr/bin/env python

import pygame,glob
from pygame import *

class Tiro:
    '''
    Classe que gerencia os tiros da nave do jogador.
    '''

    def __init__(self, game, player):
        self.player = player
        self.screen = game.screen
        self.ani = glob.glob("recursos/player/tiros/tiro-1*.png")
        self.ani.sort()
        self.img = pygame.image.load(self.ani[0])
        self.speed_init = 2
        self.speed = self.speed_init
        self.ani_pos = 0
        self.ani_pos_max = len(self.ani)-1
        self.ani_speed_init = 20
        self.ani_speed = self.ani_speed_init
        self.x = self.player.x+(self.player.img.get_width()/2) - (self.img.get_width()/2)
        self.y = self.player.y - (self.player.img.get_height()/2)
        self.update()


    def update(self):
        self.ani_speed -= 1
        if self.ani_speed == 0:
            self.img = pygame.image.load(self.ani[self.ani_pos]).convert()
            self.ani_speed = self.ani_speed_init
            if self.ani_pos == self.ani_pos_max:
                self.ani_pos = 0
            else:
                self.ani_pos += 1
        self.speed -= 1
        if self.speed == 0:
            self.y -= 1
            self.speed = self.speed_init
        self.screen.blit(self.img, (self.x, self.y))
