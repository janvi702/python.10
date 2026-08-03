import random #importing a random library
#defining different variables
options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
# if player does not enter the optin variables, the statement will be printed again
while player not in options:
	player = input("Enter a choice: ")
#the result of the player and the computer will be displayed
print(f"player: {player}")
print(f"computer: {computer}")
#using conditional statements to print the outcome
if player == computer:
	print("It's a tie!")
elif player == "rock" and computer == "scissors":
	print("You win!")
elif player == "paper" and computer == "rock":
	print("You win!")
elif player == "scissors" and computer == "paper":
	print("You win!")
else:
	print("You lose!")
