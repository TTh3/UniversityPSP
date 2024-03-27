#
# File: fifthWeek_1.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 5 - Practical (Debugging)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Collatz Conjecture
number_input = int(input("Please enter a number: "))
steps = 0
while number_input!=1:
    if number_input%2==0:
        result = int(number_input/2)
        print(number_input, "is even, so I divide by 2:", result)
        number_input=result
    elif number_input%2 != 0:
        result= int(number_input*3 +1)
        print(number_input, "is odd, so I calculate 3n + 1:", result)
        number_input=result
    steps+=1

print("The hailstone sequence took,", steps, "steps to reach 1")
        
    