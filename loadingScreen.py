# loading screen class
import pygame
import button
import textMedium
import textDisplay


class LoadingScreen():
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
        text = textDisplay.TextDisplay(
            "Brought to you by Team ByteMe", 32, self.width/2, self.height/2 - 400)
        # player number entry text
        playerNumText = textDisplay.TextDisplay(
            "Select Number of Players", 48, self.width/2, self.height/2 - 120)

        loop = True
        while loop:

            # buttons
            # play_button = button.Button(
            #     "PLAY", 32, self.width*(1 - 1/8), self.height - 50)
            back_button = button.Button(
                "BACK", 32, self.width/10, self.height - 50)

            # player number entry buttons
            playerNum_2 = button.Button(
                "2", 48, self.width/2 - 75, self.height/2)
            playerNum_3 = button.Button(
                "3", 48, self.width//2 - 25, self.height/2)
            playerNum_4 = button.Button(
                "4", 48, self.width//2 + 25, self.height/2)
            playerNum_5 = button.Button(
                "5", 48, self.width//2 + 75, self.height/2)

            # draw elements
            self.screen.blit(self.background, (0, 0))
            # play_button.draw(self.screen)
            back_button.draw(self.screen)
            text.draw(self.screen)
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
                if playerNum_2.clicked:
                    self.numPlayers = 2
                    return True
                if playerNum_3.clicked:
                    self.numPlayers = 3
                    return True
                if playerNum_4.clicked:
                    self.numPlayers = 4
                    return True
                if playerNum_5.clicked:
                    self.numPlayers = 5
                    return True
                if back_button.clicked:
                    loop = False

                # other handlers
                # ...

            # update the game state
            pygame.display.update()
            self.clock.tick(60)
