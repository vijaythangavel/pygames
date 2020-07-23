import pygame, sys, os
from pygame.locals import *

red = (255, 0, 0)

catx = 10
caty = 10
screen = 0

def myquit():
    pygame.quit()
    sys.exit(0)

def check_inputs(events):
    global catx, caty, screen

    for event in events:
        if event.type == QUIT:
            myquit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                myquit()
            elif event.key == K_LEFT:
                catx -= 5
            elif event.key == K_RIGHT:
                catx += 5
            else:
                print(event.key)
        else:
            print('None')
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (catx if catx < 256 else 255, 255, 255), (catx, 50, 50, 10))

    pygame.display.update()

def main():
    global screen
    # Initialize pygame
    pygame.init()
    # Setup Window
    window  = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Slither.eat - The Snake Game')

    screen = pygame.display.get_surface()
    pygame.display.update()

    while True:
        check_inputs(pygame.event.get())

main()