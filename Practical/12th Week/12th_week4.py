#
# File: 12th_week4.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 12 - Practical (Functions and Problem Solving Strategies II)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

def capitalize_words(phrase):
    words = phrase.split()
    new_phrase = ""
    for word in words:
        new_word = word[0].upper() + word[1:]
        new_phrase+=f'{new_word} '
    return new_phrase

phrase = capitalize_words('hello my name is jeff hee he')
print(phrase)