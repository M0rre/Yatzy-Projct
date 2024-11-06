from collections import Counter
from dice import roll_dice
from player import get_players
#from main import current_player z#TODO
current_player = "a"
final_outcome = roll_dice()


def scoreboard():

    scoreboard = {
        "Ones": None, 
        "Twos": None,
        "Threes": None,
        "Fours": None,
        "Fives": None,
        "Sixes": None,
        "Bonus": None,
        "One Pair": None,
        "Two Pairs": None,
        "Three of a Kind": None,
        "Four of a Kind": None,
        "Small straight": None,
        "Large straight": None,
        "Full House": None,
        "Chance": None,
        "Yatzy": None,    }
    return scoreboard

def get_options(final_outcome, current_player): #This shit is either huge if statement, or I import counter. edit: imported counter
        
        # did some research for counters 
        # https://docs.python.org/3/library/collections.html#collections.Counter
        # like by this point ill just type "[what i want to do]()" and it will prob have a function for it, aka found any()
       
        players_scoreboards=get_players()
        c = Counter(final_outcome)
        available_categories = []

        #TODO I mean they're pretty much one rule so simplify into one later
        
        # TODO Add bonus
       
        
        
        if players_scoreboards[current_player]["Ones"] is None and c[1] > 0:
                available_categories.append("Ones")
        if players_scoreboards[current_player]["Twos"] is None and c[2] > 0:
                available_categories.append("Twos")
        if players_scoreboards[current_player]["Threes"] is None and c[3] > 0:
                available_categories.append("Threes")
        if players_scoreboards[current_player]["Fours"] is None and c[4] > 0:
                available_categories.append("Fours")
        if players_scoreboards[current_player]["Fives"] is None and c[5] > 0:
                available_categories.append("Fives")
        if players_scoreboards[current_player]["Sixes"] is None and c[6] > 0:
                available_categories.append("Sixes")
                
        # like by this point ill just type "[what i want to do]()" and it will prob have a function for it, aka found "any()"" that way
        if players_scoreboards[current_player]["Pair"] is None and any(c >= 2):
                available_categories.append("Pair")
        if players_scoreboards[current_player]["Two Pairs"] is None and sum(1 for value in c.values() if value >= 2) >= 2:
                available_categories.append("Two Pairs")

#for _ in range(len(score_board)):

get_options()
