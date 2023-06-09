from flask import Flask, render_template, url_for, jsonify, request
from logic import Easy, Medium, Hard

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/move", methods=['POST'])
def move():
    state = request.get_json()
    difficulty = state.get("difficulty")

    if (difficulty == 0):
        game = Easy()
    elif (difficulty == 1):
        game = Medium()
    else:
        game = Hard()
    
    game.board = state.get("board")
    game.player = state.get("player")
    game.computer = state.get("computer")

    move = game.calculate_move()

    return jsonify(computerMove = move)

if __name__== "__main__":
    app.run()
 