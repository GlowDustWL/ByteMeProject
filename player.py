class Player():
    def __init__(self, player_name):
        print("[LOG]: Player instance created.")
        self.name = player_name
        self.score = 0
        self.free_token = 0

    def get_name(self):
        print("[LOG]: Player.get_name called.")
        return self.name

    def get_score(self):
        print("[LOG]: Player.get_score called.")
        return self.score

    def add_score(self, points):
        print("[LOG]: Player.add_score called.")
        self.score += points

    def sub_score(self, points):
        print("[LOG]: Player.sub_score called.")
        self.score -= points

    def zero_score(self):
        print("[LOG]: Player.zero_score called.")
        self.score = 0

    def add_token(self):
        print("[LOG]: Player.add_token called.")
        self.free_token += 1
