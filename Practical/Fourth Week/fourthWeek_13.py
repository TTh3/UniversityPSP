# File: fourthWeek_13.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: (13) Week 4 - Practical (List Data Type and For Loops) 
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
index = 0
output_string = ''
user_input = input("Enter a string: ")
while index < len(user_input):
    char = user_input[index]
    if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
        output_string += char
    index += 1
print(output_string)
'''
Explanation:
The program is asking the user to enter a 'any value' string
Using a while loop, a new variable called char storing the current element of the iteration
The next line invalidates vowels inside the string causing the variable "output_string" contain only consonants
The loop goes through every single character inside the string until the last one

Expectations: 
Printing output_string must result in a string full of only consonants

Example:
user_input = "big brown fox"
output_string = "bg brwn fx"
'''
