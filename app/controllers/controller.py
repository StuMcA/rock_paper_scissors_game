from flask import render_template, request, redirect
from app import app
from app.models.list_of_players import player_1, player_2, set_choices
from app.models.player import Player

@app.route('/game')
def index():
    return render_template(
        'index.html', 
        title="Rock, Paper, Scissors!", 
        player_1=player_1, 
        player_2=player_2
    )

@app.route('/game/fight', methods=['POST'])
def fight():
    p1_choice = request.form['p1_choice']
    p2_choice = request.form['p2_choice']
    set_choices(p1_choice, p2_choice)
    return redirect(f"/game/{player_1.choice}/{player_2.choice}")

@app.route('/game/rock/rock')
def rock_rock():
    return "Draw!"

@app.route('/game/rock/paper')
def rock_paper():
    return "P2 wins!"

@app.route('/game/rock/scissors')
def rock_scissors():
    return "P1 wins!"

@app.route('/game/paper/rock')
def paper_rock():
    return "P1 wins!"

@app.route('/game/paper/paper')
def paper_paper():
    return "Draw!"

@app.route('/game/paper/scissors')
def paper_scissors():
    return "P1 wins!"

@app.route('/game/scissors/rock')
def scissors_rock():
    return "P2 wins!"

@app.route('/game/scissors/paper')
def scissors_paper():
    return "P1 wins!"

@app.route('/game/scissors/scissors')
def scissors_scissors():
    return "Draw!"