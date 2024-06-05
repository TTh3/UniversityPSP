#
# File: 12th_week5.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 12 - Practical (Functions and Problem Solving Strategies II)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

def sum_list(num_list):
    total = 0
    for num in num_list:
        total+=num
    return total
        
sum_values = sum_list([2,31,12,1,5])
print(sum_values)