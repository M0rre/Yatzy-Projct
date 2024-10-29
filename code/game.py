def game_rules():


    #Ta bort denna sen
    import random as rand
    random_n = []
    for _ in range(6):
        random_n.append(rand.randint(1,6))
    print(random_n)

    random_n[0], random_n[1], random_n[2], random_n[3], random_n[4], random_n[5]

    #Delar upp random_n till 5 olika listor med en "dice" i varje

    dices = [random_n[i:i+1] for i in range(0, len(random_n), 1)]
    #print(dices)


    #Ettor
    ones_count = 0 
    for number in random_n:
        if number == 1:
            ones_count += 1  
            if ones_count > 0:
                print(f'Put {ones_count} on category "Ones"? ')
            


    #Tvåor 
    two_count = 0
    for number in random_n:
        if number == 2:
            two_count += 2
            if two_count > 2:
                print(f'Put {two_count} on category "Twos"?')
    #Treor
    three_count = 0 
    for number in random_n:
        if number == 3:
            three_count += 3
            if three_count > 3:
                print(f'Put {three_count} on category "Threes"?')
    #Fyror
    four_count = 0 
    for number in random_n:
        if number == 4:
            four_count += 4
            if four_count > 4:
                print(f'Put {four_count} on category "fours"?')     
    #Femmor
    five_count = 0 
    for number in random_n:
        if number == 5:
            five_count += 5
            if five_count > 5:
                print(f'Put {five_count} on category "Fives"?')
    #Sexor
    six_count = 0 
    for number in random_n:
        if number == 6:
            six_count += 6
            if six_count > 6:
                print(f'Put {six_count} on category "Sixes"?')


    ### BONUS
    #Par

    #Två Par

    #Triss

    #Fyrtal

    #Kåk

    #Liten Stege

    #Stor Stege

    #Chans 

    #Yatzy

game_rules()