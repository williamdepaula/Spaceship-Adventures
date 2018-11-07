#!/usr/bin/env python

import pygame, sys
from pygame import *



WINDOW_HEIGHT, WINDOW_WIDTH = 800, 600
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH), FULLSCREEN)
pygame.init()
pygame.mouse.set_visible(False)


class Player:
    def __init__(self):
        self.avatar = "recursos/player/nave.png"
        self.img = pygame.image.load(self.avatar)
        self.x, self.y = 0, 0
        self.update()

    # Método que atualiza a nave frame a frame
    def update(self):
        posX = (WINDOW_HEIGHT/2)-self.img.get_height()/2
        posY = WINDOW_WIDTH-self.img.get_width()
        screen.blit(self.img, (posX, posY))

    def dano(self):
        pass

    def get_rect(self):
        pass

player = Player()

class Interface:
    def __init__(self):
        self.font = pygame.font.Font("recursos/font.ttf", 35)

    def update(self):
        texto = "Aperte ESC para sair!"
        mesg = self.font.render(texto, 1, (255, 0, 0))
        screen.blit(mesg, (WINDOW_WIDTH/2.5, WINDOW_HEIGHT/2.5))
        pass

interface = Interface()

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    interface.update()
    player.update()
    pygame.display.update()