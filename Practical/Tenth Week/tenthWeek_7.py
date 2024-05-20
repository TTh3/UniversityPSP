#
# File: tenthWeek_7.py
# Author: Jaylord
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Practical 10, Excercise 7
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Part a
def total_num_a():
    number_prompt = input('Enter Positive Integer: ')
    total = 0
    while number_prompt.isdigit() != False:
        total += int(number_prompt)
        number_prompt = input('Enter Positive Integer: ')

def number_lister_b():
    number_prompt = input('Enter sequence of positive integers: ')
    number_list = [int(i) for i in number_prompt.split("0")]
    print(number_list, len(number_list), max(number_list))

number_lister_b()