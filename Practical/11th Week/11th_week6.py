#
# File: 11th_week6.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Question 6

import random

# Selection
SELECTION = ['Rock','Paper','Scissors']

user_choice = input('Rock, Paper, Scissors [1,2,3]: ')
computer_choice = random.randint(0,2)
if SELECTION[int(user_choice)-1]==SELECTION[computer_choice]:
    print(f"Draw! Both are {SELECTION[int(user_choice)]}")
elif SELECTION[int(user_choice)-1] == "Rock":
    if SELECTION[computer_choice] == "Paper":
        print("You Lose! Rock is covered by Paper!")
    else:
        print("You Win! Rock destroys Scissors!")
elif SELECTION[int(user_choice)-1] == "Paper":
    if SELECTION[computer_choice] == "Rock":
        print("You Win! Paper wins against Rock!")
    else:
        print("You Lose! Paper is cut by Scissors!")
else:   # User Choice = "Scissors"
    if SELECTION[computer_choice] == "Rock":
        print("You Lose! Scissors is destroyed by Rock!")
    else:
        print("You Win! Scissors cuts Paper!")

        
    