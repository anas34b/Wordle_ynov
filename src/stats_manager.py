import json
import os

STATS_FILE = "stats.json"

class StatsManager:
    def __init__(self):
        self.stats = {
            "games": 0,
            "wins": 0,
            "streak": 0,
            "total_attempts": 0,
            "fails": 0

        }
        self._load()

    def _load(self):
        if os.path.exists(STATS_FILE):
            with open(STATS_FILE, "r") as f:
                self.stats = json.load(f)

    def _save(self):
        with open(STATS_FILE, "w") as f:
            json.dump(self.stats, f, indent=4)

    def record_game(self, won, attempts_used):
     self.stats["games"] += 1
     self.stats["total_attempts"] += attempts_used

     if won:
        self.stats["wins"] += 1
        self.stats["streak"] += 1
     else:
        self.stats["fails"] += 1
        self.stats["streak"] = 0

     self._save()



    def get_stats(self):
     return {
        "games": self.stats["games"],
        "wins": self.stats["wins"],
        "fails": self.stats["fails"],
     }

