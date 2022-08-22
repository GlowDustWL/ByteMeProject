# end screen class
import pygame
import button
import textMedium
import textDisplay
#from playsound import playsound


class EndScreen():
    def __init__(self, screen, clock, height, width):
        self.screen = screen
        self.clock = clock
        self.height = height
        self.width = width
        self.background_input = pygame.image.load(
            'images/space_background.jpeg').convert()
        self.background = pygame.transform.smoothscale(
            self.background_input, (self.width, self.height))
        self.playerList = []

    # main menu

    def getInput(self, numPlayers, playerList, finalScores):
        #playsound('uplifting.mp3', False)
        text = textMedium.TextMedium(
            "Thank you for Playing!", self.width/2, self.height/2 - 300)
        # self.screen.blit(self.background, (0, 0))
        playerScoreIntro = textDisplay.TextDisplay(
            "Final player scores:", 26, self.width/2, self.height/2 - 200)

        # determining winner
        print("[LOG]: " + str(len(finalScores)))
        winner = 0
        for x in range(1, len(finalScores)):
            print("[LOG]: Player " + str(x) + " " + str(finalScores[x]))
            #print("[LOG]: Player " + str(x) + " " + str(finalScores[x+1]))
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
        return_to_main = button.Button(
            "MAIN MENU", 32, self.width*(1 - 1/8), self.height - 50)

        # draw first elements
        self.screen.blit(self.background, (0, 0))
        return_to_main.draw(self.screen)
        text.draw(self.screen)
        playerScoreIntro.draw(self.screen)
        # draw player names/scores
        for x in nameTextArray:
            x.draw(self.screen)
        for x in scoreTextArray:
            x.draw(self.screen)

        m = pygame.mixer.music
        m.load('drumroll.wav')
        m.play()
        pygame.display.update()
        pygame.event.pump()
        # while (m.get_busy()):
        #    pygame.time.wait(10)
        m.queue('uplifting.mp3')
        # m.play()
        pygame.time.wait(5500)
        #self.screen.blit(self.background, (0, 0))
        winnerText.draw(self.screen)
        # pygame.display.update()
        # pygame.event.pump()
        # pygame.time.wait(50000)

        # pygame.display.update()
        # pygame.time.wait(50000)
        # pygame.display.update()
        # pygame.mixer.init()
        #drumroll = pygame.mixer.Sound('drumroll.wav')
        #congrats = pygame.mixer.Sound('uplifting.mp3')
        #channel = drumroll.play()
        # while (channel.get_busy()):
        #    pygame.time.wait(100)
        #self.screen.blit(self.background, (0, 0))
        # congrats.play()
        # winnerText.draw(self.screen)
        # pygame.time.wait(1000)
        # return
        # pygame.display.update()

        loop = True
        while loop:

            return_to_main.draw(self.screen)

        # event handlers
            for event in pygame.event.get():
                # game window handlers
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if return_to_main.clicked:
                    return

        # other handlers
        # ...

        # update the game state
            pygame.display.update()
            self.clock.tick(60)
