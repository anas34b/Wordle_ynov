import unittest
from word_validator import WordValidator


class TestWordValidator(unittest.TestCase):

    # Méthode exécutée avant chaque test → création d'une instance de WordValidator
    def setUp(self):
        self.validator = WordValidator()

    # Test d’un mot valide
    def test_valid_word(self):
        self.assertTrue(self.validator.validate_word("apple"))

    # Test d’un mot trop court
    def test_too_short_word(self):
        self.assertFalse(self.validator.validate_word("cat"))

    # Test d’un mot trop long
    def test_too_long_word(self):
        self.assertFalse(self.validator.validate_word("banana"))

    # Test d’un mot avec des chiffres
    def test_non_alpha_word(self):
        self.assertFalse(self.validator.validate_word("he11o"))

    # Test d’une entrée int
    def test_non_string_input(self):
        self.assertFalse(self.validator.validate_word(12345))


# Point d'entrée du fichier pour exécuter les tests si on le lance directement
if __name__ == '__main__':
    unittest.main()
