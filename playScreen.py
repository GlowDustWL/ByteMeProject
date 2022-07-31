# play screen class
import pygame
import button
import pygame.gfxdraw
import MainDriver
import textDisplay
import textTitle


class PlayScreen():
    def __init__(self, screen, clock, height, width):
        self.screen = screen
        self.clock = clock
        self.height = height
        self.width = width
        self.background_input = pygame.image.load(
            'images/space_background.jpeg').convert()
        self.background = pygame.transform.smoothscale(
            self.background_input, (self.width, self.height))
        self.box_color = (255, 255, 255)

        # self.game = MainDriver.Game()

    # main menu

    def getInput(self):
        # initialize game instance
        game = MainDriver.Game()

        # drawing rectangleS
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            50, 50, 600, 400),  2, 3)  # Wheel section
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            950, 50, 600, 480),  2, 3)  # Jeopardy section
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            680, 50, 240, 400),  2, 3)  # Player info section
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            50, 480, 870, 50),  2, 3)  # status/ user promp
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            50, 550, 870, 255),  2, 3)  # questions / answers
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            950, 555, 50, 50),  2, 3)  # asnwer question button: A
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            950, 620, 50, 50),  2, 3)  # asnwer question button: B
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            950, 685, 50, 50),  2, 3)  # asnwer question button: C
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            950, 750, 50, 50),  2, 3)  # asnwer question button: D
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            1150, 652, 200, 50),  2, 3)  # Spin The Wheel !
        # pygame.gfxdraw.rectangle(self.background, pygame.Rect(
        #     50, 50, 600, 400), self.box_color)

        # drawing text
        wheelText = textDisplay.TextDisplay(
            "", 46, 350, 250)
        spinCount = textDisplay.TextDisplay(
            "Spins left: " + str(game.spins_left), 26, 150, 425)

        # self.screen.blit(self.background, (0, 0))

        show_spin = True
        loop = True
        while loop:

            # buttons
            game_completed_button = button.Button(
                "GAME COMPLETED", self.width*(1 - 1/8), self.height - 50)
            quit_to_main_button = button.Button(
                "QUIT TO MAIN", self.width/10, self.height - 50)
            spin_button = button.Button(
                "SPIN", 600, 425)

            # draw elements
            self.screen.blit(self.background, (0, 0))
            game_completed_button.draw(self.screen)
            quit_to_main_button.draw(self.screen)
            wheelText.draw(self.screen)
            spinCount.draw(self.screen)

            if show_spin:
                spin_button.draw(self.screen)

            # event handlers
            for event in pygame.event.get():
                # game window handlers
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if game_completed_button.clicked:
                    return True
                if quit_to_main_button.clicked:
                    loop = False

                # other handlers
                # ...
                if spin_button.clicked:
                    spin_result = game.spin()
                    game.spins_left -= 1
                    wheelText.setText(str(spin_result))
                    spinCount.setText(
                        "Spins left: " + str(game.spins_left))
                    # show_spin = False

            # update the game state
            pygame.display.update()
            self.clock.tick(60)
