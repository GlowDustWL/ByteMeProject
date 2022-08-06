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
        # title boxes
        self.categories = ['will', 'libby', 'chris', 'joe', 'mich', 'xyz']

        # player count
        self.numPlayers = 0

        # screens
        self.menuScreen = mainMenu.MainMenu(
            self.screen, self.clock, self.height, self.width)
        self.loadingScreen = loadingScreen.LoadingScreen(
            self.screen, self.clock, self.height, self.width)
        self.playScreen = playScreen.PlayScreen(
            self.screen, self.clock, self.height, self.width, self.categories)
        self.endScreen = endScreen.EndScreen(
            self.screen, self.clock, self.height, self.width)

    def play(self):
        pygame.init()

        while True:
            self.playScreen.getInput(2)


game = MainGUI().play()
