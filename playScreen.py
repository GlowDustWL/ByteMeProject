# play screen class
import pygame
import button
import pygame.gfxdraw
import MainDriver
import textDisplay
import textTitle
import jeopardyBoard
import wheel
import random
from flattenList import flattenList
import textDisplayLeft
import textDisplayQuestionWrap


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
        self.finalScores = []

        # self.game = MainDriver.Game()

    # main menu

    def getInput(self, numPlayers, playerList):
        def refresh_all_player_score():
            for x in range(len(game.players)):
                scoreTextArray[x].setText(
                    str(game.players[x].score))
                self.finalScores[x] = game.players[x].score

        def refresh_current_player_indicator():
            for x in range(len(game.players)):
                nameTextArray[x].setText(
                    game.players[x].name + " (" + str(game.players[x].free_token) + ")")
            nameTextArray[game.current_player].setText(
                "->"+nameTextArray[game.current_player].text_input+"<-")

        def randomly_assign_answers():
            tmp_list = [i for i in range(1, 5)]
            random.shuffle(tmp_list)
            game.correctAnswer = tmp_list.index(1)
            ansAText.setText(question[tmp_list[0]])
            ansBText.setText(question[tmp_list[1]])
            ansCText.setText(question[tmp_list[2]])
            ansDText.setText(question[tmp_list[3]])

        show_decision = False
        clickable_mem = []

        def wait_for_player_decision():
            nonlocal show_decision
            show_decision = True
            for x in range(0, 4):
                clickable_mem.append(answerButtonArray[x].clickable)
                answerButtonArray[x].setClickable(False)
            clickable_mem.append(spin_button.clickable)
            spin_button.setClickable(False)

        def player_decision_resolved():
            nonlocal show_decision
            show_decision = False
            for x in range(0, 4):
                answerButtonArray[x].setClickable(clickable_mem[x])
            spin_button.setClickable(clickable_mem[4])
            clickable_mem.clear()
            # force set clicked to false
            no_button.clicked = False
            yes_button.clicked = False
            refresh_all_player_score()
            refresh_current_player_indicator()

        def give_all_player_tokens():
            for x in range(len(game.players)):
                game.players[x].add_token()

        # initialize game instance
        game = MainDriver.Game(numPlayers, playerList)

        # set up final score array
        for x in range(len(game.players)):
            self.finalScores.append(0)

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
            50, 480, 870, 90),  2, 3)  # status/ user promp
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            50, 585, 1000, 240),  2, 3)  # questions / answers
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            1060, 587, 50, 50),  2, 3)  # asnwer question button: A
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            1060, 650, 50, 50),  2, 3)  # asnwer question button: B
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            1060, 712, 50, 50),  2, 3)  # asnwer question button: C
        pygame.draw.rect(self.background, self.box_color, pygame.Rect(
            1060, 773, 50, 50),  2, 3)  # asnwer question button: D
        # pygame.draw.rect(self.background, self.box_color, pygame.Rect(
        #     1150, 652, 200, 50),  2, 3)  # Spin The Wheel !
        # pygame.gfxdraw.rectangle(self.background, pygame.Rect(
        #     50, 50, 600, 400), self.box_color)

        # drawing text
        wheelText = textDisplay.TextDisplay(
            "", 46, 1320, 780)
        spinCountText = textDisplay.TextDisplay(
            "Spins left: ", 26, 150, 425)
        spinCountNum = textDisplay.TextDisplay(
            str(game.spins_left), 26, 230, 425)
        narration = textDisplay.TextDisplay(
            "Press \"SPIN\" to spin the wheel.", 26, 1340, 677)

        # Questions/Answer Display
        questionText = textDisplayQuestionWrap.Pane("No question to answer yet",
                                                    32, 870, 90, 480, 507)
        ansAText = textDisplayLeft.TextDisplayLeft(
            "answer A", 26, 75, 585+12)
        ansBText = textDisplayLeft.TextDisplayLeft(
            "answer B", 26, 75, 585+12+63*1)
        ansCText = textDisplayLeft.TextDisplayLeft(
            "answer C", 26, 75, 585+12+63*2)
        ansDText = textDisplayLeft.TextDisplayLeft(
            "answer D", 26, 75, 585+12+63*3)

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
            "SPIN", 50, 1320, 727)
        yes_button = button.Button(
            "Yes", 50, 1120, 527)
        no_button = button.Button(
            "No", 50, 1520, 527)

        # create array full of answer buttons from A to D
        answerButtonArray = [button.Button(
            "a", 48, 1085, 587 + 22.5, False), button.Button(
            "b", 48, 1085, 677, False), button.Button(
            "c", 48, 1085, 735.5, False), button.Button(
            "d", 48, 1085, 800.5, False)]

        # DEBUG
        give_all_player_tokens()

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

            if show_decision:
                narration.setText(
                    "Do you want to use a free turn token?")
                yes_button.draw(self.screen)
                no_button.draw(self.screen)

            # round 2 logic
            if game.spins_left <= 0 or game.board_empty:
                # reload board
                # todo: use different questions
                game.read_database_two()
                game.current_round += 1
                game.spins_left = game.spin_total
                game.board_empty = False
                # todo: reload the whole jeopardy board
                spinCountNum.setText(str(game.spins_left))
                # todo: change active player to 0 but only after current turn is done

            if game.current_round > 2:
                # TODO: complete game and load final score board screen
                pass

            spun = False

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
                    if answerButtonArray[x].clicked and isinstance(spin_result, int):
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
                            narration.setText(
                                "Press \"SPIN\" to spin the wheel.")
                        else:
                            # prevent incorrect answer from being selected twice
                            answerButtonArray[x].setClickable(False)
                            game.players[game.current_player].sub_score(
                                game.current_question_value)
                            if game.players[game.current_player].free_token > 0:
                                wait_for_player_decision()
                            else:
                                game.next_player()
                        refresh_all_player_score()
                        refresh_current_player_indicator()

                # other handlers
                # ...

                if show_decision:
                    if yes_button.clicked:
                        game.players[game.current_player].free_token -= 1
                        narration.setText(
                            game.players[game.current_player].name + " uses a free turn token.")
                        player_decision_resolved()
                    if no_button.clicked:
                        game.next_player()
                        narration.setText(
                            game.players[game.current_player].name + "'s turn.")
                        player_decision_resolved()

                if spin_button.clicked:
                    # spun = True
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
                            spin_button.setClickable(True)
                            if game.players[game.current_player].free_token > 0:
                                wait_for_player_decision()
                            else:
                                game.next_player()
                            print(game.current_player)
                        elif spin_result == 'free turn':
                            game.players[game.current_player].add_token()
                            narration.setText(
                                game.players[game.current_player].name + " gets a free turn token.")
                        elif spin_result == 'bankrupt':
                            game.players[game.current_player].zero_score()
                            # refresh_all_player_score()
                            print(str(game.players[game.current_player].score))
                            game.next_player()
                        elif spin_result == 'player\'s choice':
                            pass
                        elif spin_result == "opponent's choice":
                            pass
                        elif spin_result == "spin again":
                            pass
                        spin_button.setClickable(True)
                        narration.setText("Press \"SPIN\" to spin the wheel.")
                        refresh_all_player_score()
                        refresh_current_player_indicator()

                    else:  # spin result  is a category number

                        question = game.get_category_next_question(spin_result)
                        if question != None:
                            questionText.addText(question[0])
                            randomly_assign_answers()
                            # set the four answer buttons to clickable
                            for x in range(0, 4):
                                answerButtonArray[x].setClickable(True)
                        else:
                            questionText.addText("Category empty, Spin again!")
                            ansAText.setText("")
                            ansBText.setText("")
                            ansCText.setText("")
                            ansDText.setText("")
                            spin_button.setClickable(True)
                            narration.setText(
                                "Press \"SPIN\" to spin the wheel.")

                        refresh_all_player_score()
                        refresh_current_player_indicator()

                    spin_button.clicked = False

            # update the game state
            pygame.display.update()
            self.clock.tick(60)
