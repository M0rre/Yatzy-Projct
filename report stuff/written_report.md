# Planning
## main.py
* Game loop
* User input
---
## game.py
* Scoring logic
* rolling dice, choosing scores
* Winner
---
## dice.py
* Generate dice
* Don't forget to keep chosen dice
---
## player.py
* Names
* (Scores)
* (Number of turns)
---
## scoreboard(.py)
* Might be a part of player.py
* Maybe save to either a txt or SQL file
* Neat lookn' so things such as '-', '_' and '|' as separators 
---
## util_and_config.py
* Error handling
* Change player count (or make this a choise when starting the came)
* Number of dice
* Rules (changing between maxi and normal yatzy)
---
# How we created the ascii dice art

First found a stuitable img for the ascii generator:
![alt text](./images/istockphoto-172793327-612x612.jpg)

Then dialed it in for so that we got some decent results
![alt text](./images/ascii_generator.png)



### The results:
```

 ░░░░░░░▒███▓▒░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░▒▓▒░░░░░░░ 
░▓▓▓▓▓███   ░████▓▓▓▓▓▓▓▓▓████▓████▓▓▓▓▓▓▓▓▓▓████▒░████▓▓▓▓░ 
░▓▓▓███        ▓██▓▓▓▓▓▓███░      ███▓▓▓▓▓▓███░      ░███▓▓░
░▓▓██     ░▒ ░   ██▓▓▓▓██░   ░░░    ██▓▓▓▓██░          ▓█▓▓░
░▓▓█   ░  ██░     █▓▓▓██  ██     ██  ▓█▓▓▓█  ░█▒ ██ ██░ ██▓░
░▓▓█   ░░    ░░   █▓▓▓█░             ░█▓▓▓█              █▓░
░▓▓█▒     ░░  ░ ▒██▓▓▓██ ░  ▒░▒░░  ░ ▒▓▓▓▓█▓▓░ ░░░░░  ░  █▓░
░▓▓▓██  ░▓   ▓ ░██▓▓▓▓▓██░ ░     ▒░ ██▓▓▓▓██▓  ▓    ░█ ▒██▓░
░▓▓▓▓███░░   ░███▓▓▓▓▓▓▓███ ▓░ ░▒ ▓██▓▓▓▓▓▓▓██▒░   ░  ███▓▓░
░▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓███   ████▓▓▓▓▓▓▓▓▓▓██▒  ▓███▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓█████████▓▓▓▓▓▓▓▓▓▓▓█████████▓▓▓▓▓▓▓▓▓▓█████████▓▓▓▓▓░
░▓▓▓███░  ░  ▓██▓▓▓▓▓▓▓▓███░  █  ░███▓▓▓▓▓▓███▒  ▒   ███▓▓▓░
░▓███    ░▒░   ███▓▓▓▓▓██           ██▓▓▓▓██░    ░░█   ██▓▓░
░▓█  ░██    ░█░ ▒█▓▓▓▓██  ██ ░█ ░██  ██▓▓▓█  ░█     ░▒  ██▓░
░▓█          ░   █▓▓▓▓█              ▒█▓▓▓█    ▓█   ▒█   █▓░
░▓█▓ ░ ▒▒██░░  ▒ █▓▓▓▓█▒ ░ ░░▒█░░  █ ██▓▓▓█  ░ ░ ██   ░░ █▓░
░▓▓█▓░▒       ▒░▓█▓▓▓▓▓██ ░░     ▒ ▒██▓▓▓▓██░ ░     ░ ░▓██▓░
░▓▓▓██ ▒   █  ███▓▓▓▓▓▓▓██░░░  ▓  ███▓▓▓▓▓▓███ ▒  ░░  ███▓▓░
░▓▓▓▓███   ▒███▓▓▓▓▓▓▓▓▓▓████  ▒███▓▓▓▓▓▓▓▓▓▓███   ████▓▓▓▓░
 ░░░░░░▒▓█▓▒░░░░░░░░░░░░░░░░▒▓▓▒░░░░░░░░░░░░░░░▒▓█▓▒░░░░░░░ 
```


### Touched them up a bit:
```

 ░░░░░░░▒███▓▒░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░▒▓▒░░░░░░░ 
░▓▓▓▓▓███   ░████▓▓▓▓▓▓▓▓▓████▓████▓▓▓▓▓▓▓▓▓▓████▒░████▓▓▓▓░
░▓▓▓███        ▓██▓▓▓▓▓▓███░      ███▓▓▓▓▓▓███░      ░███▓▓░
░▓▓██     ░▒ ░   ██▓▓▓▓██░   ░░░    ██▓▓▓▓██░          ▓█▓▓░
░▓▓█   ░  ██░     █▓▓▓██  ██     ██  ▓█▓▓▓█ ░██░ ██ ██░ ██▓░
░▓▓█   ░░    ░░   █▓▓▓█░             ░█▓▓▓█              █▓░
░▓▓█▒     ░░  ░ ▒██▓▓▓██ ░  ▒░▒░░  ░ ▒▓▓▓▓█▓▓░ ░░░░░  ░  █▓░
░▓▓▓██  ░▓   ▓ ░██▓▓▓▓▓██░ ░     ▒░ ██▓▓▓▓██▓  ▓    ░░ ▒██▓░
░▓▓▓▓███░░   ░███▓▓▓▓▓▓▓███ ▓░ ░▒ ▓██▓▓▓▓▓▓▓██▒░   ░  ███▓▓░
░▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓███   ████▓▓▓▓▓▓▓▓▓▓██▒  ▓███▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓█████████▓▓▓▓▓▓▓▓▓▓▓█████████▓▓▓▓▓▓▓▓▓▓█████████▓▓▓▓▓░
░▓▓▓███░  ░  ▓██▓▓▓▓▓▓▓▓███░  █  ░███▓▓▓▓▓▓███▒  ▒   ███▓▓▓░
░▓██░    ██░   ███▓▓▓▓▓██           ██▓▓▓▓██░   ░░█   ██▓▓░
░▓█  ██     ██░ ▒█▓▓▓▓██   █ ░█ ░█   ██▓▓▓█  ░█     █▒  ██▓░
░▓█      ██  ░   █▓▓▓▓█              ▒█▓▓▓█     █    ▒█  █▓░
░▓█▓ ░ ▒▒░░    ▒ █▓▓▓▓█▒ ░ ░░▒█░░    ██▓▓▓█  ░ ░  █ ░░   ▓░
░▓▓█▓░▒       ▒░▓█▓▓▓▓▓██ ░░     ▒ ▒██▓▓▓▓██░ ░     ░ ░ ▓██░
░▓▓▓██ ▒      ███▓▓▓▓▓▓▓██░░░  ▓  ███▓▓▓▓▓▓███ ▒  ░░  ███▓▓░
░▓▓▓▓███   ████▓▓▓▓▓▓▓▓▓▓████  ▒███▓▓▓▓▓▓▓▓▓▓███   ████▓▓▓▓░
 ░░░░░░▒▓█▓▒░░░░░░░░░░░░░░░░▒▓▓▒░░░░░░░░░░░░░░░▒▓█▓▒░░░░░░░
```

### Then split them up and trimmed them:
1:
```
      ██▓▓██
    ██░  ░░███ 
  ███         ▓██ 
 ██     ░▒ ░   ██▓
▓█   ░  ██░     █▓
█   ░░    ░░   █▓
█▒     ░░  ░ ▒██    
 ██  ░   ░ ░ ██    
  ███░░   ░███    
    ████████    
``` 

2:
```
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
```
3:
```
    ████▓▓████
 ███░      ░███
██░          ▓█▓
█ ░██░ ██ ██░  █▓░
█              █▓░
█▓▓░ ░░    ▒░  █▓░
██▓  ▓▒▒  ░░ ▒██▓░
  ██▒░   ░  ███▓
    ██▒  ▓███▓
     ▓█████▓
```
4:
```

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
```
 
5:
```
 
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
```
  
6:
```

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
```

## Realized how stupid they looked and made some neat dice
### Neat dice:
```
1
   _______
  /    ● /|
 /_●___ /●|
|      |●●|
|   ●  |●/
|______|/

2 
   _______
  /● ● ● /|
 /●_●_●_/●|
|    ● |●●|
|      |●/
|_●____|/

3
   _______
  /● ● ● /|
 /●_●_●_/●|
| ●    |  |
|   ●  |●/
|_____●|/

4
   _______
  / ●    /|
 /____● / |
| ●  ● |● |
|      | /
|_●__●_|/

5
   _______
  /● ● ● /|
 /●_●_●_/●|
|●   ● |● |
|  ●   |●/
|●___●_|/

6
   _______
  / ●    /|
 /____● /●|
| ●  ● |● |
| ●  ● |●/
|_●__●_|/
```

# Written report Yatzy Project
Max Morén and Teo Saveros
Grade: X

### Introduction

This project involves the development of a text based verion of *Yatzy*. Yatzy is a popular dice game where players roll five dice and aim to score the highest points by achieveing specific combinations such as "Fives", "Full House", "Three of a Kind" or "Yatzy". The goal is to fill out the scoreboard with as many points as possible.

In our project we developed a text based Yatzy game following the Swedish ruleset. We build the game in Visual Studio Code to "easily" share the code between the both of us. Our Yatzy game inlcude features like a dice rolling mechanism, player interactive elements to for example keep selected dice and to re-roll dice and an intuitive scoreboard interface. The game supports both a singleplayer experience and a multiplayer experience. Our programs interface has been designed to be simple to follow and engaging to use with the ASCII dice art.

### Discussion

##### How was rolling and re-rolling solved?

##### If several players, how was that solved?

The initial design for us was for a multiplayer game but we first thought of doing singleplayer first continue building on the code to support multiplayer. But as we implemented the scoreboard and the way to get the player to have its own scoreboard we quickly realised that it would work for multiple players with a simple for loop that iterates over a input where the program ask how many players will be playing. After that it was just finishing up the code around the rounds and making sure each player gets their turn. 

##### How was the scoreboard shown?

The scoreboard was shown in a table format with 15 categories. We created the scoreboard in a dictionary where the keys are the categories and the values are the scores asociated with the category

##### How did you decide what categories were possible

##### Reading and writing files?

##### Anything else that required a bit of thought

The first iteration of the scoreboard was a completly seperate scoreboard for each player that got printed beneath eachother. This was really ugly to look at and would have made the game more confusing while playing. After some thinking and testing we came up with the finalized scoreboard used in the game now. 

dynamic lines

### Lessons Learned

Visual studio code can be tricky sometimes with compiting and syncing code and we learned that patience is key. 

### Project Work

While working with this project we often organized the work accordingly to what we felt we were able to do each time we "met" and coded together. We broke the project into smaller pieces which both made it harder at times figuring out what to do first but also made it easier to figure out what should be where. 





