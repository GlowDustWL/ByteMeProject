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
        self.box_color = (255, 255, 255)

        self.info_screen_1 = pygame.image.load(
            'images/loading_Screen_Info_1.png').convert()
        self.loading_screen_pics_1 = pygame.transform.smoothscale(
            self.info_screen_1, (369, 222))

        self.info_screen_2 = pygame.image.load(
            'images/questions_Prump.png').convert()
        self.loading_screen_pics_2 = pygame.transform.smoothscale(
            self.info_screen_2, (369, 222))

        self.info_screen_3 = pygame.image.load(
            'images/game_info_Player_info.png').convert()
        self.loading_screen_pics_3 = pygame.transform.smoothscale(
            self.info_screen_3, (369, 222))

    # main menu

    def getInput(self, numPlayers):
        # # player name entry text
        playerNameText = textDisplay.TextDisplayPink(
            "Enter Player Names", 48, self.width/2 + 470, self.height/2 - 300)

        # list for player names
        for i in range(numPlayers):
            # populated with 'Enter Name Here' for instructions
            self.playerList.append("Enter Name Here")

        # create text for each player to display player number
        nameTextArray = []
        for i in range(numPlayers):
            nameTextArray.append(textDisplay.TextDisplay(
                ("Player " + str(i+1) + ":"), 26, self.width/2 + 300, self.height - 660 + 100*i))

        # create array of input boxes for each player
        input_boxes = []
        for i in range(numPlayers):
            input_boxes.append(inputBox.InputBox(
                self.playerList[i], 32, self.width/2 + 400, self.height - 680 + 100*i))

         # text_info_Screen_1
        text_info_screen_1 = textDisplay.TextDisplay(
            "The Wheel and Board are the two main components of this game. ", 16, 710, 68)
        text_info_screen_12 = textDisplay.TextDisplay(
            "You will not interact with either of them. The board will be displayed ", 16, 718, 89)
        text_info_screen_13 = textDisplay.TextDisplay(
            "on the left of the screen and will begin to spin after you click the spin ", 16, 721, 110)
        text_info_screen_14 = textDisplay.TextDisplay(
            "button. The Board will display the categories as well as the value ", 16, 709, 131)
        text_info_screen_15 = textDisplay.TextDisplay(
            "for each question. The Board will clear the question upon a correct ", 16, 717, 152)
        text_info_screen_16 = textDisplay.TextDisplay(
            "answer being given.  ", 16, 540, 173)

        # text_info_Screen_2
        text_info_screen_21 = textDisplay.TextDisplay(
            "To the left shows, the question prompt and questions answer part ", 16, 711, 315)
        text_info_screen_22 = textDisplay.TextDisplay(
            "of the game. If the wheel landed on a category and that category  ", 16, 708, 336)
        text_info_screen_23 = textDisplay.TextDisplay(
            "still shows questions left to answer on the board then a question  ", 16, 710, 357)
        text_info_screen_24 = textDisplay.TextDisplay(
            "will be shown to you under the question prompt area. The question ", 16, 715, 378)
        text_info_screen_25 = textDisplay.TextDisplay(
            "answers will be populated with 4 multiple choice answers.  The player  ", 16, 730, 399)
        text_info_screen_26 = textDisplay.TextDisplay(
            "who answers the question correctly will earn points based on ", 16, 693, 420)
        text_info_screen_27 = textDisplay.TextDisplay(
            "the question amount. The players who do not answer the question  ", 16, 716, 441)
        text_info_screen_28 = textDisplay.TextDisplay(
            "correctly will lose the points that the question is worth. To select an  ", 16, 718, 462)
        text_info_screen_29 = textDisplay.TextDisplay(
            "answer choose A, B, C, or D off to the right.  ", 16, 624, 483)
        # buttons
        play_button = button.Button(
            "PLAY", 32, self.width*(1 - 1/8), self.height - 50)
        back_button = button.Button(
            "BACK", 32, self.width/10, self.height - 50)

        loop = True
        while loop:

            # draw elements
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.background, (0, 0))
            play_button.draw(self.screen)
            back_button.draw(self.screen)
            playerNameText.draw(self.screen)
            self.screen.blit(self.loading_screen_pics_1, (52, 52))
            self.screen.blit(self.loading_screen_pics_2, (52, 302))
            self.screen.blit(self.loading_screen_pics_3, (52, 552))
            # draw info scrren 1 text
            text_info_screen_1.draw(self.screen)
            text_info_screen_12.draw(self.screen)
            text_info_screen_13.draw(self.screen)
            text_info_screen_14.draw(self.screen)
            text_info_screen_15.draw(self.screen)
            text_info_screen_16.draw(self.screen)
            # draw info scrren 2 text
            text_info_screen_21.draw(self.screen)
            text_info_screen_22.draw(self.screen)
            text_info_screen_23.draw(self.screen)
            text_info_screen_24.draw(self.screen)
            text_info_screen_25.draw(self.screen)
            text_info_screen_26.draw(self.screen)
            text_info_screen_27.draw(self.screen)
            text_info_screen_28.draw(self.screen)
            text_info_screen_29.draw(self.screen)

            # draw player numbers
            for x in nameTextArray:
                x.draw(self.screen)

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
                # check if input box clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check which input box
                    for x in input_boxes:
                        if x.input_rect.collidepoint(event.pos):
                            x.clicked = True
                            # update box color
                            x.current_color = x.active_color
                            # remove 'enter name here' text
                            self.playerList[input_boxes.index(x)] = ""
                        else:
                            x.clicked = False
                            # update box color
                            x.current_color = x.passive_color
                # check if keyboard input given
                if event.type == pygame.KEYDOWN:
                    # check which input box
                    for x in input_boxes:
                        if x.clicked:
                            # character limit
                            if (x.text_surface_width > 200):
                                x.clicked = False
                                x.current_color = x.passive_color
                                break
                            # corresponding player number for input box
                            player_num = input_boxes.index(x)
                            # if backspace pressed, remove character
                            if event.key == pygame.K_BACKSPACE:
                                self.playerList[player_num] = self.playerList[player_num][:-1]
                            # if return or keypad enter pressed, change input to not clicked
                            elif (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                                x.clicked = False
                                x.current_color = x.passive_color
                            # if tab pressed, change input to not clicked
                            elif event.key == pygame.K_TAB:
                                x.clicked = False
                                x.current_color = x.passive_color
                            # if other key pressed, add unicode character to player name
                            else:
                                self.playerList[player_num] += event.unicode

            pygame.draw.rect(self.background, self.box_color, pygame.Rect(
                50, 50, 375, 225),  2, 3)  # Block #1
            pygame.draw.rect(self.background, self.box_color, pygame.Rect(
                50, 300, 375, 225),  2, 3)  # Block #2
            pygame.draw.rect(self.background, self.box_color, pygame.Rect(
                50, 550, 375, 225),  2, 3)  # Block #3
            pygame.draw.rect(self.background, self.box_color, pygame.Rect(
                450, 50, 550, 225),  2, 3)  # Info for Wheel, Player, Board
            pygame.draw.rect(self.background, self.box_color, pygame.Rect(
                450, 300, 550, 225),  2, 3)  # Info for Prompt and questions
            pygame.draw.rect(self.background, self.box_color, pygame.Rect(
                450, 550, 550, 225),  2, 3)  # Info for Spin wheel and flow info
            # draw input boxes
            for x in input_boxes:
                x.draw(self.screen, self.playerList[input_boxes.index(x)])

            # update the game state
            pygame.display.update()
            self.clock.tick(60)
