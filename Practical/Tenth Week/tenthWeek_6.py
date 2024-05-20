#
# File: tenthWeek_6.py
# Author: Jaylord
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Practical 10, Excercise 6
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

def read_colour():
    user_colour = input('Enter Primary Colour - red, blue or yellow: ')
    while user_colour not in ['red','blue','yellow']:
        user_colour = input('Please enter valid primary colour! red, blue or yellow: ')

read_colour()
        