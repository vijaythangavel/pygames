import pygame, sys, os
from pygame.locals import *

red = (255, 0, 0)

#Initalize Pygame
pygame.init()

#Setup Window
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Slither.eat - The Snake Game')

screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption('Snake')
pygame.display.flip()

# count = 0
while True:
    print('Slither.eat - The Snake GAme')
    pass
