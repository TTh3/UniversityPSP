#
# File: 11th_week3.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Question 3
number_list = input("Enter 10 numbers: ").split()
for num in range(int(len(number_list)/2)):
    prev_num = number_list[num]
    next_num = number_list[len(number_list) - num - 1]
    number_list[num] = next_num
    number_list[len(number_list) - num - 1] = prev_num
    print(prev_num, next_num)
    
print("Reversed Number List: ", number_list)