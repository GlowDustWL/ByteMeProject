# MainGUI class

# import statements
from turtle import screensize
import pygame
import mainMenu
import loadingScreen
import playScreen
import endScreen
import threading
#import multiprocessing
from playsound import playsound
import pyaudio
import wave
import time


class MainGUI():
    def __init__(self):

        self.height = 900
        self.width = 1600
        self.screen = pygame.display.set_mode(
            (self.width, self.height))
        self.clock = pygame.time.Clock()
        #self.t1 = threading.Thread(target=playsound('selection.mp3', False))

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

    # def loopSound():
    #    while True:
    #        playsound('space.mp3', block=True)

    def play(self):
        pygame.init()

        # Currently plays background music once then stops
        def loopSound():
            while True:
                playsound('bkg_music.mp3', block=True)
        loopThread = threading.Thread(
            target=loopSound, name='backgroundMusicThread')
        loopThread.daemon = True
        loopThread.start()

        while True:
            # Attempting to start and stop music using pyaudio instead of playsound

            #background_music = wave.open('space_9ljFoAnf.wav', 'rb')
            #p = pyaudio.PyAudio()
            #chunk = 1024

            # def callback(in_data, frame_count, time_info, status):
            #    data = background_music.readframes(frame_count)
            #    return (data, pyaudio.paContinue)

            # stream = p.open(format=p.get_format_from_width(background_music.getsampwidth()),
            #                channels=background_music.getnchannels(),
            #                rate=background_music.getframerate(),
            #                output=True,
            #                stream_callback=callback)
            #data = background_music.readframes(chunk)
            #loop = True
            # while loop:
            #    stream.write(data)
            #    data = background_music.readframes(chunk)
            #    if data == b'':
            #        background_music.rewind()
            #        data = background_music.readframes(chunk)

            # stream.stop_stream()
            # stream.start_stream()
            # stream.stop_stream()
            # stream.close()
            # background_music.close()
            # p.terminate()

            # Attempting to loop music using multiprocessing and playsound
            # p = multiprocessing.Process(
            #    target=playsound, args=('space.mp3', False))
            # p.start()
            # p.terminate()
            # while True:
            #    if not self.t1.is_alive():
            #        self.t1 = threading.Thread(
            #            target=playsound('space.mp3', False))
            #        self.t1.start()
            #playsound('space.mp3', False)
            if self.menuScreen.getInput():
                self.numPlayers = self.menuScreen.numPlayers
                # stream.close()
                # background_music.close()
                # p.terminate()
                if self.loadingScreen.getInput(self.numPlayers):
                    self.playerList = self.loadingScreen.playerList
                    # self.numPlayers = self.loadingScreen.numPlayers
                    # p.terminate()
                    if self.playScreen.getInput(self.numPlayers,
                                                self.playerList):
                        self.playerScores = self.playScreen.finalScores
                        self.endScreen.getInput(self.numPlayers, self.playerList,
                                                self.playerScores)

    # def play_my_sound():
    #    playsound('space.mp3', False)


game = MainGUI().play()
