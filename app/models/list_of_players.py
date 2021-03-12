from app.models.player import Player

player_1 = Player("Abraham Lincoln", 1)
player_2 = Player("Jefferson Davis", 2)

def set_choices(p1_choice, p2_choice):
    player_1.choice = p1_choice
    player_2.choice = p2_choice