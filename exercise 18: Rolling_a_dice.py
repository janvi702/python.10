#create a file
import random

#Dice diagram
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │", 
        "└─────────┘" ),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │", 
        "└─────────┘" ),
    3: ("┌─────────┐",
        "│    ●    │",
        "│    ●    │",
        "│    ●    │", 
        "└─────────┘" ),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │", 
        "└─────────┘" ),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │", 
        "└─────────┘" ),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │", 
        "└─────────┘" ) }

#Assigned variables
dice = []
total = 0

#To generate random values for each die
num_of_dice = int(input("Enter the dice number: "))
for die in range(num_of_dice):
    dice.append(random.randint(1, 6)) 

#To represent the dice visually line-by-line
for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line) 

#Sum values of all dice and the final result
for die in dice:
    total += die
print(f"total: {total}")
