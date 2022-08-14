import random
import sys
import json
from player import Player


class Game:
    def __init__(self, numPlayers, playerList, spins=10):
        # internal question & answers data structure. 2D array, [category][value]
        # each 4 string List in a cell consist of: question, correct answer, 2 wrong answers
        self.questions = []
        self.correctAnswer = 0
        # self.initialize_dummy_database()
        self.read_database()
        self.current_round = 1  # 1 base
        self.board_empty = False
        self.current_question_value = 0  # value of the current active question
        self.spin_total = spins
        self.spins_left = spins
        self.current_player = 0  # 0 base
        self.total_player = numPlayers
        self.players = []
        # create Player objects for each player
        for i in range(self.total_player):
            # user input name
            if (playerList[i] != "Enter Name Here" and playerList[i] != ""):
                self.players.append(Player(playerList[i]))
            # user did not input name
            else:
                self.players.append(Player("Player " + str(i+1)))

    # read database for questions & answers to populate internal data structures
    def read_database(self):
        f = open("questions.json", "r", encoding='utf8')
        self.questions = json.loads(f.read())

    # read second database for questions & answers to populate internal data structures (again)
    def read_database_two(self):
        f = open("questions2.json", "r", encoding='utf8')
        self.questions = json.loads(f.read())

    # def initialize_dummy_database(self):
    #     f = open("questions.json", "w")
    #     questions = [
    #         [['Question_placeholder?', 'Correct', 'Incorrect 1', 'Incorrect 2'] for i in range(5)] for j in range(6)]
    #     f.write(json.dumps(questions))
    #     f.close

    def is_board_empty(self):
        for i in range(len(self.questions)):
            if len(self.questions[i]) > 1:
                self.board_empty = False
                return False
        self.board_empty = True
        return True

    # Among 18 sector, get a random spin result
    # either string or index num of category
    def spin(self):
        result = random.randint(0, 17)
        sectors = {0: 'lose turn', 1: 'free turn', 2: 'bankrupt',
                   3: "player's choice", 4: "opponent's choice", 5: "spin again"}
        return_val = sectors.get(result, None)
        if return_val != None:
            return return_val
        return result % 6

    def next_player(self):
        if self.current_player < self.total_player - 1:
            self.current_player += 1
        else:
            self.current_player = 0

    def get_category_next_question(self, category_index):
        # category name is always first element
        if len(self.questions[category_index]) == 1:
            return None
        self.current_question_value = self.get_category_value(category_index)

        question = self.questions[category_index].pop(1)
        print('INDEX BEING POPPED = ' + str(category_index))
        # update board_empty flag
        self.is_board_empty()
        return question
        # return self.questions[category_index].pop(1)

    # give the value of the question that just got popped

    def get_category_value(self, category_index):
        value = 1000 - (len(self.questions[category_index]) - 2) * 200
        if self.current_round == 2:
            return value * 2
        return value

    # give the current index of the provided category
    def get_question_index(self, category_index):
        question_index = 5 - len(self.questions[category_index])
        return question_index

    def question_sequence(self, category):
        # check if empty
        if len(self.questions[category]) == 0:
            print("Category is empty! Spin Again!")
            return
        # get score value by checking how many questions remaining in category
        print("Category " + str(category))
        if not self.question_prompt(
                self.get_category_next_question(category), self.get_category_value(category)):
            self.next_player()

    def question_prompt(self, question_item, value):
        # todo: add randomness
        # todo: add player class integration
        print("For a value of " + str(value))
        print(question_item[0])
        print("1. " + question_item[1])
        print("2. " + question_item[2])
        print("3. " + question_item[3])
        answer = int(input("Select the answer (1-3):"))
        if answer == 1:
            print("You are correct!")
            print("[LOG]: Calling Player.add_score")
            self.players[self.current_player].add_score(value)
            print("[LOG]: Calling Player.get_score")
            print("Your new score is: " +
                  str(self.players[self.current_player].get_score()))
            return True
        else:
            print("You are incorrect.")
            print("[LOG]: Calling Player.sub_score")
            self.players[self.current_player].sub_score(value)
            print("[LOG]: Calling Player.get_score")
            print("Your new score is: " +
                  str(self.players[self.current_player].get_score()))
            return False

    # run playable demo
    def demo(self):
        # TODO: integrate with player class once player class is setup
        print("Welcome to Wheel of Jeopardy!")
        while self.current_round <= 2:
            print("==========")
            print("This is round " + str(self.current_round))
            print(str(self.spins_left) + " spins remaining!")
            print("Player " + str(self.current_player + 1) + "'s turn")
            input("Press Enter to spin...")
            self.spins_left -= 1
            spin_result = self.spin()
            if type(spin_result) == str:
                print("The wheel landed on... " + spin_result + "!")
                if spin_result == 'lose turn':
                    self.next_player()
                elif spin_result == 'free turn':
                    print("[LOG]: Calling Player.add_token")
                    self.players[self.current_player].add_token()
                    pass
                elif spin_result == 'bankrupt':
                    print("[LOG]: Calling Player.zero_score")
                    self.players[self.current_player].zero_score()
                    print("[LOG]: Calling Player.get_score")
                    print("Your new score is: " +
                          str(self.players[self.current_player].get_score()))
                    self.next_player()
                elif spin_result == "player's choice":
                    # todo: add error checking
                    selection = int(input("Select a category index (0-5)"))
                    self.question_sequence(selection)
                elif spin_result == "opponent's choice":
                    # todo: add error checking
                    # todo: add switch active player
                    selection = int(input(
                        "Select a category index for your opponent (0-5)"))
                    self.question_sequence(selection)
                elif spin_result == "spin again":
                    # stub for now, need it for graphical update later
                    pass
            else:
                self.question_sequence(spin_result)
            if self.is_board_empty() or self.spins_left <= 0:
                # reload board
                # todo: use different questions
                self.read_database()
                print("Round " + str(self.current_round) + " over!")
                print("The score for all players are...")
                for i in range(self.total_player):
                    print("[LOG]: Calling Player.get_score")
                    print("Player " + str(i) + ": " +
                          str(self.players[i].get_score()))
                self.current_round += 1
                self.spins_left = self.spin_total
        winner = self.players[0]
        for player in self.players:
            if player.get_score() >= winner.get_score():
                winner = player
        print(str(winner.get_name()) + " is the winner!")
        return


def main():
    args = sys.argv[1:]
    if len(args) != 0:
        game = Game(int(args[0]))
    else:
        game = Game()
    game.demo()


if __name__ == "__main__":
    main()
