# 🎮 Wordle - Console

Ce projet est un jeu **Wordle** développée en Python.

---

## 🧠 Objectif du jeu

Devinez un mot de 5 lettres en **6 tentatives maximum**.  
À chaque essai, vous obtenez un retour visuel :

- 🟩 Lettre correcte à la **bonne position**
- 🟨 Lettre correcte à la **mauvaise position**
- ⬜ Lettre **absente** du mot

---

## ✅ Fonctionnalités principales

- Mot cible sélectionné **aléatoirement** depuis une liste de mots valides
- Affichage en couleurs via symboles (🟩, 🟨, ⬜)
- Validation des entrées :
  - 5 lettres
  - Alphabetique uniquement
- Suivi des parties jouées :
  - Nombre de parties
  - Nombre de victoires
  - Nombre d’échecs
- Possibilité de **réinitialiser les statistiques** au lancement

---

## 🔧 Technologies

- Python 3.10+
- `unittest` (tests unitaires)
- `coverage` (rapport de couverture)

---

## 📁 Structure du projet

```
Wordle_ynov/
│
├── src/
│   ├── game_logic.py           # Logique de comparaison (🟩 🟨 ⬜)
│   ├── game_state.py           # Gestion du jeu (tentatives, victoire, etc.)
│   ├── word_validator.py       # Validation des mots (format uniquement)
│   ├── stats_manager.py        # Gestion des statistiques
│   ├── test_game_logic.py      # Tests unitaires de la logique
│   ├── test_game_state.py      # Tests unitaires du GameState
│   ├── test_word_validator.py  # Tests unitaires du validateur
│   └── test_stats_manager.py   # Tests unitaires du système de stats
│
├── play.py                     # Lancement du jeu
├── stats.json                  # Fichier généré automatiquement (statistiques)
└── README.md                   # Ce fichier
```

---

## ▶️ Comment lancer le jeu

```bash
python play.py
```

ℹ️ Au démarrage, il est possible de **réinitialiser les stats** en appuyant sur `y`.

---

## 🧪 Exécuter les tests

```bash
python -m coverage run --source=src test_all.py
```

---

## 📊 Couverture des tests

Pour obtenir le rapport de couverture :

```bash
python -m coverage report
```

Exemple de sortie :
```
Name                    Stmts   Miss  Cover
-------------------------------------------
src/game_logic.py          13      0   100%
src/game_state.py          27      0   100%
src/stats_manager.py       25      0   100%
src/word_validator.py      12      0   100%
-------------------------------------------
TOTAL                      77      0   100%
```

---

## 🧠 Auteur

- **Anas Daoui**
