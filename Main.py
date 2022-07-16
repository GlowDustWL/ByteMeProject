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

# Initializing Color
white = (255, 255, 255)


# main menu
def mainMenu():
    while True:

        # draw elements

        screen.blit(background_1, (0, 0))
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
    while True:

        # draw elements

        screen.blit(background_1, (0, 0))
        back_button = button.Button("BACK", width/16, height - 50)
        back_button.draw(screen)

        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if back_button.clicked:
                mainMenu()

        # Drawing Rectangle
        pygame.draw.rect(background_1, white, pygame.Rect(
            50, 50, 600, 400),  2, 3)  # Wheel section
        pygame.draw.rect(background_1, white, pygame.Rect(
            950, 50, 600, 480),  2, 3)  # Jeopardy section
        pygame.draw.rect(background_1, white, pygame.Rect(
            680, 50, 240, 400),  2, 3)  # Player info section
        pygame.draw.rect(background_1, white, pygame.Rect(
            50, 480, 870, 50),  2, 3)  # status/ user promp
        pygame.draw.rect(background_1, white, pygame.Rect(
            50, 550, 870, 255),  2, 3)  # questions / answers
        pygame.draw.rect(background_1, white, pygame.Rect(
            950, 555, 50, 50),  2, 3)  # asnwer question button: A
        pygame.draw.rect(background_1, white, pygame.Rect(
            950, 620, 50, 50),  2, 3)  # asnwer question button: B
        pygame.draw.rect(background_1, white, pygame.Rect(
            950, 685, 50, 50),  2, 3)  # asnwer question button: C
        pygame.draw.rect(background_1, white, pygame.Rect(
            950, 750, 50, 50),  2, 3)  # asnwer question button: D
        pygame.draw.rect(background_1, white, pygame.Rect(
            1150, 652, 200, 50),  2, 3)  # Spin The Wheel !

        # update the game state
        pygame.display.update()
        clock.tick(60)


def optionsScreen():
    while True:

        # draw elements
        screen.blit(background_1, (0, 0))
        back_button = button.Button("BACK", width/16, height - 50)
        back_button.draw(screen)

        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if back_button.clicked:
                mainMenu()

        # update the game state
        pygame.display.update()
        clock.tick(60)

        # Drawing Rectangle
        pygame.draw.rect(background_1, white,
                         pygame.Rect(700, 225, 200, 400),  2, 3)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


mainMenu()
