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

        # player count
        self.numPlayers = 0

        # player names
        self.playerList = []

        # player scores
        self.playerScores = []

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
                self.numPlayers = self.menuScreen.numPlayers
                if self.loadingScreen.getInput(self.numPlayers):
                    self.playerList = self.loadingScreen.playerList
                    # self.numPlayers = self.loadingScreen.numPlayers
                    if self.playScreen.getInput(self.numPlayers,
                                                self.playerList):
                        self.playerScores = self.playScreen.finalScores
                        self.endScreen.getInput(self.numPlayers, self.playerList,
                                                self.playerScores)


game = MainGUI().play()
