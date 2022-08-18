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

        # buttons
        play_button = button.Button(
            "PLAY", 32, self.width*(1 - 1/8), self.height - 50)
        back_button = button.Button(
            "BACK", 32, self.width/10, self.height - 50)

        loop = True
        while loop:

            # draw elements
            self.screen.blit(self.background, (0, 0))
            play_button.draw(self.screen)
            back_button.draw(self.screen)
            playerNameText.draw(self.screen)

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
