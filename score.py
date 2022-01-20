class Score:
    def __init__(self):
        self.best_score = None
        self.score = 0
        self.load_previous_score()

    def load_previous_score(self):
        try:
            with open('score.txt', 'r') as f:
                self.best_score = int(f.read())
        except FileNotFoundError:
            self.best_score = 0

    def save_score(self):
        with open('score.txt', 'w') as f:
            f.write(str(self.best_score))
