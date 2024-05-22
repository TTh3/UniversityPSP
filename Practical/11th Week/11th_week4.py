#
# File: 11th_week4.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Question 4
def reverse_list(number_list, bottomIndex, topIndex):
    number_list_org = [] + number_list
    number_list[bottomIndex] = topIndex
    number_list[len(number_list) - num - 1] = number_list_org[bottomIndex]
    return number_list

number_list = input("Enter 10 numbers: ").split()
for num in range(int(len(number_list)/2)):
    bottomIndex = num
    topIndex = number_list[len(number_list) - num - 1]
    number_list = reverse_list(number_list, num, topIndex)
print(number_list)
