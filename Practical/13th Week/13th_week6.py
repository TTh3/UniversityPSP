#
# File: 13th_week6.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 13 - Practical
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Question 6
def display_with_dash (word):
    new_word = ""
    for letter in word:
        new_word+=letter+'-'
    return new_word[:-1]
words = ['Elvis', 'has', 'left', 'the', 'building!']
for word in words:
    print(display_with_dash(word))