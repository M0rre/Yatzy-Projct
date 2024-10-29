def get_art():
  # Less neat dice
  die_1 = """
        ██▓▓██      
      ██░  ░░███    
    ███         ▓██ 
  ██     ░▒ ░   ██▓
  █   ░  ██░     █▓
  █   ░░    ░░   █▓ 
  █▒     ░░  ░ ▒██    
  ██  ░   ░ ░ ██    
    ███░░   ░███    
      ████████      
  """
 
  die_2 = """
      ███▓▓▓███     
    ███░      ███   
  ██░   ░░░    ██  
  ██  ██     ██  ▓█ 
  █░             ░█▓
  ██ ░  ▒░▒░░  ░ ▒█▓
  ██░ ░     ▒░ ██▓ 
    ███ ▓░ ░▒ ▓██▓  
      ███   ████▓   
        ██████▓     
  """

  die_3 = """
    ███▓▓▓████
  ███░      ░███
  ██░          ▓█▓
  █ ░██░ ██ ██░ ██▓░
  █              █▓░
  █▓▓░ ░░    ▒░  █▓░
  ██▓  ▓▒▒  ░░ ▒██▓░
    ██▒░   ░  ███▓
      ██▒  ▓███▓
      ▓█████▓
  """

  die_4 = """
    ███▓▓▓███    
  ███░  ░  ▓██ 
  ██░    ██░   ███   
  █  ██     ██░ ▒█ 
  █      ██  ░   █   
  █▓ ░ ▒▒░░    ▒▓█ 
  █▓░▒      ▒░▓█
    ██ ▒      ███  
    ███   ████   
      ▓▓█▓▓   
  """

  die_5 = """
      ███▓▓▓▓███
    ███░  █  ░███▓
  ██           ██▓
  ██   █ ░█ ░█   ██▓
  █              ▒█▓
  █▒ ░ ░░▒█░░  ▒▒██▓
  ██ ░░     ▒ ▒██▓
    ██░░░  ▒▒ ███▓
    ████  ▒███▓
      ░░▓▓▒░░
  """

  die_6 = """
    ███▓▓▓▓▓██
  ███▒  ▒   ███
  ██░   ░░█   ██▓
  █  ░█     █▒  ██
  █     █    ▒█  █▓
  █  ░ ░  █ ░░   ▓░
  ██░ ░     ░ ░ ▓██
  ▓███ ▒  ░░  ███
    ▓███   ████▓
      ░▒▓█▓▒░
      """

  # Neat dice
  dice_1 = """
     _______ 
    /    ● /|
   /_●___ /●|
  |      |●●|
  |   ●  |●/ 
  |______|/  
  
  """
  dice_2 ="""
     _______ 
    /● ● ● /|
   /●_●_●_/●|
  |    ● |●●|
  |      |●/ 
  |_●____|/  
  """
  dice_3 ="""
     _______ 
    /● ● ● /|
   /●_●_●_/●|
  | ●    |  |
  |   ●  |●/ 
  |_____●|/  
  """
  dice_4 ="""
     _______ 
    / ●    /|
   /____● / |
  | ●  ● |● |
  |      | / 
  |_●__●_|/  
  """
  dice_5 ="""
     _______ 
    /● ● ● /|
   /●_●_●_/●|
  |●   ● |● |
  |  ●   |●/ 
  |●___●_|/  
  """
  dice_6 ="""
     _______ 
    / o    /|
   /____o /o|
  | ●  ● |o |
  | ●  ● |o/ 
  |_●__●_|/  
  """

  # Nu ska den också vara skalbar med antal tärningar kvar och använda vilken tärning som input
  lines = zip(dice_1.splitlines(), dice_2.splitlines(), dice_3.splitlines(), dice_4.splitlines(), dice_5.splitlines(), dice_6.splitlines())
  
  for line in lines:
    print(" ".join(line))
  """
  dices = dice_1, dice_2, dice_3, dice_4, dice_5, dice_6
  spacing = ' '* 5
  for pieces in zip(*(dice.splitlines() for dice in dices)):
    print(spacing.join(pieces))

  print(f"Dice 1: {dice_1:<20} Dice 2: {dice_2:^11} Dice 3: {dice_3:>15} ") 
  """
  
  import random as rand
  random_n = []
  for _ in range(6):
    random_n.append(rand.randint(1,6))
  print(random_n)
  
  

  dices = [dice_1, dice_2, dice_3, dice_4, dice_5, dice_6] 
  #for i in dices:
    #for lines in dices[i]:
get_art()
