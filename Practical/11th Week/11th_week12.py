#
# File: 11th_week12.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import random

# Selection
SELECTION = ["Rock", "Paper", "Scissors"]

user_choice = input("Rock, Paper, Scissors [1,2,3]: ")

def generate_number():
    return random.randint(1, 3)

def determine_winner(computer_choice, user_choice):
    # SELECTION[computer_choice], SELECTION[int(user_choice)-1]
    if user_choice == computer_choice:
        print(f"Draw! Both are {SELECTION[int(user_choice)]}")
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print("You Lose! Rock is covered by Paper!")
        else:
            print("You Win! Rock destroys Scissors!")
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("You Win! Paper wins against Rock!")
        else:
            print("You Lose! Paper is cut by Scissors!")
    else:  # User Choice = "Scissors"
        if computer_choice == "Rock":
            print("You Lose! Scissors is destroyed by Rock!")
        else:
            print("You Win! Scissors cuts Paper!")

total_games = 0
def play_game ():
    prompt = input("Play again (y|n)? ")
    if prompt == 'y':
        total_games+=1
# rps_game.py
computer_choice = random.randint(0, 2)
