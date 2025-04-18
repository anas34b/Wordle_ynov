from game_logic import GameLogic
from word_validator import WordValidator

class GameState:
    def __init__(self, target_word, max_attempts=6):
        self.target_word = target_word.lower()
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts
        self.history = []
        self.is_over = False
        self.is_winner = False
        self.validator = WordValidator()
        self.logic = GameLogic()

    def make_guess(self, guess):
        if self.is_over:
            raise Exception("La partie est terminée.")
        
        if not self.validator.validate_word(guess):
            raise ValueError("Format invalide (5 lettres alphabétiques requises)")

        guess = guess.lower()
        result = self.logic.check_guess(guess, self.target_word)
        self.history.append((guess, result))
        self.remaining_attempts -= 1

        if guess == self.target_word:
            self.is_winner = True
            self.is_over = True
        elif self.remaining_attempts == 0:
            self.is_over = True

        return result
