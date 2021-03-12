from flask import render_template, request, redirect
from app import app
from app.models.list_of_players import player_1, player_2
from app.models.player import Player

@app.route('/index')
def index():
    return render_template(
        'index.html', 
        title="Rock, Paper, Scissors!", 
        player_1=player_1, 
        player_2=player_2
    )

@app.route('index/rock/rock')
def rock_rock():
    return "Draw!"

@app.route('index/rock/paper')
def rock_paper():
    return "P2 wins!"

@app.route('index/rock/scissors')
def rock_scissors():
    return "P1 wins!"

@app.route('index/paper/rock')
def paper_rock():
    return "P1 wins!"

@app.route('index/paper/paper')
def paper_paper():
    return "Draw!"

@app.route('index/paper/scissors')
def paper_scissors():
    return "P1 wins!"

@app.route('index/scissors/rock')
def scissors_rock():
    return "P2 wins!"

@app.route('index/scissors/paper')
def scissors_paper():
    return "P1 wins!"

@app.route('index/scissors/scissors')
def scissors_scissors():
    return "Draw!"