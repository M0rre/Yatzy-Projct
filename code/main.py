import util_and_config as uac
import player
import dice


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
        user_menu_input = uac.error_handling_int("Choose form menu (0-4)")
        
        match user_menu_input:
            case 1:
                    game()
            case 0:
                    exit(1)
               
def game():
        players = player.get_players().keys()
        players_scoreboards = player.get_players
        
        
        for round in range(15):
                for current_player in players:
                        print("Round: ", round + 1)
                        print(f"{current_player}s turn")
                        final_outcome = dice.roll_dice(total_dice=5, max_rolls=3)
                
        print("Done")
                       


user_menu()