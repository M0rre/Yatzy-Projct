#Ta bort denna sen
from collections import Counter
from dice import final_outcome




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
        "Yatzy": None,    }
    return scoreboard

def get_options(final_outcome): #This shit is either huge if statement, or I import counter. edit: imported counter
        
        # did some research for counters 
        # https://docs.python.org/3/library/collections.html#collections.Counter
        # like by this point ill just type "[what i want to do]()" and it will prob have a function for it, aka found any()
        c = Counter(final_outcome)
        available_categories = []

        #TODO I mean they're pretty much one rule so simplify into one later
        
        # TODO Add bonus
        
        if scoreboard["Ones"] is None and c[1] > 0:
                available_categories.append("Ones")
        if scoreboard["Twos"] is None and c[2] > 0:
                available_categories.append("Twos")
        if scoreboard["Threes"] is None and c[3] > 0:
                available_categories.append("Threes")
        if scoreboard["Fours"] is None and c[4] > 0:
                available_categories.append("Fours")
        if scoreboard["Fives"] is None and c[5] > 0:
                available_categories.append("Fives")
        if scoreboard["Sixes"] is None and c[6] > 0:
                available_categories.append("Sixes")
                
        # like by this point ill just type "[what i want to do]()" and it will prob have a function for it, aka found "any()"" that way
        if scoreboard["Pair"] is None and any(c >= 2)
        

#for _ in range(len(score_board)):

score()
calculate_upper_section()
calculate_score(category, dice)
