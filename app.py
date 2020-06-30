from flask import Flask, request, render_template, url_for
from datetime import datetime
import math

from game import Game

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return f"""
    <h1>Hello heroku</h1>
    <p>It is currently {the_time}.</p>
    <img src="http://loremflickr.com/600/400" />
    <p><h1> <a href="{ url_for('game_') }"> Play Game </a></h1></p>
    """


@app.route('/game', methods=['GET', 'POST'])
def game_():
    game = Game()
    game.play()

    color_code={
        1: 'yellow',
        2: 'red',
        3: 'blue',
        4: 'rgb(255,255,255)',
        5: 'SeaGreen',
        6: 'LightSlateGrey',
    }

    code = (game.codemaker.code)
    moves = (game.moves)
    feedbacks = (game.feedback)
    log = game.log.split('\n')


    return render_template('game.html', color=color_code, code=code, moves=moves, feedbacks=feedbacks, winner=game.winner, log=log)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
