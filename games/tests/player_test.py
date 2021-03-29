import unittest 
from models.player_class import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("player1", "scissors")
    

    def test_player_has_name(self):
        self.assertEqual("player1", self.player.name)

    def test_player_has_choice(self):
        self.assertEqual("scissors", self.player.choice)
    

