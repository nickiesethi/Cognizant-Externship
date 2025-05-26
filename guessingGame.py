# Project: Number Guessing Game

# Python's random library that automatically picks a random number that falls into the range specified
import random

# picks a number between 1 and 100
number_to_guess = random.randint(1, 100)

# Initialize our attempt counter to 0
count = 0 

# we give them 10 attempts
while(count < 10):
    if count >= 10:
             break
    user = int(input("Guess the number (between 1 and 100): "))
    if user > number_to_guess and count < 10: 
        print("Too high! Try again.", end = " ")
        count += 1
        
        continue
    elif user < number_to_guess and count < 10:
        print("Too low! Try again.", end = " ")
        count += 1
        if count >=10:
             break
        continue
    elif user == number_to_guess and count < 10:
        count += 1
        if count >= 10:
             break
        print("Congratulations! You guessed it in " + str(count) + " attempts!", end = " ")
        break
    
if count == 10:
        print("\nGame over! Better luck next time!")