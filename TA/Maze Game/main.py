import pygame
from random import choice

RES = WIDTH, HEIGHT = 1200, 900
TILE = 50
kolom, baris = WIDTH // TILE, HEIGHT // TILE

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('red'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
    clock.tick(30)
