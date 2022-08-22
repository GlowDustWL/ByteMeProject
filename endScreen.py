# end screen class
import pygame
import button
import textMedium
import textDisplay
import util


class EndScreen():
    def __init__(self, screen, clock, height, width):
        self.screen = screen
        self.clock = clock
        self.height = height
        self.width = width
        self.background_input = pygame.image.load(util.resourcePath(
            'images/space_background.jpeg')).convert()
        self.background = pygame.transform.smoothscale(
            self.background_input, (self.width, self.height))
        self.playerList = []

    # main menu

    def getInput(self, numPlayers, playerList, finalScores):
        # initalizing sounds
        pygame.mixer.init()
        selection = pygame.mixer.Sound(
            util.resourcePath('sounds/selection.mp3'))

        text = textMedium.TextMedium(
            "Thank you for Playing!", self.width/2, self.height/2 - 300)
        # self.screen.blit(self.background, (0, 0))
        playerScoreIntro = textDisplay.TextDisplay(
            "Final player scores:", 26, self.width/2, self.height/2 - 200)

        # determining winner
        print("[LOG]: " + str(len(finalScores)))
        winner = 0
        for x in range(1, len(finalScores)):
            if (finalScores[winner] == finalScores[x]):
                winner = 7
                break
            if (finalScores[winner] < finalScores[x]):
                winner = x

        if (winner == 7):
            winnerText = textMedium.TextMedium(
                "It's a tie!", self.width/2, self.height/2 + 250)
        else:
            winnerText = textMedium.TextMedium(
                "The winner is " + playerList[winner] + "!", self.width/2, self.height/2 + 250)

        nameTextArray = []
        scoreTextArray = []
        for x in range(numPlayers):
            nameTextArray.append(textDisplay.TextDisplay(
                playerList[x] + ":", 26, self.width/2 - 90, self.height - 550 + 70*x))
            scoreTextArray.append(textDisplay.TextDisplay(
                str(finalScores[x]), 26, self.width/2 + 100, self.height - 550 + 70*x))

        # buttons
        continue_button = button.Button(
            "MAIN MENU", 32, self.width*(1 - 1/8), self.height - 50)

        # draw first elements
        self.screen.blit(self.background, (0, 0))
        continue_button.draw(self.screen)
        text.draw(self.screen)
        playerScoreIntro.draw(self.screen)
        # draw player names/scores
        for x in nameTextArray:
            x.draw(self.screen)
        for x in scoreTextArray:
            x.draw(self.screen)

        # initializing drumroll
        m = pygame.mixer.music
        m.load(util.resourcePath('sounds/drumroll.wav'))
        m.play()
        m.set_volume(1)
        pygame.display.update()
        pygame.event.pump()
        # cue next music
        m.queue(util.resourcePath('sounds/uplifting.mp3'))

        # wait for drumroll before displaying winner
        pygame.time.wait(5500)
        #self.screen.blit(self.background, (0, 0))
        winnerText.draw(self.screen)
        pygame.time.wait(500)

        loop = True
        while loop:

            continue_button.draw(self.screen)

        # event handlers
            for event in pygame.event.get():
                # game window handlers
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if continue_button.clicked:
                    selection.play()
                    return

        # other handlers
        # ...

        # update the game state
            pygame.display.update()
            self.clock.tick(60)
