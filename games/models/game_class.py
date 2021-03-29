from models.player_class import Player

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    
    def get_result(self):
        if self.player1.choice == "scissors" and self.player2.choice == "rock":
            return "Player 2 wins"
        elif self.player1.choice == "rock" and self.player2.choice == "paper":
            return "Player 2 wins"
        elif self.player1.choice == "paper" and self.player2.choice == "scissors":
            return "Player 2 wins"
        elif self.player1.choice == "scissors" and self.player2.choice == "paper":
            return "Player 1 wins"
        elif self.player1.choice == "rock" and self.player2.choice == "scissors":
            return "Player 1 wins"
        elif self.player1.choice == "paper" and self.player2.choice == "rock":
            return "Player 1 wins"
        else: 
            return None
