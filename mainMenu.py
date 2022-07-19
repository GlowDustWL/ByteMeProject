# main menu class
import pygame
import button
import textTitle


class MainMenu():
    def __init__(self, screen, clock, height, width):
        self.screen = screen
        self.clock = clock
        self.height = height
        self.width = width
        self.background_input = pygame.image.load(
            'images/space_background.jpg').convert()
        self.background = pygame.transform.scale(
            self.background_input, (self.width, self.height))

    # main menu

    def getInput(self):
        text = textTitle.TextTitle("Wheel of Jeopardy", self.width/2, 150)
        while True:

            # buttons
            start_button = button.Button("START", self.width/2, self.height/2)
            exit_button = button.Button(
                "EXIT", self.width/2, self.height/2 + 50)

            # draw elements
            self.screen.blit(self.background, (0, 0))
            start_button.draw(self.screen)
            exit_button.draw(self.screen)
            text.draw(self.screen)

            # event handlers
            for event in pygame.event.get():
                # game window handlers
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if start_button.clicked:
                    return True
                if exit_button.clicked:
                    pygame.quit()
                    exit()

                # other handlers
                # ...

            # update the game state
            pygame.display.update()
            self.clock.tick(60)
