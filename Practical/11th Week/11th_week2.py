#
# File: 11th_week2.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Question 2
series_num = input("Enter a Series of number, separated with space: ").split()
def find_lowest ():
    lowest_num = int(series_num[0]) 
    for num in series_num:
        if int(num) < lowest_num:
            lowest_num = int(num)
    return lowest_num       

def find_highest ():
    highest_num = int(series_num[0]) 
    for num in series_num:
        if int(num) > highest_num:
            highest_num = int(num)
    return highest_num

def find_total():
    total = 0
    for num in series_num:
        total += int(num)
    return total

def find_average():
    total = find_total()
    average = total/len(series_num)
    return average

print("Lowest Number", find_lowest())
print("Highest Number", find_highest())
print("Total", find_total())
print("Average", find_average())
