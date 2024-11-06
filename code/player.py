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
    players = uac.error_handling_int("How many players do you want to add? ")

    #Loop to add each player 
    for i in range(players):
        player_name = input(f"Choose name for player {i + 1}: ")
        players_scoreboards[player_name] = scoreboard() #Assigns a individual scoreboard
        print(f"Current players: {list(players_scoreboards.keys())}")

    print("\nAll players have been added.")
    return players_scoreboards


def print_scoreboards(player_scoreboards):
    #For printing scoreboards in a nice way
    for player, board in player_scoreboards.items():
        print(f"\nScoreboard for {player}:")
        for category, score in board.items():
            print(f"{category}: {score}")

def print_scoreboard_two(players_scoreboards):
    #Creates a list of the keys (player names)
    player_names = list(players_scoreboards)

    #Header for names
    print(f"{'Category':<20}", end="") # <20 kan vi nog ändra 
    for player in player_names:
        print(f"{player:<{15}}", end="")
    print()

    #Print each category and then scores
    categories = list(scoreboard().keys()) # Get a list from categories from the scoreboard
    for category in categories:
        print(f"{category:<{20}}", end="")# samma vänstersak
        for player in player_names:
            #Gets player score for category
            score = players_scoreboards[player][category]
            score_str = f"{score}" if score is not None else 0 
            print(f"{score_str:<15}", end="") #Score colum
        print()




players_scoreboards = get_players()
print_scoreboard_two(players_scoreboards)