#
# File: 11th_week5.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Question 5
def happy(name=""):
    if name != "":
        print("Happy Birthday,",f"dear {name}")
    print("Happy Birthday To You!")
def sing(name):
    happy()
    happy()
    happy(name)    
    happy()

sing('Elmer')