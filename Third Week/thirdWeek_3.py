#
# File: thirdWeek_3.py
# Author: Jaylord
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Practical 3, Excercise 3
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# a)
str1 = 'Wednesday Thursday Friday'
new_string = ''
index = 0
while index < len(str1):
    if str1[index].isupper():
        new_string = new_string + str1[index]

    index = index + 1
    
new_string = new_string + '!?!'
# It grabs every upper case letter inside the string of characters to combine to a string
'''
print(new_string)
-> WTF!?!
'''

# b)
str1 = 'Wednesday Thursday Friday'
new_string = ''
index = 0
while index < len(str1):
    if str1[index].isupper():
        new_string = str1[index] + new_string

    index = index + 1
new_string = new_string + '!?!'
print(new_string)

