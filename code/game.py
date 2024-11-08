from collections import Counter
from player import print_scoreboard
import util_and_config as uac

def get_options(final_outcome, current_player, players_scoreboards): #This shit is either huge if statement, or I import counter. edit: imported counter
        
        # did some research for counters 
        # https://docs.python.org/3/library/collections.html#collections.Counter
        # like by this point ill just type "[what i want to do]()" and it will prob have a function for it, aka found any()

        c = Counter(final_outcome)
        available_categories = []

        one_to_six = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
        for i in range(1,7):
                if players_scoreboards[current_player][one_to_six[i-1]] is None and c[i] > 0:
                        available_categories.append(one_to_six[i-1])
                
        if players_scoreboards[current_player]["Pair"] is None and any(n >= 2 for n in c.values()):
                available_categories.append("Pair")
                                                                        #1 constant to count x times there's been two pairs in final_outcome
        if players_scoreboards[current_player]["Two Pairs"] is None and sum(1 for value in c.values() if value >= 2) >= 2:
                available_categories.append("Two Pairs")
                
        if players_scoreboards[current_player]["Three of a Kind"] is None and any(n >= 3 for n in c.values()):
                available_categories.append("Three of a Kind") 
                
        if players_scoreboards[current_player]["Four of a Kind"] is None and any(n >= 4 for n in c.values()):
                available_categories.append("Four of a Kind")
        
        if players_scoreboards[current_player]["Full House"] is None and len(c) == 2 and any(u for u,j in c.items() if j == 2) and any(u for u,j in c.items() if j == 3):
                available_categories.append("Full House")
                
        if players_scoreboards[current_player]["Small straight"] is None and sorted(final_outcome) == [1, 2, 3, 4, 5]:
                available_categories.append("Small straight")
                
        if players_scoreboards[current_player]["Large straight"] is None and sorted(final_outcome) == [2, 3, 4, 5, 6]:
                available_categories.append("Large straight")
                
        if players_scoreboards[current_player]["Chance"] is None:
                available_categories.append("Chance")
                 
        if players_scoreboards[current_player]["Yatzy"] is None and any(n >= 5 for n in c.values()):
                available_categories.append("Yatzy")
                
        available_categories.append("Cross out")
                
        print(f"Choose (0-{len(available_categories)})\n0: Show scoreboard")
        for category in available_categories:
                print(f"{available_categories.index(category)+1}: {category}")
        
        
        while True:
                user_category = uac.error_handling_int("Enter an option: ")
                
                if user_category == 0:
                        print_scoreboard(players_scoreboards)
                        input("Press enter to continue")
                # For numbers 1-6, basically did same as when appending but with more steps to make input a number and output string AND non static number for each option
                elif 1 <= user_category <= len(available_categories):
                        picked_category = available_categories[user_category-1] # Go back to index values to "browse" where you want to put your dice and takes string as picked_category value
                        if picked_category in one_to_six: # Checks if category is in one to six
                                num = one_to_six.index(picked_category)+1 # Get pos of it aka the number, add one bc index to number
                                players_scoreboards[current_player][picked_category] = c[num] * num #Multiply that shid
                                
                                
                        elif picked_category == "Pair":
                                # Finds largest key aka just the pair face, we times it with two because it's two of em 
                                # Also as I said before literally type [what you want]() and it works
                                players_scoreboards[current_player][picked_category] = max(u for u,j in c.items() if j >= 2)*2 
                                
                        elif picked_category == "Two Pairs":
                                players_scoreboards[current_player][picked_category] = sum(n for n in list(sorted((pairs for pairs in (u for u,j in c.items() if j >= 2)),reverse=True)))*2
        
                        elif picked_category == "Three of a Kind": # We look for highest value of any number that has been counted more than 3 times
                                players_scoreboards[current_player][picked_category] = max(u for u,j in c.items() if j >= 3)*3 
                                
                        elif picked_category == "Four of a Kind":
                                players_scoreboards[current_player][picked_category] = max(u for u,j in c.items() if j >= 4)*4 
                                
                        elif picked_category == "Full House": # Sum because all dice are used, it's already determined that it's a possibility
                                players_scoreboards[current_player][picked_category] = sum(final_outcome)
                                
                        elif picked_category == "Small straight":
                                players_scoreboards[current_player][picked_category] = 15
                                
                        elif picked_category == "Large straight":
                                players_scoreboards[current_player][picked_category] = 20
                                
                        elif picked_category == "Chance":
                                players_scoreboards[current_player][picked_category] = sum(final_outcome)
                                
                        elif picked_category == "Yatzy":
                                players_scoreboards[current_player][picked_category] = 50
                                
                                
                        elif picked_category == "Cross out":
                        
                                available_categories_cross_out = [category for category in players_scoreboards[current_player] if players_scoreboards[current_player][category] is None]
                                available_categories_cross_out.remove("Bonus") # So you cannot cross out the bonus
                                
                                print(f"Choose (0-{len(available_categories_cross_out)})\n0: Show scoreboard")
                                for category in available_categories_cross_out:
                                        print(f"{available_categories_cross_out.index(category)+1}: {category}")
                                
                                
                                while True:
                                        user_category_cross_out = uac.error_handling_int("Enter an option: ")
                                        if user_category_cross_out == 0:
                                                print_scoreboard(players_scoreboards)
                                                input("Press enter to continue")
                                        elif 1 <= user_category_cross_out <= len(available_categories_cross_out):
                                                players_scoreboards[current_player][available_categories_cross_out[user_category_cross_out - 1]] = 0
                                                break
                                        else:
                                                print("Invalid choice, please choose a valid option: ")
                                    
                          
                        
                        # Add bonus for one to six, also I did it again [what I need to be done/checked]()
                        if all(players_scoreboards[current_player][category] is not None for category in one_to_six):
                                ots = sum(players_scoreboards[current_player][category] for category in one_to_six)
                                if ots >= 63:
                                        players_scoreboards[current_player]["Bonus"] = 50                           
                                                
                                                
                        print_scoreboard(players_scoreboards)
                        input("Press enter to continue")
                        break 
