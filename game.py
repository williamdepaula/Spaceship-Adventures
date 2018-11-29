#!/usr/bin/env python

import pygame, sys, glob
from pygame import *
from player import Player


class Game:
    '''
    Classe que cuida de todas as informações para rodar o jogo
    '''
    def __init__(self):
        self.WINDOW = (800, 600)
        self.screen = pygame.display.set_mode(self.WINDOW, FULLSCREEN)
        pygame.init()
        pygame.mouse.set_visible(False)
        self.sound = pygame.mixer.Sound('music/musica.wav')
        self.sound.play()
        self.font = pygame.font.Font("recursos/font.ttf", 25)

    def update(self):
        vida = "Vida: X X X"
        mesg = self.font.render(vida, 1, (255,255,255))
        self.screen.blit(mesg, (10, 10))
        especial = "X X X : Especial"
        mesg = self.font.render(especial, 1, (255, 255, 255))
        self.screen.blit(mesg, (550, 10))

game = Game()
player = Player(game)


while True:
    game.screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
            if event.key == K_UP:
                player.movimento['up'] = True
            if event.key == K_DOWN:
                player.movimento['down'] = True
            if event.key == K_LEFT:
                player.movimento['left'] = True
            if event.key == K_RIGHT:
                player.movimento['right'] = True

        if event.type == KEYUP:
            if event.key == K_UP:
                player.movimento['up'] = False
            if event.key == K_DOWN:
                player.movimento['down'] = False
            if event.key == K_LEFT:
                player.movimento['left'] = False
                player.direcao = "up"
            if event.key == K_RIGHT:
                player.movimento['right'] = False
                player.direcao = "up"

    player.update()
    game.update()
    pygame.display.update()