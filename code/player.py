import util_and_config as uac

def scoreboard(): 
    scoreboard = {
        "Ones": None, 
        "Twos": None,
        "Threes": None,
        "Fours": None,
        "Fives": None,
        "Sixes": None,
        "Bonus": None,
        "Pair": None,
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

def get_players():
    #Dict to store player names and their individual scoreboard
    players_scoreboards = {}

    #Asks for number of players and keeps asking if players = 0
    while True:
        players = uac.error_handling_int("How many players do you want to add? (No duplicates): ")
        if players > 0:
            break
        print("Players must be at least 1. Please try again: ")

    #Loop to add each player #TODO if 0 it just gives up SO FIX THAT
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
            score_str = "-" if score == 0 else score_str # So crossed out values are more visible
            print(f"\033[4m{score_str:^{width}}┃\033[0m", end="") #Score colum
        print()

