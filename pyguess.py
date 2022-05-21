# A simple number guessing game
# Could you make something cooler?
import random
import datetime


# Make n a random number between 1 and 99
n = random.randint(2, 5)

# # Ask user to guess the number    
guess = int(input("Enter an integer from 1 to 10: "))

while (True):
    if guess < n: 
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 10: "))
    elif guess > n: 
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 10: "))
    else:
        print ("you guessed it!")
        break
