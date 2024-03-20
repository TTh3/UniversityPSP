# File: fourthWeek_8.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: (8) Week 4 - Practical (List Data Type and For Loops) 
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
fanta = "fanta"
a_count = 0
index = 0
while index < len(fanta):
    if fanta[index] == "a":
        a_count+=1
    index+=1
print(a_count)
print(fanta.count("a"))