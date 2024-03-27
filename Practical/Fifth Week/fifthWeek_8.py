#
# File: fifthWeek_8.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 5 - Practical (Debugging)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
PIZZA_MENU = ["Margherita","Hawaiian","Pepperoni"]
PIZZA_RECIPES=[
    ["Tomato","Cheese", "Fresh Tomato", "Basil"],
    ["Tomato","Cheese", "Ham", "Pineapple"],
    ["Tomato","Cheese", "Pepperoni"]
               ]

def display_details():
    AUTHOR = "Jaylord Silverio"
    EMAIL_ID= "siljd001@mymail.unisa.edu.au"
    POLICY  ="This is my own's work as defined by the University's Academic Misconduct Policy"
    
def get_pizza_choice():
    for index in range(len(PIZZA_MENU)):
        print(f"{index}: {PIZZA_MENU[index]}")
        if index+1 == len(PIZZA_MENU):
            print(f"{index+1}: Quit")

selection = int(input('Please make a selection: '))

while (selection < 0) or (selection > len(PIZZA_MENU)):
    selection = int(input("Invalid input, please try again: "))

print(f"{PIZZA_MENU[selection]}: {" ".join(PIZZA_RECIPES[selection])}")

