import sys
import os
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.word_validator import VALID_WORDS
from src.game_state import GameState
from src.stats_manager import StatsManager

# Choix aléatoire d’un mot cible parmi les mots valides
TARGET_WORD = random.choice(VALID_WORDS)

def print_result(result):
    print("Résultat : ", end="")
    for symbol in result:
        print(symbol, end=" ")
    print("\n")

def main():
    game = GameState(target_word=TARGET_WORD)
    if os.path.exists("stats.json"):
     choice = input("🔄 Réinitialiser les stats ? (y/n) : ").strip().lower()
    if choice == "y":
        os.remove("stats.json")
        print("✅ Stats réinitialisées.\n")
    stats = StatsManager()

    print("🎮 Bienvenue dans Wordle Console Edition ! 🎮")
    print("-------------------------------------------------")
    print("🔤 Règles du jeu :")
    print("Tu dois deviner un mot de 5 lettres en 6 tentatives maximum.")
    print("À chaque essai, tu verras un retour en couleurs :")
    print("  🟩 Lettre correcte à la bonne position")
    print("  🟨 Lettre correcte mais mauvaise position")
    print("  ⬜ Lettre absente du mot")
    print("-------------------------------------------------\n")

    while not game.is_over:
        guess = input(f"Tentative ({game.max_attempts - game.remaining_attempts + 1}/6) : ").strip()
        try:
            result = game.make_guess(guess)
            print_result(result)
        except ValueError as ve:
            print("❌", ve)
        except Exception as e:
            print("⚠️", e)
            break

    print("\n🔚 Partie terminée !")
    
    # Calcul du nombre de tentatives valides
    attempts_used = game.max_attempts - game.remaining_attempts
    if attempts_used == 0:
        print("ℹ️ Aucune tentative valide effectuée — stats non mises à jour.")
    else:
        stats.record_game(game.is_winner, attempts_used)

    final_stats = stats.get_stats()
    print("\n📊 Statistiques globales :")
    print(f"Total de parties : {final_stats['games']}")
    print(f"Victoires        : {final_stats['wins']}")
    print(f"Échecs         : {final_stats['fails']}")
    print("\n📜 Historique des tentatives :")
    for i, (guess, result) in enumerate(game.history, 1):
       print(f"Tentative {i} : {guess.upper()} → {' '.join(result)}")
    if game.is_winner:
        print("🎉 Bravo ! Tu as trouvé le mot !")
    else:
        print(f"❌ Tu as perdu.. Le mot était : {game.target_word}, 😢 Dommage")

if __name__ == "__main__":
    main()
