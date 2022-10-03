import random


class Hangman:
    """
    class of hangman game, have all of basic attributes we need for hangman
    """

    def __init__(self, idx):
        """
        initialize all the attributes
        """
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = random.choice(self.possible_words)
        self.well_guessed_letters = "_" * len(self.word_to_find)  # list user can see
        self.bad_guessed_letter = []
        self.turn_count = 0
        self.error_count = 0
        self.lives = 5

    def play(self):
        self.turn_count += 1
        letter = input("please enter a single letter: ")
        if len(letter) == 1 and letter.isalpha():  # have correct letter input
            if letter in self.word_to_find:
                location = [i for i, guess_letter in enumerate(self.word_to_find) if guess_letter == letter]
                for idx in location:
                    self.word_to_find[idx] = letter  # have guessed letter in the list
                    self.well_guessed_letters = "".join(self.word_to_find)
                    return self.well_guessed_letters

            else:
                self.bad_guessed_letter.append(letter)
                self.lives -= 1
                self.error_count += 1
                print("you have bad guess, letters are not correct")
        else:
            print("not a valid letter")

    def well_played(self):
        """
        will be called when player got all letter correct
        """
        print(f"{self.well_guessed_letters} in {self.turn_count} turns with {self.error_count}errors!")

    @staticmethod
    def game_over():
        """
        will be called when game is over
        """
        print("game over...")

    def start_game(self):
        """
        to start the game
        """
        while self.lives > 0 or "_" in self.well_guessed_letters:
            self.play()
        if self.lives == 0:
            self.game_over()
        else:
            if "_" not in self.well_guessed_letters:
                self.well_played()
        print(
            f"well guessed letters: {self.well_guessed_letters}, bad guessed letters: {self.bad_guessed_letter}, life: {self.lives}, error count: {self.error_count}, turn count: {self.turn_count}")
