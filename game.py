#!/usr/bin/env python

import pygame, sys, glob
from pygame import *



WINDOW_HEIGHT, WINDOW_WIDTH = 800, 600
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH), FULLSCREEN)
pygame.init()
pygame.mouse.set_visible(False)
sound = pygame.mixer.Sound('music/musica.wav')


class Player:
    def __init__(self):
        sound.play()
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
        self.img = pygame.image.load(self.ani[self.direcao][self.ani_pos])
        self.x = (WINDOW_HEIGHT/2)-self.img.get_height()/2
        self.y = WINDOW_WIDTH-self.img.get_width()
        self.update()



    # Método que atualiza a nave frame a frame
    def update(self):
        self.ani_speed -= 1
        if self.ani_speed == 0:
            self.img = pygame.image.load(self.ani[self.direcao][self.ani_pos])
            self.ani_speed = self.ani_speed_init
            if self.ani_pos == self.ani_max:
                self.ani_pos = 0
            else:
                self.ani_pos += 1

        if self.movimento["up"]:
            if self.y > 0:
                self.y -= self.speed

        if self.movimento["down"]:
            if self.y < WINDOW_WIDTH-self.img.get_width():
                self.y += self.speed

        if self.movimento["left"]:
            self.direcao = "left"
            if self.x > 0:
                self.x -= self.speed

        if self.movimento["right"]:
            self.direcao = "right"
            if self.x < WINDOW_HEIGHT - self.img.get_height():
                self.x += self.speed

        screen.blit(self.img, (self.x, self.y))

    def dano(self):
        pass

    def get_rect(self):
        pass

player = Player()

class Interface:
    def __init__(self):
        self.font = pygame.font.Font("recursos/font.ttf", 35)

    def update(self):
        #texto = "Aperte ESC para sair!"
        #mesg = self.font.render(texto, 1, (255, 0, 0))
        #screen.blit(mesg, (WINDOW_WIDTH/2.5, WINDOW_HEIGHT/2.5))
        pass

interface = Interface()

while True:
    screen.fill((0,0,0))
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
    interface.update()
    player.update()
    pygame.display.update()