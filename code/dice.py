def get_dice_roll(held_dice,total_dice):
  import random as rand
  random_n = [rand.randint(1,6) for _ in range(total_dice-held_dice)]
  print(random_n)
  
  return random_n

def get_art(random_n):
  # Neat dice list
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
              # "*" To 
  lines = zip(*(dice[roll-1].splitlines() for roll in random_n)) 
  #lines_held= zip()
  return "\n".join(" ".join(line) for line in lines)
  
def main():
  # Temp variables
  held_dice = 0
  total_dice = 5
  
  random_n = get_dice_roll(held_dice, total_dice)
  get_art(random_n)
  print(get_art(sorted(random_n)))

main()

