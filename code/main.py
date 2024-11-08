import util_and_config as uac
config = uac.config()
import player
import dice
import game


def user_menu():
        uac.clear_terminal()
        print("""
         $$\     $$\          $$\                         
         \$$\   $$  |         $$ |                        
          \$$\ $$  /$$$$$$\ $$$$$$\   $$$$$$$$\ $$\   $$\ 
           \$$$$  / \____$$\\_$$  _|  \____$$  |$$ |  $$ |
            \$$  /  $$$$$$$ | $$ |      $$$$ _/ $$ |  $$ |
             $$ |  $$  __$$ | $$ |$$\  $$  _/   $$ |  $$ |
             $$ |  \$$$$$$$ | \$$$$  |$$$$$$$$\ \$$$$$$$ |
             \__|   \_______|  \____/ \________| \____$$ |
                                                $$\   $$ |
                                                \$$$$$$  |
                                                 \______/ 
        1. Start
        2. High Scores

        0. Exit program
        """)

        user_menu_input = uac.error_handling_int("Choose form menu (0-2): ")
        while True:
                match user_menu_input:
                        case 1:
                                uac.clear_terminal()
                                play_game()
                        case 2:
                                uac.clear_terminal()
                                print_high_scores()
                                user_menu_input = uac.error_handling_int("1. Start\n2. High Scores\n\n\n0. Exit program\nChoose form menu (0-2): ")
                        case 0:
                                exit(1)
                        case _:
                                uac.clear_terminal()
                                user_menu_input = uac.error_handling_int("1. Start\n2. High Scores\n\n\n0. Exit program\nWrong input, choose form menu (0-2): ")
               
def play_game():
        players_scoreboards = player.get_players()
        players = list(players_scoreboards.keys())
        for round in range(15):
                for current_player in players:
                        print("Round: ", round + 1)
                        print(f"{current_player}s turn")
                        final_outcome = dice.roll_dice(config["total_dice"], config["max_rolls"])
                        game.get_options(final_outcome, current_player, players_scoreboards)
        update_highscore_file(players_scoreboards, filename="code\highscore_file.txt", player_totals = {})

def update_highscore_file(players_scoreboards, filename="code\highscore_file.txt", player_totals = {}):
        with open(filename, "r",encoding="utf-8") as file:
                for line in file:
                        player_data = line.rstrip()
                        player, score = player_data.split("円") # Stole the wierd symbol idea from Ben and Max instead of having a ":"
                        score = int(score)
                        player_totals[player] = score
        # Player totals
        
        # Calc player sum
        for player, category in players_scoreboards.items():
                player_score_sum = sum(score for score in category.values() if score is not None)# None needed for testing
                player_totals[player] = player_score_sum
                
        def get_value(item):
                return item[1]  # Get the score value from dict 
        sorted_highscore = dict(sorted(player_totals.items(), key=get_value, reverse=True))

        with open(filename, "w",encoding="utf-8") as file:
                for player, score in sorted_highscore.items():
                        file.write(f"{player}円{score}\n")


# Basically copied all of it from update_highscore_file
def print_high_scores(filename="code\highscore_file.txt"):
    with open(filename, "r",encoding="utf-8") as file:
        highscore_data = []
        for line in file:
            player_data = line.rstrip()
            player, score = player_data.split("円")
            score = int(score)
            highscore_data.append(f"{player}, {score}")

    # Print the highscore list
    print("\nPrevious high scores")
    print("======================")
    for highscore_print in highscore_data:
        print(highscore_print)
    print("======================")
    input("Enter to continue")
    uac.clear_terminal()

user_menu()