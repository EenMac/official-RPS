from game import game
from flask import render_template
from models.player_class import Player
from models.game_class import Game

@game.route('/')
def home():
    return 'Welcome: lets play a game'

# @game.route('/engage')
# def engage():
#     return render_template('index.html', title = "Lets play a little game", game_actions=game_actions)

@game.route('/<choice1>/<choice2>')
def get_result(choice1, choice2):
    player1 = Player("Player 1", choice1)
    player2 = Player("Player 2", choice2) 
    game = Game(player1, player2)
    champion = game.get_result()
    return render_template('index.html', player1 = player1, player2 = player2, champion = champion)


    # champion = game.get_result()
    # return render_template('index.html', player1 == str(f"Player 1 chose: {choice1}"), player2 == (f"Player 2 chose: {choice2}), result = (f"The winner is {champion}")