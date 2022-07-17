class Player():
    def __init__(self, player_name):
        self.name = player_name
        self.score = 0

    def get_name(self):
        print(self.name)
        return self.name

    def get_score(self):
        print(self.score)
        return self.score

    def add_score(self, points):
        self.score += points

    def sub_score(self, points):
        self.score -= points

    def zero_score(self):
        self.score = 0
