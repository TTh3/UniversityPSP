# File: fourthWeek_11.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: (11) Week 4 - Practical (List Data Type and For Loops) 
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import random
numList = []
for _ in range(10):
    numList.append(random.randint(1,20))

print(sorted(numList))