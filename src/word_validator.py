VALID_WORDS = [
    "apple", "crane", "reach", "plant", "apply", "grape", "flame", "chair", "trace", "glide"
]

# Définition de la classe responsable de la validation des mots
class WordValidator:
    def __init__(self):
     self.valid_words = VALID_WORDS

    # Méthode principale de validation
    def validate_word(self, word):
        # Vérifie si l'entrée est une chaîne de caractères
        if not isinstance(word, str):
            return False
        
        # Vérifie que le mot contient exactement 5 lettres
        if len(word) != 5:
            return False
        
        # Vérifie que le mot ne contient que des lettres alphabétiques
        if not word.isalpha():
            return False

        # Si toutes les conditions sont remplies, le mot est valide
        return True
