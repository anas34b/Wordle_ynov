import unittest
import os
import json
from stats_manager import StatsManager

STATS_FILE = "stats.json"

class TestStatsManager(unittest.TestCase):

    def setUp(self):
        # Assurer que stats.json est supprimé avant chaque test
        if os.path.exists(STATS_FILE):
            os.remove(STATS_FILE)
        self.manager = StatsManager()

    def test_initial_stats(self):
        stats = self.manager.get_stats()
        self.assertEqual(stats["games"], 0)
        self.assertEqual(stats["wins"], 0)
        self.assertEqual(stats["fails"], 0)

    def test_record_win(self):
        self.manager.record_game(True, 4)
        stats = self.manager.get_stats()
        self.assertEqual(stats["games"], 1)
        self.assertEqual(stats["wins"], 1)
        self.assertEqual(stats["fails"], 0)

    def test_record_fail(self):
        self.manager.record_game(False, 6)
        stats = self.manager.get_stats()
        self.assertEqual(stats["games"], 1)
        self.assertEqual(stats["wins"], 0)
        self.assertEqual(stats["fails"], 1)

    def test_multiple_games(self):
        self.manager.record_game(True, 4)
        self.manager.record_game(True, 3)
        self.manager.record_game(False, 6)
        stats = self.manager.get_stats()
        self.assertEqual(stats["games"], 3)
        self.assertEqual(stats["wins"], 2)
        self.assertEqual(stats["fails"], 1)

if __name__ == "__main__":
    unittest.main()
