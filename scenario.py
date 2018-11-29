#!/usr/bin/env python

import pygame, glob
from pygame import *
from asteroids import Asteroid

class Scenario:
    '''
    Classe com as informações de cenario do jogo.
    '''

    def __init__(self, game):
        self.screen = game.screen
        self.img = pygame.image.load("recursos/background.jpg").convert()
        self.asteroid = Asteroid(game)


    def update(self):
        self.screen.blit(self.img, (0, 0))
        self.asteroid.update()