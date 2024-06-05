#
# File: 13th_week9.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 13 - Practical
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

def determine_initials(*full_name):
    
    if len(full_name) == 1:
        full_name = full_name[0].split()
        
    new_name = ""
    for  name in full_name:
        new_name += name[0]+". "
    return new_name
print(determine_initials('jaylord','delison','silverio'))

name_list= ["Peter Gene Hernandez", "Steveland Judkins", "Norma Jean Mortensen", "Ramon Antonio Gerard Estevez", "Declan Patrick McManus"]
for name in name_list:
    print(determine_initials(name))