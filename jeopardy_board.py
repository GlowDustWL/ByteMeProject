# Copied straight from Chris for test GUI setup

# import statements
import pygame
from sys import exit
import button

# initialize pygame
pygame.init()

# declare variables
width = 1600
height = 900

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wheel of Jeopardy")
clock = pygame.time.Clock()

# surfaces
background_1 = pygame.image.load('images/space_background.jpg').convert()
background_1 = pygame.transform.scale(background_1, (width, height))

# main menu


def mainMenu():
    while True:

        # draw elements
        screen.blit(background_1, (0, 0))
        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # update the game state
        pygame.display.update()
        clock.tick(60)

mainMenu()
