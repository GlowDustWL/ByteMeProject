# import statements
import pygame
from sys import exit
import button
from jeopardy_board import jeopardyBoard

# initialize pygame
pygame.init()

# declare variables
width = 1600
height = 900

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wheel of Jeopardy")
clock = pygame.time.Clock()

# surfaces
background_menu = pygame.image.load('images/space_background.jpg').convert()
background_menu = pygame.transform.scale(background_menu, (width, height))
background_play = pygame.image.load('images/space_background.jpg').convert()
background_play = pygame.transform.scale(background_menu, (width, height))
background_options = pygame.image.load('images/space_background.jpg').convert()
background_options = pygame.transform.scale(background_menu, (width, height))

# Initializing Color
white = (255, 255, 255)


# main menu
def mainMenu():
    while True:

        # draw elements

        screen.blit(background_menu, (0, 0))
        start_button = button.Button("START", width/2, height/2)
        options_button = button.Button("OPTIONS", width/2, height/2 + 50)
        start_button.draw(screen)
        options_button.draw(screen)

        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if start_button.clicked:
                playScreen()
            if options_button.clicked:
                optionsScreen()

        # update the game state
        pygame.display.update()
        clock.tick(60)


def playScreen():
    loop = True
    while loop:

        # draw elements

        screen.blit(background_play, (0, 0))
        back_button = button.Button("BACK", width/16, height - 50)
        back_button.draw(screen)

        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if back_button.clicked:
                # mainMenu()
                loop = False
        # Drawing Jeopardy Board and rectangles
        jeopardyBoard()
    
        # update the game state
        pygame.display.update()
        clock.tick(60)


def optionsScreen():
    loop = True
    while loop:

        # draw elements
        screen.blit(background_options, (0, 0))
        back_button = button.Button("BACK", width/16, height - 50)
        back_button.draw(screen)

        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if back_button.clicked:
                # mainMenu()
                loop = False

        # update the game state
        pygame.display.update()
        clock.tick(60)

        # Drawing Rectangle
        pygame.draw.rect(background_options, white,
                         pygame.Rect(700, 225, 200, 400),  2, 3)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


mainMenu()
