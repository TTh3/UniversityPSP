#
# File: tenthWeek_1&2.py
# Author: Jaylord
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Practical 10, Excercise 1 & 2
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import random


# Display Details
def display_details():
    print("Author: Jaylord Silverio")
    print("Email Id: siljd001")
    print("This is my own work as defined by the")
    print("University's Academic Misconduct policy")


# A Game of rock-paper-scissors (part a)
results = [0, 0, 0]  # wins  # losses  # draws


# Validate User's Choice
def get_choice():
    user_choice = input("Rock(1), Paper(2), Scissors(3) or No(4)? ")
    while user_choice not in ["1", "2", "3", "4"]:
        user_choice = input(
            "Please choose a valid number! Rock(1), Paper(2), Scissors(3) or No(4)? "
        )
    return user_choice


def RockPaperScissors(user_choice, computer_choice):

    Options = {"1": "Rock", "2": "Paper", "3": "Scissors"}

    userRealChoice = Options.get(user_choice)
    computerRealChoice = Options.get(str(computer_choice))
    print(f"You chose {userRealChoice}.")
    print(f"Computer chose {computerRealChoice}.")
    EndOptions = [
        ["Paper", "Rock", "You win - paper covers rock", 0],
        ["Rock", "Paper", "You lose - rock is covered by paper", 1],
        ["Scissors", "Paper", "You win - scissors cut paper", 0],
        ["Scissors", "Rock", "You lose - scissors can't cut rock", 1],
        ["Rock", "Scissors", "You win - rock can't be cut by scissors", 0],
        ["Paper", "Scissors", "You lose - paper is cut by scissors!", 1],
        ["Paper", "Paper", "Draw! Both Paper", 2],
        ["Scissors", "Scissors", "Draw! Both Scissors", 2],
        ["Rock", "Rock", "Draw! Both Rock", 2],
    ]
    for choice in EndOptions:
        if userRealChoice == choice[0]:
            if computerRealChoice == choice[1]:
                results[
                    choice[3]
                ] += 1  # Adds 1 to results list (0: win, 1: loss, 2: draw)
                return choice[2]


# Initial User Prompt
user_choice = get_choice()

while user_choice != "4":
    while user_choice not in ["1", "2", "3", "4"]:
        user_choice = input(
            "Please choose a valid number! Rock(1), Paper(2), Scissors(3) or No(4)? "
        )
    computer_choice = random.randint(1, 3)
    endResult = RockPaperScissors(user_choice, computer_choice)
    print(endResult, end="\n\n")
    user_choice = input("Rock(1), Paper(2), Scissors(3) or No(4)? ")
print(
    f"Wins: {results[0]}\nLosses: {results[1]}\nDraws: {results[2]}\n\nThank you for playing!"
)
