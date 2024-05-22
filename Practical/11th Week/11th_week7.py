#
# File: 11th_week7.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import random

# Question 7
def generate_password(password_length):
    ascii_list = '''!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''
    password = ""
    for _ in range(password_length):
        random_ascii_char = ascii_list[random.randint(0,len(ascii_list)-1)]
        password+=random_ascii_char
    return password
# print(generate_password(8))