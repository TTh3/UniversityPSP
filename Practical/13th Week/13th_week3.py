#
# File: 13th_week3.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 13 - Practical
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

def count_letter (word, char):
    num_char = 0
    for letter in word:
        if char == letter:
            num_char+=1
            
    return num_char

word_input = input('Write the word: ')
char_input = input('Type a letter: ')
print(count_letter(word_input, char_input))
