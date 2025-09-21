"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""
from random import randint

def check_int(s):
    """ Check if string 's' represents an integer. """
    # Convert s to string
    s = str(s) 

    # If first character of the string s is - or +, ignore it when checking
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    
    # Otherwise, check the entire string
    return s.isdigit()

def check_interval(s):
    """ Check if the target is between 1 and 100"""
    if s.isdigit():
        if s>=1 and s<=100:
            return True
        return False
    return False

def input_integer(prompt):
    """ Asks user for an integer input for the computer to guess. If valid, the string input is returned as an integer. """
    target = input(prompt) # Ask the user for their guess
    while not check_int(target) and not check_interval(target): # Repeat until the user inputs a valid integer
        print('Please, enter a n integer number between 1 and 100')
        target = input(prompt)  
    return int(target)

print("First you need to choose a number and then i will try to find it")
target = input_integer("Your number (1-100)? ")

guess = randint(1, 100) # Computer selects a random number to guess between 1 and 100 inclusive

#initialization of the lowest and highest as we do as human on the first try
lowest_guess=1 
highest_guess=100

while guess != target: # Repeat until the computer guesses.
    print(f"My new guess is {guess}")
    if guess < target : #if the guess is too low
        print(" But it's to low !") 
        lowest_guess=guess #update the lowest, the computer can't go under
        guess= randint(guess,highest_guess-1) # the computer needs to guess between the highest and its last guess
    else :
        print("But it looks too high!\n")
        highest_guess=guess #update the lowest, the computer can't go higher
        guess = randint(lowest_guess,guess)

print("I won ! The number was " + str(guess))