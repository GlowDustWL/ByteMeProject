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
            "Enter Player Names", 48, self.width/2, self.height/2 - 220)

        # list for player names
        for i in range(numPlayers):
            self.playerList.append("Enter Name Here")

        # Testing
        #self.playerList[0] = "Player 1"

        # create text for each player to display scores
        nameTextArray = []
        for i in range(numPlayers):
            nameTextArray.append(textDisplay.TextDisplay(
                ("Player " + str(i+1)), 26, self.width/2 - 170, self.height - 580 + 100*i))

        input_boxes = []
        for i in range(numPlayers):
            input_boxes.append(inputBox.InputBox(
                self.playerList[i], 32, self.width/2 - 70, self.height - 600 + 100*i))
        # user_input_1 = inputBox.InputBox(
        #    self.playerList[0], 32, self.width/2 - 75, self.height/2)

        loop = True
        while loop:

            # buttons
            play_button = button.Button(
                "PLAY", 32, self.width*(1 - 1/8), self.height - 50)
            back_button = button.Button(
                "BACK", 32, self.width/10, self.height - 50)

            # # player number entry buttons
            # playerNum_2 = button.Button(
            #     "2", 48, self.width/2 - 75, self.height/2)
            # playerNum_3 = button.Button(
            #     "3", 48, self.width//2 - 25, self.height/2)
            # playerNum_4 = button.Button(
            #     "4", 48, self.width//2 + 25, self.height/2)
            # playerNum_5 = button.Button(
            #     "5", 48, self.width//2 + 75, self.height/2)

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

            # draw player names/scores
            for x in nameTextArray:
                x.draw(self.screen)

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
                    for x in input_boxes:
                        if x.input_rect.collidepoint(event.pos):
                            x.clicked = True
                            x.current_color = x.active_color
                            self.playerList[input_boxes.index(x)] = ""
                        else:
                            x.clicked = False
                            x.current_color = x.passive_color
                    print("in mouse down")
                    # if user_input_1.input_rect.collidepoint(event.pos):
                    #    user_input_1.clicked = True
                    #    user_input_1.current_color = user_input_1.active_color
                    # else:
                    #    user_input_1.clicked = False
                    #    user_input_1.current_color = user_input_1.passive_color
                if event.type == pygame.KEYDOWN:
                    #current_box = input_boxes[0]
                    #player_num = 0
                    for x in input_boxes:
                        if x.clicked:
                            player_num = input_boxes.index(x)
                            #current_box = x
                            #player_num = input_boxes.index(x)
                            if event.key == pygame.K_BACKSPACE:
                                self.playerList[player_num] = self.playerList[player_num][:-1]
                            elif event.key == pygame.K_RETURN:
                                x.clicked = False
                                x.current_color = x.passive_color
                            elif event.key == pygame.K_KP_ENTER:
                                x.clicked = False
                                x.current_color = x.passive_color
                            else:
                                self.playerList[player_num] += event.unicode
                    #print("in keydown")
                    # if event.key == pygame.K_BACKSPACE:
                    #    self.playerList[0] = self.playerList[0][:-1]
                    # elif event.key == pygame.K_RETURN:
                    #    user_input_1.clicked = False
                    #    user_input_1.current_color = user_input_1.passive_color
                    # elif event.key == pygame.K_KP_ENTER:
                    #    user_input_1.clicked = False
                    #    user_input_1.current_color = user_input_1.passive_color
                    # else:
                    #    print("in player list")
                    #    self.playerList[0] += event.unicode
                    #    print(self.playerList[0])

            #j = 0
            for x in input_boxes:
                x.draw(self.screen, self.playerList[input_boxes.index(x)])
                #j += 1
            #user_input_1.draw(self.screen, self.playerList[0])

            # other handlers
            # ...

            # update the game state
            pygame.display.update()
            self.clock.tick(60)
