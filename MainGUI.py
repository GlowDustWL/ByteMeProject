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
            # initialize background music
            m = pygame.mixer.music
            m.load('bkg_music.mp3')
            m.play(-1)
            m.set_volume(1)

            if self.menuScreen.getInput():
                self.numPlayers = self.menuScreen.numPlayers
                if self.loadingScreen.getInput(self.numPlayers):
                    self.playerList = self.loadingScreen.playerList
                    # lower volume of background music
                    m.set_volume(0.2)
                    if self.playScreen.getInput(self.numPlayers,
                                                self.playerList):
                        self.playerScores = self.playScreen.finalScores
                        # stop background music
                        m.stop()
                        self.endScreen.getInput(self.numPlayers, self.playerList,
                                                self.playerScores)


game = MainGUI().play()
