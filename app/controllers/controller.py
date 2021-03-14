from flask import render_template, request, redirect
from app import app
from app.models.list_of_players import player_1, player_2, computer_player, set_choices
from app.models.player import Player
from app.models.game import Game

# Home page
@app.route('/game')
def index():
    player_1.score = 0
    player_2.score = 0
    return render_template(
        'index.html', 
        title="Rock, Paper, Scissors!", 
        player_1=player_1, 
        player_2=player_2,
        p1_score=player_1.score,
        p2_score=player_2.score
    )

# 2 player game - choices submitted
@app.route('/game/fight', methods=['POST'])
def fight():
    p1_choice = request.form['p1_choice']
    p2_choice = request.form['p2_choice']
    set_choices(p1_choice, p2_choice)
    return redirect(f"/game/{p1_choice}/{p2_choice}")

# Results page for 2 player game
@app.route('/game/<p1_choice>/<p2_choice>')
def game_result(p1_choice, p2_choice):
    game = Game(player_1, player_2)
    game_result = game.determine_winner(player_1, player_2)
    return render_template(
        'playagain.html',
        title="Play again!",
        player_1=player_1,
        player_2=player_2,
        game_result=game_result,
        p1_score=player_1.score,
        p2_score=player_2.score,
        results=player_1.results
    )

# 1 player game - main page
@app.route('/play')
def play_game():
    player_1.score = 0
    return render_template(
        'play.html',
        title="Beat the computer",
        player_1=player_1,
        player_2=computer_player,
        p1_score=player_1.score,
        p2_score=computer_player.score
    )

# 1 player game - new name submitted
@app.route('/play/newplayer', methods=['POST'])
def new_player():
    new_player_name = request.form['player_name']
    player_1.name = new_player_name
    return redirect('/play')

# 1 player game - choice submitted
@app.route('/play/fight', methods=['POST'])
def comp_fight():
    p1_choice = request.form['p1_choice']
    p2_choice = computer_player.choice
    set_choices(p1_choice, p2_choice)    
    return redirect(f"/play/{p1_choice}/{p2_choice}")

# 1 player game - results page
@app.route('/play/<p1_choice>/<p2_choice>')
def game_result_comp(p1_choice, p2_choice):
    game = Game(player_1, computer_player)
    game_result = game.determine_winner(player_1, computer_player)
    return render_template(
        'comp_playagain.html',
        title="Play again!",
        player_1=player_1,
        player_2=computer_player,
        game_result=game_result,
        p1_score=player_1.score,
        p2_score=computer_player.score,
        results=player_1.results
    )
