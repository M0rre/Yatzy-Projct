import util_and_config as uac
config = uac.config()
import player
import dice
import game


def user_menu():
        print("""
        ==============================================================
                            .__                  __                 
        _____ _____  ___  __|__|  ___.__._____ _/  |____________.__.
        /     \\\\__  \ \  \/  /  | <   |  |\__  \\\\   __\___   <   |  |
        |  Y Y  \/ __ \_>    <|  |  \___  | / __ \|  |  /    / \___  |
        |__|_|  (____  /__/\_ \__|  / ____|(____  /__| /_____ \/ ____|
            \/     \/      \/     \/          \/           \/\/     
        ==============================================================
        1. Start
        2. Rules (WIP just print a txt file tho)

        0. Exit program
        """)
        user_menu_input = uac.error_handling_int("Choose form menu (0-4): ")
        
        match user_menu_input:
                case 1:
                        play_game()
                case 0:
                        exit(1)
               
def play_game():
        players_scoreboards = player.get_players()
        players = list(players_scoreboards.keys())
        for round in range(15):
                for current_player in players:
                        print("Round: ", round + 1)
                        print(f"{current_player}s turn")
                        final_outcome = dice.roll_dice(config["total_dice"], config["max_rolls"])
                        game.get_options(final_outcome, current_player, players_scoreboards)
        print("Done")
                       
def save_to_file():

        filename = "highscore_file.txt"
        with open(filename, 'w') as file:
                for players in player:
                        file.write(f"{player}, {sum(score)}")
                        file.write("------------")

user_menu()