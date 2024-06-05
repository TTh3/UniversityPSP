#
# File: 13th_week8.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 13 - Practical
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

def countDigits(chars):
    numInt = 0
    for char in chars:
        if char.isdigit():
            numInt+=1
    return numInt

print(countDigits('j1k23hiugh8'))