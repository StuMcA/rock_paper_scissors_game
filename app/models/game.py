class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.points_for_win = 1

    def determine_winner(self, player_1, player_2):

        not_picked = player_1.choice == 'not selected' or player_2.choice == "not selected"

        rock_draw = player_1.choice == "rock" and player_2.choice == "rock"
        paper_draw = player_1.choice == "paper" and player_2.choice == "paper"
        scissors_draw = player_1.choice == "scissors" and player_2.choice == "scissors"

        draw = rock_draw or paper_draw or scissors_draw

        p1_win = (
            (player_1.choice == "rock" and player_2.choice == "scissors") or 
            (player_1.choice == "scissors" and player_2.choice == "paper") or 
            (player_1.choice == "paper" and player_2.choice == "rock")
        )

        if not_picked:
            game_result = f"Please select a move for both players!"

        elif draw:
            game_result =  f"It was a draw! Both played {player_1.choice}"
            player_1.results.append(f"{player_1.choice.capitalize()} draw")
            if len(player_1.results) > 10:
                player_1.results.pop(0)
            
        elif p1_win:
            game_result = f"{player_1.name} won with {player_1.choice}"
            player_1.score += 1
            player_1.results.append(f"P1 win with {player_1.choice}")
            if len(player_1.results) > 10:
                player_1.results.pop(0)

        else:
            game_result = f"{player_2.name} won with {player_2.choice}"
            player_2.score += 1
            player_1.results.append(f"P2 win with {player_2.choice}")
            if len(player_1.results) > 10:
                player_1.results.pop(0)
        
        return game_result


results = []

    