#
# File: 13th_week4.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 13 - Practical
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

def generate_chars(number, char):
    word = ""
    for _ in range(number):
        word+=char
    return word
print(generate_chars(5,'o'))
    