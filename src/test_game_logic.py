import unittest
from game_logic import GameLogic

class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.logic = GameLogic()

    # Test : tous les caractères correspondent exactement
    def test_exact_match(self):
        self.assertEqual(self.logic.check_guess("apple", "apple"), ['🟩', '🟩', '🟩', '🟩', '🟩'])

    # Test : aucun caractère ne correspond
    def test_no_match(self):
        self.assertEqual(self.logic.check_guess("crane", "sloth"), ['⬜', '⬜', '⬜', '⬜', '⬜'])

    # Test : quelques lettres sont présentes mais mal placées
    def test_partial_match(self):
        self.assertEqual(self.logic.check_guess("crane", "reach"), ['🟨', '🟨', '🟩', '⬜', '🟨'])
    
    # Test : quelques lettres sont exactement placées et d'autres ne correspond pas
    def test_duplicate_letters(self):
        self.assertEqual(self.logic.check_guess("piano", "plant"), ['🟩', '⬜', '🟩', '🟩', '⬜'])

# Exécution des tests
if __name__ == '__main__':
    unittest.main()
