#
# File: fourthWeek_4.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: (4) Week 4 - Practical (List Data Type and For Loops) 
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

xy = [4,3,2,1,0,'new','old']
print(xy)
for elm in xy:
    print(elm)
print(xy[:3])
print(xy[:-3])
xy[4] = "same"
print(xy)
print(list(reversed(xy)))