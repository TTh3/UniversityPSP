#
# File: 13th_week5.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 13 - Practical
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

def hailstone_seq (number):
    while number != 1:
        if number % 2 == 0:
            
            print(f'{number} is even, so I divide by 2:{number/2}')
            number = number/2
        else:
            print(f'{number} is odd, so I calculate 3n + 1:{3*number+1}')
            number = 3*number + 1

hailstone_seq(15)
            