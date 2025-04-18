import unittest
from game_state import GameState

class TestGameState(unittest.TestCase):

    def setUp(self):
        self.state = GameState("apple")

    #Vérifie que faire une tentative valide diminue le nombre de tentatives restantes
    def test_valid_guess_reduces_attempts(self):
        self.state.make_guess("crane")
        self.assertEqual(self.state.remaining_attempts, 5)

    #Vérifie que si on trouve le mot, le jeu est gagné et terminé
    def test_win_condition(self):
        self.state.make_guess("apple")
        self.assertTrue(self.state.is_winner) # Le joueur a gagné
        self.assertTrue(self.state.is_over) # La partie est terminée

    #Vérifie que si on rate les 6 essais, on perd et la partie est finie
    def test_lose_condition(self):
        for _ in range(6):
            self.state.make_guess("crane")
        self.assertFalse(self.state.is_winner)
        self.assertTrue(self.state.is_over)

    #Vérifie que l'historique des tentatives contient bien les mots joués
    def test_guess_history(self):
        self.state.make_guess("crane")
        self.assertEqual(len(self.state.history), 1)
        self.assertEqual(self.state.history[0][0], "crane")

    #Vérifie qu'on ne peut pas rejouer après que la partie est finie
    def test_guess_after_game_over_raises(self):
        for _ in range(6):
            self.state.make_guess("crane")
        with self.assertRaises(Exception):
            self.state.make_guess("crane")

    #Vérifie qu'un mot invalide (caractères non alphabétiques) lève une erreur
    def test_invalid_word_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.state.make_guess("12ab3")

if __name__ == '__main__':
    unittest.main()
