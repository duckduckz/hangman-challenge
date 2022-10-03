from utils.game import Hangman

class Main(Hangman):
    def __init__(self):
        super().__init__()

    def start_game(self, letter):
        if self.game_over() or self.well_played():
            return self.play()
        elif self.lives == 0:
            return self.game_over()
        elif letter in self.well_guessed_letters:
            return self.well_played()










