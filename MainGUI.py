# MainGUI class

# import statements
from turtle import screensize
import pygame
import mainMenu
import loadingScreen
import playScreen
import endScreen


class MainGUI():
    def __init__(self):

        self.height = 900
        self.width = 1600
        self.screen = pygame.display.set_mode(
            (self.width, self.height))
        self.clock = pygame.time.Clock()

        # screens
        self.menuScreen = mainMenu.MainMenu(
            self.screen, self.clock, self.height, self.width)
        self.loadingScreen = loadingScreen.LoadingScreen(
            self.screen, self.clock, self.height, self.width)
        self.playScreen = playScreen.PlayScreen(
            self.screen, self.clock, self.height, self.width)
        self.endScreen = endScreen.EndScreen(
            self.screen, self.clock, self.height, self.width)

    def play(self):
        pygame.init()

        while True:
            if self.menuScreen.getInput():
                if self.loadingScreen.getInput():
                    if self.playScreen.getInput():
                        self.endScreen.getInput()


game = MainGUI().play()
