import random 
import util_and_config as uac

def get_dice_roll(held_dices, held_values, total_dice):
    # Generate new rolls for dice that are not held
    new_rolls = [random.randint(1, 6) for _ in range(total_dice - len(held_dices))]
    current_dice = []

    new_roll_index = 0

    # Stores new and held dice, held dice keeps their position
    for i in range(total_dice):
        if i in held_dices: 
            # Finds the pos of i in held_dices and transfers it to
            current_dice.append(held_values[held_dices.index(i)])  # Get the held dice value directly
        else:
            current_dice.append(new_rolls[new_roll_index])  # Use the new roll
            new_roll_index += 1

    return current_dice

def get_art(current_dice):
    # Dice art for numbers 1 to 6
    dice = [
"""
     _______ 
    /    o /|
   /_o___ /o|
  |      |oo|
  |   ●  |o/ 
  |______|/  
  
  """
  ,
  """
     _______ 
    /o o o /|
   /o_o_o_/o|
  |    ● |oo|
  |      |o/ 
  |_●____|/  
  """
  ,
  """
     _______ 
    /o o o /|
   /o_o_o_/o|
  | ●    |  |
  |   ●  |o/ 
  |_____●|/  
  """
  ,
  """
     _______ 
    / o    /|
   /____o / |
  | ●  ● |o |
  |      | / 
  |_●__●_|/  
  """
  ,
  """
     _______ 
    /o o o /|
   /o_o_o_/o|
  |●   ● |o |
  |  ●   |o/ 
  |●___●_|/  
  """
  ,
  """
     _______ 
    / o    /|
   /____o /o|
  | ●  ● |o |
  | ●  ● |o/ 
  |_●__●_|/  
  """
    ]

    # Build the visual representation of the dice roll
    lines = zip(*(dice[roll - 1].splitlines() for roll in current_dice))
    return "\n".join(" ".join(line) for line in lines)

def roll_dice(total_dice=5, max_rolls=3): # TODO Add to config file
    held_dices = []
    held_values = []
    big_line = "="*97
    
    current_dice = get_dice_roll(held_dices, held_values, total_dice)
    
    for roll_number in range(max_rolls):
            if roll_number+1 < max_rolls:
                    print(f"Roll {roll_number + 1} Result:")
                    print(get_art(current_dice))
            if roll_number+1 == max_rolls:
                    print("Final Result:")
                    print(get_art(current_dice))
            if roll_number < max_rolls - 1:  # Don't hold on the last roll
                # Ask the user which dice to hold
                held_input = input(f"Enter the dices of the dice to hold (1-{total_dice}, leave blank or 0 to stop rolling), separated by commas: ")
                
                if held_input: # Made dynamic lines, why? Idk ocd or something
                    print(big_line+"="+("="*len(held_input)))
                else:    
                    print(big_line)
                
                
                if held_input.strip() == "0":
                    print("Skipped remaining rolls")
                    break
                
                if held_input.strip():  # If there's an input, make som use out of it and TODO#// INPUT IS OUT OF RANGE 
                    #. TODO if duplicates it breaks # // made into a set that converts to list so ignores duplicates
                    held_dices = list({int(i)-1 for i in held_input.split(',') if i.strip().isdigit() and 1 <=int(i) <= total_dice}) # Ignores numbers to largenow
                    held_values = [current_dice[i] for i in held_dices if i < total_dice]  # Keep only valid dices

                # Roll the dice again
                current_dice = get_dice_roll(held_dices, held_values, total_dice)

    return current_dice


# The thing you commented must've been me trying to return only the variable because I tried to use it in other files by only importing that variable later, which did not work... but it didn't destroy anything either so I guess that's where it came from