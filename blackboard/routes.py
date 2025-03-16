from flask import render_template
from blackboard import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/board/<int:board_id>')
def board(board_id):
    return render_template('board.html', board_id=board_id)