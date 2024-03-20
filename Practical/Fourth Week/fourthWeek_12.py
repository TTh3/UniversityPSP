# File: fourthWeek_12.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: (12) Week 4 - Practical (List Data Type and For Loops) 
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import random


randomNum = random.randint(1,100)
# print({randomNum})
def a():
    user_guess = int(input('Choose an integer between 1 to 100: '))
    while user_guess!=randomNum:
        print('Too bad - please try again!')
        user_guess = int(input('Choose an integer between 1 to 100: '))
        
    print("Well Done - you guessed it!")
    
def b():
    user_guess = int(input('Choose an integer between 1 to 100: '))
    
    while user_guess!=randomNum:
        
        if user_guess < randomNum:
            print('Too Low - Please Try Again!')
        else:
            print('Too High - Please try again!')
        user_guess = int(input('Choose an integer between 1 to 100: '))
    print("Well Done - you guessed it!")
    
def c():
    play_again = "y"
    while play_again!="n":
        randomNum = random.randint(1,100)
        print(randomNum)
        user_guess = int(input('Choose an integer between 1 to 100: '))
        while user_guess!=randomNum:
            if user_guess < randomNum:
                print('Too Low - Please Try Again!')
            else:
                print('Too High - Please try again!')
            user_guess = int(input('Choose an integer between 1 to 100: '))
        print("Well Done - you guessed it!")
        
        # Next Round
        play_again = input("Would you like to play again? [y/n]: ")
    print('bye bye!')

# a() or b() or c()
c()