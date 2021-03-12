class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_score = 0
        self.player_2_score = 0

    def determine_winner(self, player_1, player_2):

        rock_draw = player_1.choice == "rock" and player_2.choice == "rock"
        paper_draw = player_1.choice == "paper" and player_2.choice == "paper"
        scissors_draw = player_1.choice == "scissors" and player_2.choice == "scissors"

        draw = rock_draw or paper_draw or scissors_draw

        p1_win = (
            (player_1.choice == "rock" and player_2.choice == "scissors") or 
            (player_1.choice == "scissors" and player_2.choice == "paper") or 
            (player_1.choice == "paper" and player_2.choice == "rock")
        )

        if draw:
            game_result =  f"It was a draw! Both played {player_1.choice}"
            
        elif p1_win:
            game_result = f"{player_1.name} won with {player_1.choice}"

        else:
            game_result = f"{player_2.name} won with {player_2.choice}"
        
        return game_result



        
    