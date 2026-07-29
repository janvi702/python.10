#To generate a random number from 1 to 50
import random
num = random.randint(1, 50) 
print(num) 

#Alternate method
import random
low = 1
high = 50
num = random.randint(low, high) #returns random number between 1 to 50
print(num) 

#To generate floating number between 0 to 1
import random
num = random.random() #returns floating point between 0 and 1
print(num) 

#To generate rock, paper and scissor
import random
game = ("rock", "paper", "scissor") 
final = random.choice(game) 
print(final) 
