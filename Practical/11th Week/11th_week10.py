#
# File: 11th_week10.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Question 10
infile = open("seinfeld.txt", "r")
outfile = open("seinfeldOut2.txt", "w")

string = infile.readlines()
print(string)
for line in string:
    outfile.write(line)
infile.close()
outfile.close()