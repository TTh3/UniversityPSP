#
# File: tenthWeek_5.py
# Author: Jaylord
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Practical 10, Excercise 5
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

singleNumbers = input("Write a number: ")
while singleNumbers.isdigit() == False:
    singleNumbers = input("Please write a valid number: ")
    
total = 0
for integer in singleNumbers:
    total+=int(integer)

print(f"The total of the integers is {total}")
