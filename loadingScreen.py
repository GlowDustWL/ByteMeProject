# loading screen class
import pygame
import button
import textMedium


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

    # main menu

    def getInput(self):
        text = textMedium.TextMedium(
            "Brought to you by Team ByteMe", self.width/2, self.height/2)
        loop = True
        while loop:

            # buttons
            play_button = button.Button(
                "PLAY", self.width*(1 - 1/8), self.height - 50)
            back_button = button.Button(
                "BACK", self.width/10, self.height - 50)

            # draw elements
            self.screen.blit(self.background, (0, 0))
            play_button.draw(self.screen)
            back_button.draw(self.screen)
            text.draw(self.screen)

            # event handlers
            for event in pygame.event.get():
                # game window handlers
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if play_button.clicked:
                    return True
                if back_button.clicked:
                    loop = False

                # other handlers
                # ...

            # update the game state
            pygame.display.update()
            self.clock.tick(60)
