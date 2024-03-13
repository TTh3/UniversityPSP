#
# File: secondWeek_12.py
# Author: Jaylord
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Practical 2, Excercise 12
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

temperature = int(input("What is the temperature? "))
if temperature >= 40:
    print("Way too hot - Stay Inside!")
elif temperature >= 30:
    print("Hot - Beach Time!")
elif temperature >= 20:
    print('Lovely day - how about a picnic!?!')
else:
    print("Way too cold - stoke up the fire!")
