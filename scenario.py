#!/usr/bin/env python

import pygame, glob
from pygame import *

class Scenario:
    '''
    Classe com as informações de cenario do jogo.
    '''

    def __init__(self, game):
        self.screen = game.screen
        self.img = pygame.image.load("recursos/background.jpg")


    def update(self):
        self.screen.blit(self.img, (0, 0))