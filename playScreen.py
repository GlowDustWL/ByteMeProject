# play screen class
import pygame
import button


class PlayScreen():
    def __init__(self, screen, clock, height, width):
        self.screen = screen
        self.clock = clock
        self.height = height
        self.width = width
        self.background_input = pygame.image.load(
            'images/space_background.jpg').convert()
        self.background = pygame.transform.scale(
            self.background_input, (self.width, self.height))
        self.box_color = (255, 255, 255)

    # main menu

    def getInput(self):

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

        loop = True
        while loop:

            # buttons
            game_completed_button = button.Button(
                "GAME COMPLETED", self.width*(1 - 1/8), self.height - 50)
            quit_to_main_button = button.Button(
                "QUIT TO MAIN", self.width/10, self.height - 50)

            # draw elements
            self.screen.blit(self.background, (0, 0))
            game_completed_button.draw(self.screen)
            quit_to_main_button.draw(self.screen)

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

            # update the game state
            pygame.display.update()
            self.clock.tick(60)
