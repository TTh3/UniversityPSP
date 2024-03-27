#
# File: fifthWeek_2.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 5 - Practical (Debugging)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
import random

loop_count = 0
pair_count = 0
while loop_count !=10:
    die1= random.randint(1,6)
    die2= random.randint(1,6)

    if die1==die2:
        print(f"You rolled a pair of {die1}s")
        pair_count+=1
    else:
        print(f"You rolled a {die1} and a {die2}")
    loop_count+=1
    
print(f"You have rolled pairs {pair_count}/{10}")