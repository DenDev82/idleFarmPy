import pygame
import os
import time
import math
import random

pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
running = True
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
#Asset load
nebo = pygame.image.load("nebo.png")
oblak = pygame.image.load("oblak.png")
trava = pygame.image.load("trava.png")
baza_f = pygame.image.load("slamna3_nasa.png")
baza_e = pygame.transform.flip(baza_f,1,0)
#Cloud Variables
i = -128
j = -128
k = random.randint(-256,-128)
#Tile mapping
TILE_SIZE = 64
def crtanje():
    global i,j,k
    screen.blit(nebo, (0,0))
    i+=random.uniform(2,3)
    j+=random.uniform(1,2)
    k+=random.uniform(1.5,2.4)
    if i>640+oblak.get_width():
        i = -128
    if j>640+oblak.get_width():
        j = -128
    if k>640+oblak.get_width():
        k = random.randint(-256,-128)
    pos_tiles = SCREEN_WIDTH//TILE_SIZE
    for tile in range(0,pos_tiles):
        screen.blit(trava,(tile*TILE_SIZE,SCREEN_HEIGHT-TILE_SIZE))
    screen.blit(oblak, (i,32))
    screen.blit(oblak, (j,96))
    screen.blit(oblak, (k,160))
    screen.blit(baza_f, (0, SCREEN_HEIGHT-TILE_SIZE*4))
    screen.blit(baza_e, (SCREEN_WIDTH-TILE_SIZE*2, SCREEN_HEIGHT-TILE_SIZE*4))
    # screen.blit(oblak, (i+random.randint(100,200), random.randint(64,100)))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    crtanje()

    pygame.display.flip()
    clock.tick(60)
