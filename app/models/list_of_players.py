import random
from app.models.player import Player
from app.models.computer import Computer

player_1 = Player("Abraham Lincoln", 1)
player_2 = Player("Jefferson Davis", 2)

computer_player = Computer()

def computer_choice():
    moves = ["rock", "paper", "scissors"]
    return random.choice(moves)

def set_choices(p1_choice, p2_choice = None):
    player_1.choice = p1_choice
    player_2.choice = p2_choice
    computer_player.choice = computer_choice()


    