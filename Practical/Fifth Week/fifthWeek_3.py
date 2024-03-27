#
# File: fifthWeek_3.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 5 - Practical (Debugging)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

colour_mixers = [
    [["red","blue"],"purple"],
    [["red","yellow"],"orange"],
    [["blue","yellow"],"green"],
    [["blue","red"],"purple"],
    [["yellow","red"],"orange"],
    [["yellow","blue"],"green"]
                 ]
mix_colours = input("Mix red, yellow or blue: ").split(" ")
for colourGroups in range(len(colour_mixers)):
    if mix_colours == colour_mixers[colourGroups][0]:
        print(f"You mixed {mix_colours[0]} and {mix_colours[1]}, which results to {colour_mixers[colourGroups][1]}")
    

