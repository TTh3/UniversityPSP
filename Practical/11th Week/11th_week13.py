#
# File: 11th_week13.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
def my_function(number):
    new_list = []
    index = 2
    while index < number:
        if number % index == 0:
            new_list.append(index)
        index += 1
    return new_list

print(my_function(12))
# new_list = [2,4]

# The function above returns the multiple factors of the provided number parameter