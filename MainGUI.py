# import statements
import pygame
#from sys import exit
#import button
import mainMenu
import loadingScreen
import playScreen
import endScreen


# initialize pygame
pygame.init()


# declare variables
height = 900
width = 1600


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wheel of Jeopardy!")
clock = pygame.time.Clock()


# create objects for each screen
menuScreen = mainMenu.MainMenu(screen, clock, height, width)
# the information screen
loadingScreen = loadingScreen.LoadingScreen(screen, clock, height, width)
playScreen = playScreen.PlayScreen(screen, clock, height, width)
endScreen = endScreen.EndScreen(screen, clock, height, width)

# loop that iterates to drive game window state.
while True:

    if menuScreen.getInput():
        if loadingScreen.getInput():
            if playScreen.getInput():
                endScreen.getInput()
