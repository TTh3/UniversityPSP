#
# File: secondWeek_11.py
# Author: Jaylord
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Practical 2, Excercise 11
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

stage_rocket_time = int(input("Enter the time since rocket launch: "))
if stage_rocket_time<=100:
    print("Stage 1")
elif stage_rocket_time<=170:
    print("Stage 2")
elif stage_rocket_time<=260:
    print("Stage 3")
else:
    print("Free Flight (Unpowered)!")