#
# File: 11th_week1.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Question 1
def determine_grade(score):
    if score >= 85 and score <= 100:
        return "HD"
    elif score >= 75:
        return "D"
    elif score >= 65:
        return "C"
    elif score >= 55:
        return "P1"
    elif score >= 50:
        return "P2"
    elif score >= 40:
        return "F1"
    elif score >= 0:
        return "F2"
    
# Running determine_grade(score) function
grade = determine_grade(90)
print(grade)