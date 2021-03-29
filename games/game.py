from flask import Flask

game = Flask(__name__)

from controllers import controller

if __name__ == '__main__':
    game.run(debug=True)