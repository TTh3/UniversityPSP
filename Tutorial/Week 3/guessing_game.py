#
# File: guessing_Game.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Version: 1.0 5 August 2014
# Description: Week 3 Tutorial - Guessing Game (While Loop & Inputs)
# Academic Misconduct policy.
#

import random

number = random.randint(1, 10)
print('Random number is:', number)

guess = int(input('Please enter your guess: '))
print('You guessed:', guess)

while number != guess:
    if guess < number:
        print('Too low')
    elif guess > number:
        print('Too high')
    guess = int(input('Please enter your guess: '))
print('Well done - you guessed it!')
