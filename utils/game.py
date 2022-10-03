import random

possible_words = ['becode', 'learning', 'mathematics', 'sessions']


class Hangman:

    def __init__(self):
        """
        basic attributes we need for hangman
        """
        self.word_to_find = random.choice(possible_words)
        self.well_guessed_letters = ['_' for letter in self.word_to_find]
        self.turn_count = 0
        self.error_count = 0
        self.lives = 5

    def play(self, letters):
        """
        return the hangman game
        """
        # append input letters in to possible_words
        while self.lives < 5:
            while len(letters) == 1 and letters.isalpha() is False:
                letters = input("please enter a single letter: ")
                # valid letter chosen, add it to word_to_find then converting to letter list
                if letters in self.possible_words:
                    self.word_to_find.append(letters)
                    letter = ' '.join((self.word_to_find, letters))

                    # well_guessed_letter append in the list
                    bad_guessed_letters = []
                    if letter in self.well_guessed_letters:
                        self.well_guessed_letters.append(letter)
                        print(self.well_guessed_letters)
                        return self.well_guessed_letters

                    else:
                        bad_guessed_letters.append(letter)
                        self.error_count += 1
                        self.lives -= 1
                        self.turn_count -= 1
                        print(bad_guessed_letters)

    def well_played(self):
        #if "_" not in self.well_guessed_letters:
        print(f"{self.well_guessed_letters} in {self.turn_count} turns with {self.error_count}errors!")

    def game_over(self):
        while True:
            if self.lives == 0:
                print("game over")


