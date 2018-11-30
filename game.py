#!/usr/bin/env python

import pygame, sys, glob, random
from pygame import *
from player import Player
from scenario import Scenario
from asteroids import Asteroid
from tiro import Tiro


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
        self.volume = 0
        self.sound.set_volume(self.volume)
        self.sound.play(-1)
        self.font = pygame.font.Font("recursos/font.ttf", 25)
        self.asteroids = []
        self.tiros = []
        self.dif_faze = 10000

    def enemies(self):
        if self.dif_faze > 1000:
            self.dif_faze -= 1
        if random.randint(0, self.dif_faze) <= 1:
            self.asteroids.append(Asteroid(self, random.randint(0, 800), -20))

    def update(self):
        if self.volume < 1.0:
            self.volume += 0.0002
            self.sound.set_volume(self.volume)
        for enem in self.asteroids:
            enem.update()

        for tiro in self.tiros:
            tiro.update()
        vida = "Vida: X X X "
        mesg = self.font.render(vida, 1, (255,255,255))
        self.screen.blit(mesg, (10, 10))
        especial = "X X X : Especial"
        mesg = self.font.render(especial, 1, (255, 255, 255))
        self.screen.blit(mesg, (560, 10))
        self.enemies()



game = Game()
scenario = Scenario(game)
player = Player(game)
asteroids = []
tiros = []


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
            if event.key == K_SPACE:
                game.tiros.append(Tiro(game, player))

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

    scenario.update()
    player.update()
    game.update()
    pygame.display.update()