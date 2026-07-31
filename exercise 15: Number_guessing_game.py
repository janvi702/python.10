import random

low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True

print("Number Guessing Game")
print(f"Select a number between {low} and {high}: ")

while is_running:
	guess = input("Enter your guess: ")

	if guess.isdigit():
		guess = int(guess)
		guesses +=1
		
		if guess < low or guess > high:
			print("The Number is out of range, Retry!  ")
		elif guess < answer:
			print("Too low, try again!  ")
		elif guess > answer:
			print("Too high, try again!  ")
		else:
			print (f"You guessed correctly! Number is:  {guesses}")
	else:
		print("Invaild guess!, Retry!")
