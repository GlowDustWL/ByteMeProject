# main menu class
import pygame
import button
import textTitle
import textDisplay


class MainMenu():
    def __init__(self, screen, clock, height, width):
        self.screen = screen
        self.clock = clock
        self.height = height
        self.width = width
        self.background_input = pygame.image.load(
            'images/space_background.jpeg').convert()
        self.background = pygame.transform.smoothscale(
            self.background_input, (self.width, self.height))
        self.numPlayers = 0

    # main menu

    def getInput(self):

        # initializing sounds
        pygame.mixer.init()
        selection = pygame.mixer.Sound('selection.mp3')

        text = textTitle.TextTitle("Wheel of Jeopardy", self.width/2, 200)
        subtitle = textDisplay.TextDisplay(
            "Created by The ByteMe Team", 16, self.width/2, 250)

        # self.screen.blit(self.background, (0, 0))
        # pygame.display.update()

        # player number entry text
        playerNumText = textDisplay.TextDisplay(
            "Select Number of Players", 48, self.width/2, self.height/2 - 105)

        # buttons
        # start_button = button.Button(
        #     "START", 36, self.width/2, self.height/2)
        exit_button = button.Button(
            "EXIT", 36, self.width/2, self.height/2 + 200)

        # player number entry buttons
        playerNum_2 = button.Button(
            "2", 36, self.width/2 - 75, self.height/1.8)
        playerNum_3 = button.Button(
            "3", 36, self.width//2 - 25, self.height/1.8)
        playerNum_4 = button.Button(
            "4", 36, self.width//2 + 25, self.height/1.8)
        playerNum_5 = button.Button(
            "5", 36, self.width//2 + 75, self.height/1.8)

        while True:

            # draw elements
            self.screen.blit(self.background, (0, 0))
            # start_button.draw(self.screen)
            exit_button.draw(self.screen)
            text.draw(self.screen)
            subtitle.draw(self.screen)

            playerNum_2.draw(self.screen)
            playerNum_3.draw(self.screen)
            playerNum_4.draw(self.screen)
            playerNum_5.draw(self.screen)
            playerNumText.draw(self.screen)

            # event handlers
            for event in pygame.event.get():
                # game window handlers
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # if start_button.clicked:
                #     return True
                if exit_button.clicked:
                    pygame.quit()
                    exit()
                if playerNum_2.clicked:
                    self.numPlayers = 2
                    selection.play()
                    return True
                if playerNum_3.clicked:
                    self.numPlayers = 3
                    selection.play()
                    return True
                if playerNum_4.clicked:
                    self.numPlayers = 4
                    selection.play()
                    return True
                if playerNum_5.clicked:
                    self.numPlayers = 5
                    selection.play()
                    return True
                # other handlers
                # ...

            # update the game state
            pygame.display.update()
            self.clock.tick(60)
