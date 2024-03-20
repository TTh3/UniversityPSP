# File: fourthWeek_5.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: (5) Week 4 - Practical (List Data Type and For Loops) 
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

numbers =[7,8,2,0,1,6,3,4]

numSum = 0
index = 0
while index < len(numbers):
    numSum+=numbers[index]
    index+=1
print(index, numSum)