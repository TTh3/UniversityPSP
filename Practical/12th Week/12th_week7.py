#
# File: 12th_week7.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 12 - Practical (Functions and Problem Solving Strategies II)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

def update_list(num_list, size):
    for index in range(size):
        num = int(input(f"Enter a number ({index+1}): "))
        num_list[index] = num
number_list = [0]*10
MAX_SIZE = 10
update_list(number_list,MAX_SIZE)
print(number_list)

    