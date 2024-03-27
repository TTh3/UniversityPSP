#
# File: fifthWeek_4.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 5 - Practical (Debugging)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

sing = input("Would you like to sing a song [y|n]? ")
while sing != "n":
    verses_counter = int(input("How many verses of the song do you want to sing? "))
    while verses_counter != 0:
        print(f"{verses_counter} bottles of beer on the wall")
        print(f"{verses_counter} bottles of beer")
        print("If one of those should happen to fall")
        verses_counter-=1
        if verses_counter==0:
            print("No bottles of beer on the wall!!")
        else:
            print(f"{verses_counter} bottles of beer on the wall")
        print("\n")
    
    sing = input("That was fun! Would you like to sing again [y|n]? ")
    print("\n")
print("Thanks for singing along! : )")
    
    



