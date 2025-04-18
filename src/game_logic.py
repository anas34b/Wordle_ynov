class GameLogic:
    
    # Méthode qui compare un mot proposé avec le mot cible
    def check_guess(self, guess, target_word):
        result = ['⬜'] * 5  # Initialisation : toutes les lettres sont grises
        target_word_chars = list(target_word)  # Liste de lettres du mot cible

        # 1ère passe : vérifier les lettres bien placées (🟩)
        for i in range(5):
            if guess[i] == target_word[i]:
                result[i] = '🟩'
                target_word_chars[i] = None  # Marquer la lettre comme utilisée (évite de la re-compter)

        # 2ème passe : vérifier les lettres correctes mal placées (🟨)
        for i in range(5):
            if result[i] == '⬜' and guess[i] in target_word_chars:
                result[i] = '🟨'
                target_word_chars[target_word_chars.index(guess[i])] = None  # Marquer comme utilisée

        return result
