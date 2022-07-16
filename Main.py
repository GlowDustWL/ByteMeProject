# import statements
import pygame
from sys import exit
import button

<<<<<<< Updated upstream
# Libby Lewis
print("This is Libby's first commit")
print("Testing Libby's First Branch")
print("Testing again")
=======
# initialize pygame
pygame.init()
>>>>>>> Stashed changes

# declare variables
width = 1600
height = 900

<<<<<<< Updated upstream
# Michaela
print("hellllllllllloooooooooooooooooo - Michaela")

print("Joseph's 2nd Commit")

print("Michaela's branch push")

print("Joseph's 2nd Commit")
=======
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wheel of Jeopardy")
clock = pygame.time.Clock()
>>>>>>> Stashed changes

# surfaces
background_1 = pygame.image.load('images/space_background.jpg').convert()
background_1 = pygame.transform.scale(background_1, (width, height))

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
        back_button = button.Button("BACK", width/2, height/2 + 50)
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


def optionsScreen():
    while True:

        # draw elements
        screen.blit(background_1, (0, 0))
        back_button = button.Button("BACK", width/2, height/2 + 50)
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


mainMenu()
