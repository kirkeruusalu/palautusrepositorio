import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsstats(unittest.TestCase):
    def setUp(self):
        # annetaan Statisticsstats-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_player_found(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")
    
    def test_search_player_not_found(self):
        player = self.stats.search("Nonexistent Player")
        self.assertIsNone(player)

    def test_team_players_found(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
        self.assertEqual(team_players[0].name, "Semenko")
        self.assertEqual(team_players[1].name, "Kurri")
        self.assertEqual(team_players[2].name, "Gretzky")


    def test_team_no_players(self):
        team_players = self.stats.team("FIC")
        self.assertEqual(len(team_players), 0)

    def test_top_scorers(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")
    
if __name__ == "__main__":
    unittest.main()

    