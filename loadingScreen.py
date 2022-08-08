# loading screen class
import pygame
import button
import inputBox
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
        self.playerList = []

    # main menu

    def getInput(self, numPlayers):
        text = textDisplay.TextDisplay(
            "Brought to you by Team ByteMe", 32, self.width/2, self.height/2 - 400)
        # # player name entry text
        playerNameText = textDisplay.TextDisplay(
            "Enter Player Names", 48, self.width/2, self.height/2 - 120)

        # list for player names
        for i in range(numPlayers):
            self.playerList.append("")

        # Testing
        self.playerList[0] = "hi"

        #input_rect = pygame.Rect(200, 200, 140, 32)
        user_input_1 = inputBox.InputBox(
            self.playerList[0], 32, self.width/2, self.height-50)

        #color_active = pygame.Color('lightskyblue3')
        #color_passive = pygame.Color('chartreuse4')
        #color = color_passive
        #active_input = False

        loop = True
        while loop:

            # buttons
            play_button = button.Button(
                "PLAY", 32, self.width*(1 - 1/8), self.height - 50)
            back_button = button.Button(
                "BACK", 32, self.width/10, self.height - 50)

            # user_input_1 = inputBox.InputBox(
            # "TEST", 32, self. width/2, self.height-50)

            # # player number entry buttons
            # playerNum_2 = button.Button(
            #     "2", 48, self.width/2 - 75, self.height/2)
            # playerNum_3 = button.Button(
            #     "3", 48, self.width//2 - 25, self.height/2)
            # playerNum_4 = button.Button(
            #     "4", 48, self.width//2 + 25, self.height/2)
            # playerNum_5 = button.Button(
            #     "5", 48, self.width//2 + 75, self.height/2)

            #input_rect = pygame.Rect(200, 200, 140, 32)

            # draw elements
            self.screen.blit(self.background, (0, 0))
            play_button.draw(self.screen)
            back_button.draw(self.screen)
            text.draw(self.screen)
            # user_input_1.draw(self.screen)
            # playerNum_2.draw(self.screen)
            # playerNum_3.draw(self.screen)
            # playerNum_4.draw(self.screen)
            # playerNum_5.draw(self.screen)
            playerNameText.draw(self.screen)
            #color_active = pygame.Color('lightskyblue3')
            #color_passive = pygame.Color('chartreuse4')
            #color = color_passive
            #active_input = False

            # event handlers
            for event in pygame.event.get():
                # game window handlers
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # if playerNum_2.clicked:
                #     self.numPlayers = 2
                #     return True
                # if playerNum_3.clicked:
                #     self.numPlayers = 3
                #     return True
                # if playerNum_4.clicked:
                #     self.numPlayers = 4
                #     return True
                # if playerNum_5.clicked:
                #     self.numPlayers = 5
                #     return True
                if play_button.clicked:
                    return True
                if back_button.clicked:
                    loop = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("in mouse down")
                    if user_input_1.input_rect.collidepoint(event.pos):
                        user_input_1.clicked = True
                        user_input_1.current_color = user_input_1.active_color
                    else:
                        user_input_1.clicked = False
                        user_input_1.current_color = user_input_1.passive_color
                if event.type == pygame.KEYDOWN:
                    print("in keydown")
                    if event.key == pygame.K_BACKSPACE:
                        self.playerList[0] = self.playerList[0][:-1]
                    elif event.key == pygame.K_RETURN:
                        user_input_1.clicked = False
                        user_input_1.current_color = user_input_1.passive_color
                    elif event.key == pygame.K_KP_ENTER:
                        user_input_1.clicked = False
                        user_input_1.current_color = user_input_1.passive_color
                    else:
                        print("in player list")
                        self.playerList[0] += event.unicode
                        print(self.playerList[0])

            user_input_1.draw(self.screen, self.playerList[0])
            pygame.display.flip()

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #    if input_rect.collidepoint(event.pos):
            #        active_input = True
            #    else:
            #        active_input = False
            # if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_BACKSPACE:
            #        self.playerList[0] = self.playerList[0][:-1]
            #    elif event.key == pygame.K_RETURN:
            #        active_input = False
            #    elif event.key == pygame.K_KP_ENTER:
            #        active_input = False
            #    else:
            #        self.playerList[0] += event.unicode

            # other handlers
            # ...

            # if active_input:
            #    color = color_active
            # else:
            #    color = color_passive

            #base_font = pygame.font.Font(None, 32)
            # pygame.draw.rect(
            #    self.screen, user_input_1.current_color, user_input_1.input_rect)
            # text_surface = base_font.render(
            #    self.playerList[0], True, (255, 255, 255))
            # self.screen.blit(
            #    text_surface, (user_input_1.input_rect.x+5, user_input_1.input_rect.y+5))
            #user_input_1.input_rect.w = max(100, text_surface.get_width()+10)

            # pygame.display.flip()

            # update the game state
            pygame.display.update()
            self.clock.tick(60)
