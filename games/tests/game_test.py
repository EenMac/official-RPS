import unittest
from models.game_class import Game
from models.player_class import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("andy", "rock")
        self.player2 = Player("iain", "scissors") 
        self.game = Game(self.player1, self.player2)
        


    def test_Game_has_players(self):
        self.assertEqual("andy", self.game.player1.name)
    def test_game_has_player2(self):
        self.assertEqual("iain", self.game.player2.name)
    def test_player_can_win(self):
        self.assertEqual("Player 1 wins", self.game.get_result())
    # def test_player_can_win_different_hands(self):
    #     self.player1.choice == "paper"
    #     self.player2.choice == "scissors"
    #     self.assertEqual("Player 2 wins", self.game.get_result())
    # def test_player_cant_lose(self):
    #     self.player1 = Player("chris", "paper")
    #     self.player2 = Player("Steve", "scissors")
    #     self.assertEqual("Player 2 wins", self.game.get_result())





    