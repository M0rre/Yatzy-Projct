#Ta bort denna sen
import random as rand
current_dice = []
for _ in range(6):
    current_dice.append(rand.randint(1,6))
print("Rolled dice", current_dice)



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





def calculate_upper_section(dice, number):
    return dice.count(number) * number

def calculate_lower_section(dice):
    pairs = [dice]
"""
    #Ones
    ones_count = 0 
    for number in current_dice:
        if number == 1:
            ones_count += 1  
    if ones_count > 0:
        return ones_count
            
    #Twoos 
    twos_count = 0
    for number in current_dice:
        if number == 2:
            twos_count += 1
    if twos_count > 0:
        return twos_count
    #Threes
    threes_count = 0 
    for number in current_dice:
        if number == 3:
            threes_count += 1
    if threes_count > 0:
        return threes_count
    #Fours
    fours_count = 0 
    for number in current_dice:
        if number == 4:
            fours_count += 1
    if fours_count > 0:
        return fours_count     
    #Fives
    fives_count = 0 
    for number in current_dice:
        if number == 5:
            fives_count += 1
    if fives_count > 0:
        return fives_count
    #Six'
    sixs_count = 0 
    for number in current_dice:
        if number == 6:
            sixs_count += 1
    if sixs_count > 0:
        return sixs_count
"""
    





#for _ in range(len(score_board)):

score()
calculate_upper_section()
calculate_score(category, dice)
