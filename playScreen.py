# play screen class
import pygame
import button
import pygame.gfxdraw
import MainDriver
import textDisplay
import textTitle
import jeopardyBoard
import wheel
from flattenList import flattenList
import textDisplayLeft


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
        # title boxes
        self.categories = []
        self.questions = []
        self.answers = [[]]

        # self.game = MainDriver.Game()

    # main menu

    def getInput(self, numPlayers, playerList):
        def refresh_current_player_score():
            scoreTextArray[game.current_player].setText(
                str(game.players[game.current_player].score))

        def refresh_current_player_indicator():
            for x in range(len(game.players)):
                nameTextArray[x].setText(
                    game.players[x].name)
            nameTextArray[game.current_player].setText(
                "->"+game.players[game.current_player].name+"<-")

        # initialize game instance
        game = MainDriver.Game(numPlayers, playerList)

        # parse categories to be displayed
        self.categories.append(game.questions[0][0])
        self.categories.append(game.questions[1][0])
        self.categories.append(game.questions[2][0])
        self.categories.append(game.questions[3][0])
        self.categories.append(game.questions[4][0])
        self.categories.append(game.questions[5][0])
        self.categories = flattenList(self.categories)

        print(game.questions[0][1][0])
        print(game.questions[4][1][0])

        # drawing rectangleS
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            50, 50, 600, 400),  2, 3)  # Wheel section
        # pygame.draw.rect(self.background, self.box_color, pygame.Rect(
        #     950, 50, 600, 480),  2, 3)  # Jeopardy section
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
        # pygame.draw.rect(self.background, self.box_color, pygame.Rect(
        #     1150, 652, 200, 50),  2, 3)  # Spin The Wheel !
        # pygame.gfxdraw.rectangle(self.background, pygame.Rect(
        #     50, 50, 600, 400), self.box_color)

        # drawing text
        wheelText = textDisplay.TextDisplay(
            "", 46, 1250, 750)
        spinCountText = textDisplay.TextDisplay(
            "Spins left: ", 26, 150, 425)
        spinCountNum = textDisplay.TextDisplay(
            str(game.spins_left), 26, 230, 425)
        narration = textDisplay.TextDisplay(
            "Press \"SPIN\" to spin the wheel.", 26, 1265, 630)

        # Questions/Answer Display
        questionText = textDisplay.TextDisplay(
            "No question to answer yet", 26, 480, 507)
        ansAText = textDisplayLeft.TextDisplayLeft(
            "answer A", 26, 75, 550+20)
        ansBText = textDisplayLeft.TextDisplayLeft(
            "answer B", 26, 75, 550+20+63*1)
        ansCText = textDisplayLeft.TextDisplayLeft(
            "answer C", 26, 75, 550+20+63*2)
        ansDText = textDisplayLeft.TextDisplayLeft(
            "answer D", 26, 75, 550+20+63*3)

        # create text for each player to display scores
        nameTextArray = []
        scoreTextArray = []
        for x in range(len(game.players)):
            nameTextArray.append(textDisplay.TextDisplay(
                game.players[x].name, 26, self.width/2, self.height - 810 + 70*x))
            scoreTextArray.append(textDisplay.TextDisplay(
                str(game.players[x].score), 26, self.width/2, self.height - 780 + 70*x))
        refresh_current_player_indicator()

        # self.screen.blit(self.background, (0, 0))
        board = jeopardyBoard.JeopardyBoard()
        myWheel = wheel.Wheel()

        # buttons
        game_completed_button = button.Button(
            "GAME COMPLETED", 32, self.width*(1 - 1/8), self.height - 50)
        quit_to_main_button = button.Button(
            "QUIT TO MAIN", 32, self.width/10, self.height - 50)
        spin_button = button.Button(
            "SPIN", 46, 1250, 680)

        # create array full of answer buttons from A to D
        answerButtonArray = [button.Button(
            "a", 48, 975, 580, False), button.Button(
            "b", 48, 975, 645, False), button.Button(
            "c", 48, 975, 710, False), button.Button(
            "d", 48, 975, 775, False)]

        show_spin = True
        loop = True
        while loop:

            # draw elements
            self.screen.blit(self.background, (0, 0))
            game_completed_button.draw(self.screen)
            quit_to_main_button.draw(self.screen)

            for x in range(0, 4):
                answerButtonArray[x].draw(self.screen)

            wheelText.draw(self.screen)
            spinCountText.draw(self.screen)
            spinCountNum.draw(self.screen)
            narration.draw(self.screen)
            board.draw(self.screen, self.categories)
            ansAText.draw(self.screen)
            ansBText.draw(self.screen)
            ansCText.draw(self.screen)
            ansDText.draw(self.screen)
            questionText.draw(self.screen)

            # Draw wheel
            myWheel.draw(self.screen)

            # draw player names/scores
            for x in nameTextArray:
                x.draw(self.screen)
            for x in scoreTextArray:
                x.draw(self.screen)

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

                # answer selection handlers
                for x in range(0, 4):
                    if answerButtonArray[x].clicked:
                        if x == game.correctAnswer:
                            game.players[game.current_player].add_score(
                                game.current_question_value)
                            board.removeSquare(
                                self.screen, spin_result, game.get_question_index(spin_result))
                            # set all answer buttons to unclickable
                            for x in range(0, 4):
                                answerButtonArray[x].setClickable(False)
                            # set the spin button to clickable
                            spin_button.setClickable(True)
                        else:
                            # prevent incorrect answer from being selected twice
                            answerButtonArray[x].setClickable(False)
                            game.players[game.current_player].sub_score(
                                game.current_question_value)
                            game.next_player()
                        refresh_current_player_score()
                        refresh_current_player_indicator()

                # other handlers
                # ...
                if spin_button.clicked:
                    # set the spin button to unclickable
                    spin_button.setClickable(False)
                    # attribute = angle in degrees
                    myWheel.spin(self.screen, 360)
                    spin_result = game.spin()
                    game.spins_left -= 1
                    wheelText.setText(str(spin_result))
                    spinCountNum.setText(str(game.spins_left))
                    print(spin_result)

                    # game logic
                    if type(spin_result) == str:
                        if spin_result == 'lose turn':
                            game.next_player()
                            print(game.current_player)
                            spin_button.setClickable(True)
                        elif spin_result == 'free turn':
                            game.players[game.current_player].add_token()
                            narration.setText(
                                "Player " + str(game.current_player + 1) + " gets a free turn.")
                            spin_button.setClickable(True)
                        elif spin_result == 'bankrupt':
                            game.players[game.current_player].zero_score()
                            refresh_current_player_score()
                            print(str(game.players[game.current_player].score))
                            game.next_player()
                            spin_button.setClickable(True)
                        elif spin_result == 'player\'s choice':
                            spin_button.setClickable(True)
                            pass
                        elif spin_result == "opponent's choice":
                            spin_button.setClickable(True)
                            pass
                        elif spin_result == "spin again":
                            spin_button.setClickable(True)
                            pass
                        refresh_current_player_score()
                        refresh_current_player_indicator()

                    else:  # spin result  is a category number

                        question = game.get_category_next_question(spin_result)
                        if question != None:
                            questionText.setText(question[0])
                            ansAText.setText(question[1])
                            ansBText.setText(question[2])
                            ansCText.setText(question[3])
                            ansDText.setText(question[4])
                            # set the four answer buttons to clickable
                            for x in range(0, 4):
                                answerButtonArray[x].setClickable(True)
                        else:
                            questionText.setText("Category empty, Spin again!")
                            ansAText.setText("")
                            ansBText.setText("")
                            ansCText.setText("")
                            ansDText.setText("")
                        refresh_current_player_score()
                        refresh_current_player_indicator()

            # update the game state
            pygame.display.update()
            self.clock.tick(60)
