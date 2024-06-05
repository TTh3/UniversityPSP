#
# File: 12th_week3.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 12 - Practical (Functions and Problem Solving Strategies II)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
import random
def get_random(a=10):
    return random.randint(1,a)
for _ in range(10):
    random_num = get_random(10)
    print(random_num)