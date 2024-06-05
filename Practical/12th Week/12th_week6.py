#
# File: 12th_week6.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 12 - Practical (Functions and Problem Solving Strategies II)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
import random
def generate_lotto_number ():
    return [str(random.randint(0,9)) for _ in range(7)]
def display_lotto_number (lotto_number):
    text = ", ".join(lotto_number)
    print(text)
    return text

for _ in range(20):
    lotto_number = generate_lotto_number()
    display_lotto_number(lotto_number)