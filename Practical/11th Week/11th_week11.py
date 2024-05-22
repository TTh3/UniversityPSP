#
# File: 11th_week11.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Question 11
infile = open("seinfeld.txt", "r")
# a
outfilea = open("seinfeldOut3a.txt", "w")

# b
outfileb = open("seinfeldOut3b.txt", "w")


for line in infile:
    outfilea.write(line)
    outfileb.write(line)
    
infile.close()
outfilea.close()
outfileb.close()