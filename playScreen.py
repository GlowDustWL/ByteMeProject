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

    def getInput(self, numPlayers):
        # initialize game instance
        game = MainDriver.Game(numPlayers)

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

        # self.screen.blit(self.background, (0, 0))
        board = jeopardyBoard.JeopardyBoard()
        myWheel = wheel.Wheel()

        show_spin = True
        loop = True
        while loop:

            # buttons
            game_completed_button = button.Button(
                "GAME COMPLETED", 32, self.width*(1 - 1/8), self.height - 50)
            quit_to_main_button = button.Button(
                "QUIT TO MAIN", 32, self.width/10, self.height - 50)
            spin_button = button.Button(
                "SPIN", 46, 1250, 680)

            # draw elements
            self.screen.blit(self.background, (0, 0))
            game_completed_button.draw(self.screen)
            quit_to_main_button.draw(self.screen)
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

            # Jeopardy board highlight/removal examples
            # # Remove squares from board, grid layout zero-indexed, test example
            # x_remove = 0
            # y_remove = 3
            # board.removeSquare(self.screen, x_remove, y_remove)
            # # Highlight squares from board, grid layout zero-indexed, test example
            # x_highlight = 2
            # y_highlight = 0
            # board.highlightSquare(self.screen, x_highlight, y_highlight)

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

                # other handlers
                # ...
                if spin_button.clicked:
                    spin_result = game.spin()
                    game.spins_left -= 1
                    wheelText.setText(str(spin_result))
                    spinCountNum.setText(str(game.spins_left))
                    # show_spin = False
                    game.players[0].add_score(500)
                    scoreTextArray[0].setText(str(game.players[0].score))
                    print(spin_result)

                    # game logic
                    if type(spin_result) == str:
                        if spin_result == 'lose turn':
                            game.next_player()
                            print(game.current_player)
                        elif spin_result == 'free turn':
                            game.players[game.current_player].add_token()
                            narration.setText(
                                "Player " + str(game.current_player + 1) + " gets a free turn.")
                        elif spin_result == 'bankrupt':
                            game.players[game.current_player].zero_score()
                            print(str(game.players[game.current_player].score))
                        elif spin_result == 'player\'s choice':
                            pass
                    else:  # spin result  is a category number
                        questionText.setText(game.questions[spin_result][1][0])
                        ansAText.setText(game.questions[spin_result][1][1])
                        ansBText.setText(game.questions[spin_result][1][2])
                        ansCText.setText(game.questions[spin_result][1][3])
                        ansDText.setText(game.questions[spin_result][1][4])

                        # update the game state
            pygame.display.update()
            self.clock.tick(60)
