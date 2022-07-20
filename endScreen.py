# end screen class
import pygame
import button
import textMedium


class EndScreen():
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
        text = textMedium.TextMedium(
            "Thank you for Playing!", self.width/2, self.height/2)
        loop = True
        while loop:

            # buttons
            continue_button = button.Button(
                "CONTINUE", self.width*(1 - 1/8), self.height - 50)

            # draw elements
            self.screen.blit(self.background, (0, 0))
            continue_button.draw(self.screen)
            text.draw(self.screen)

            # event handlers
            for event in pygame.event.get():
                # game window handlers
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if continue_button.clicked:
                    return

                # other handlers
                # ...

            # update the game state
            pygame.display.update()
            self.clock.tick(60)
