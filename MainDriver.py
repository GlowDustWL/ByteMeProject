import random
import sys


class Game:
    def __init__(self, spins=50):
        # internal question & answers data structure. 2D array, [category][value]
        # each 4 string List in a cell consist of: question, correct answer, 2 wrong answers
        self.questions = [
            [['Question', 'Correct', 'Incorrect 1', 'Incorrect 2'] for i in range(5)] for j in range(6)]
        self.current_round = 1
        self.spin_total = spins
        self.spins_left = spins
        self.current_player = 1
        self.total_player = 2  # todo: increase later, allow parameter

    # read database for questions & answers to populate internal data structures
    def read_database(self):
        pass

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
        if self.current_player < self.total_player:
            self.current_player += 1
        else:
            self.current_player = 1

    def get_category_next_question(self, category_index):
        return self.questions[category_index].pop(0)

    def question_sequence(self, category):
        # check if empty
        if len(self.questions[category]) == 0:
            print("Category is empty! Spin Again!")
            return
        if not self.question_prompt(
                self.get_category_next_question(category)):
            self.next_player()

    def question_prompt(self, question_item):
        # todo: add randomness
        # todo: add player class integration
        print(question_item[0])
        print("1. " + question_item[1])
        print("2. " + question_item[2])
        print("3. " + question_item[3])
        answer = int(input("Select the answer (1-3):"))
        if answer == 1:
            print("You are correct!")
            return True
        else:
            print("You are incorrect.")
            return False

    # run playable demo
    def demo(self):
        # TODO: integrate with player class once player class is setup
        print("Welcome to Wheel of Jeopardy!")
        while self.current_round <= 2:
            print("==========")
            print("This is round " + str(self.current_round))
            print(str(self.spins_left) + " spins remaining!")
            print("Player " + str(self.current_player) + "'s turn")
            input("Press Enter to spin...")
            self.spins_left -= 1
            spin_result = self.spin()
            if type(spin_result) == str:
                print("The wheel landed on... " + spin_result + "!")
                if spin_result == 'lose turn':
                    self.next_player()
                elif spin_result == 'free turn':
                    # todo: add free turn token to player class instance
                    pass
                elif spin_result == 'bankrupt':
                    # todo: remove all points from player class instance
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
            if self.spins_left <= 0:
                print("Round " + str(self.current_round) + " over!")
                self.current_round += 1
                self.spins_left = self.spin_total
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
