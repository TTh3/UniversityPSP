#
# File: 11th_week9.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Question 9 
infile = open("seinfeld.txt", "r")
outfile = open("seinfeldOut1.txt", "w")

string = infile.read()
print(string)
outfile.write(string)
infile.close()
outfile.close()