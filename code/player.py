#funktion för att samla in spelare och avsluta när alla spelare gått med

import util_and_config as uac

def scoreboard(): 

    scoreboard = {
        "Ones": None, 
        "Twos": None,
        "Threes": None,
        "Fours": None,
        "Fives": None,
        "Sixes": None,
        "One Pair": None,
        "Two Pairs": None,
        "Three of a Kind": None,
        "Four of a Kind": None,
        "Small straight": None,
        "Large straight": None,
        "Full House": None,
        "Chance": None,
        "Yatzy": None,
    }
    return scoreboard

#def get_players():
"""
    player_list = []

    players = int(input("How many players do you want to add? "))

    for i in range(players):
        player_name = input(f"Choose name for player {i + 1}: ")
        player_list.append(player_name)
        print(f"Current players:", player_list )
        i += 1

    print("All players have been added\n",player_list)
"""

def get_players():
    #Dict to store player names and their individual scoreboard
    players_scoreboards = {}

    #Asks for number of players
    players = uac.error_handling_int("How many players do you want to add? (No duplicates): ")

    #Loop to add each player 
    for i in range(players):
        player_name = input(f"Choose name for player {i + 1}: ")
        players_scoreboards[player_name] = scoreboard() #Assigns a individual scoreboard
        print(f"Current players: {list(players_scoreboards.keys())}")

    print("\nAll players have been added.")
    return players_scoreboards


def print_all_scoreboards(player_scoreboards):
    #For printing scoreboards in a nice way
    for player, board in player_scoreboards.items():
        print(f"\nScoreboard for {player}:")
        for category, score in board.items():
            print(f"{category}: {score}")

def print_scoreboard(players_scoreboards):
    #Creates a list of the keys (player names)
    player_names = list(players_scoreboards)
    player_column_widths = {player: len(player) + 2 for player in player_names}
    #Header for names
    print("\033[4m\u00A0\033[0m"*(19+sum(int(i) for i in player_column_widths.values())+len(player_names))) # 19 is for category len, pipes and spaces and len(player_names is there for the additional pipes created by each player)
    #magic numbers: ""\033[4m   \033[0m"" for underline and "\u00A0" for a space that accepts underlines
    print(f"\033[4m┃ {'Category':<16}\033[0m", end="\033[4m┃\033[0m")
    for player in player_names:
        width = player_column_widths[player]
        print(f"\033[4m{player:^{width}}\033[0m", end="\033[4m┃\033[0m")
    print()

    

    #Print each category and then scores #?Added some lines for readability on the scoresheet also resized it
    categories = list(scoreboard().keys()) # Get a list from categories from the scoreboard
    for category in categories:
        print(f"\033[4m┃ {category:<16}\033[0m", end="\033[4m┃\033[0m")# samma vänstersak
        for player in player_names:
            #Gets player score for category
            width = player_column_widths[player]
            score = players_scoreboards[player][category]
            score_str = f"{score}" if score is not None else 0 
            print(f"\033[4m{score_str:^{width}}┃\033[0m", end="") #Score colum
        print()


if __name__ == "__main__":
    players_scoreboards = get_players()
    print_scoreboard(players_scoreboards)
    