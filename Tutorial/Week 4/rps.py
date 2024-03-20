'''
One loop = One input for users choice (1-3)

Three options:
 Rock (1) Paper (2) Scissors (3)
 
Three end results:
 WIN LOSE DRAW

Computer Choice:
Use math library Random function to Generate Computers turn
picking an integer (1 to 3)

'''

import random

def rps(userChoice, computerChoice):
    # EndOptions[] = [userChoice, computerChoice]
    Options = {"1":"Rock", "2":"Paper", "3":"Scissors"}
    userRealChoice = Options.get(userChoice)
    computerRealChoice = Options.get(str(computerChoice))
    print(userRealChoice, computerRealChoice)
    EndOptions = [['Paper', 'Rock', 'User Wins!'],
                  ['Rock', 'Paper', 'Computer Wins!'],
                  ['Scissors', 'Paper', 'User Wins!'],
                  ['Scissors', 'Rock', 'Computer Wins!'],
                  ['Rock', 'Scissors', 'User Wins!'],
                  ['Paper', 'Scissors', 'Computer Wins!'],
                  ['Paper', 'Paper', 'Draw!'],
                  ['Scissors', 'Scissors', 'Draw!'],
                  ['Rock', 'Rock', 'Draw!']]
    for choice in EndOptions:
        if userRealChoice == choice[0]:
            if computerRealChoice == choice[1]:
                return choice[2]
while True:
    userChoice = input('1,2,3 (Rock, Paper, Scissors): ')
    computerChoice = random.randint(1,3)
    endResult = rps(userChoice, computerChoice)
    print(endResult, end="\n\n")












    
    
