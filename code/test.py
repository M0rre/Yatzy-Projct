

import util_and_config as uac




def scoreboard(): 
    scoreboard = {
        "Ones": 1, 
        "Twos": 1,
        "Threes": 1,
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


def save_to_file(players_scoreboards):

    filename = "code\highscore_file.txt"




    previous_scores = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                player_data = line
                

                #split to player and score
                player, score = player_data.split("円")
                #Turn score to int for reordering later
                previous_scores.append((player, int(score)))
    except FileNotFoundError:
        pass


    for player, scoreboard in players_scoreboards.items():
        total_score = 0
        for category, score in scoreboard.items():
            for category, score in scoreboard.items():
                total_score += score or 0  # Adds 0 if score is None
            previous_scores.append((player, total_score))

    previous_scores.sort(key=lambda x: x[1], reverse=True)

    with open(filename, 'w') as file:
        for player, score in previous_scores:
            file.write(f"{player}円 {score}\n")

    print("Scoreboard saved and sorted")
        

players_scoreboards = get_players()

print("scoreboards")
print_scoreboard(players_scoreboards)

save_to_file(players_scoreboards)
