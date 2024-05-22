# Rock-paper-scissors game.
#
# Rock-paper-scissors game play:  
# The objective is to select a gesture which defeats the computer.  
# Gestures are resolved as follows:
#    *  Rock crushes scissors – rock wins.
#    *  Paper covers rock – paper wins.
#    *  Scissors cut paper – scissors win.
# If both players choose the same gesture, the game is a draw.

import random


def display_details():
    print('Author:  Jaylord')
    print('Email Id: siljd001')
    print('This is my own work as defined by the ')
    print('University\'s Academic Misconduct Policy.')


def generate_number():
    randomNo = random.randint(1, 3)
    return randomNo


def get_choice():
    # Prompt for and read user's choice
    choice = int(input('\nRock(1), Paper(2) or Scissors(3)? '))
    while choice < 1 or choice > 3:
        print('Invalid input - please enter the number 1, 2 or 3.')
        choice = int(input('Rock(1), Paper(2) or Scissors(3)? '))
    return choice


def determine_winner(user, comp):
    # Find a winner.
    
    # if comp chose rock
    if comp == 1 and user == 2:
        print('You win - paper covers rock!')
    elif comp == 1 and user == 3:
        print('You lose - rock crushes scissors!')

    # if comp chose paper
    elif comp == 2 and user == 3:
       print('You win - scissors cut paper!')
    elif comp == 2 and user == 1:
       print('You lose - paper covers rock!')

    # if comp chose scissors
    elif comp == 3 and user == 1:
       print('You win - rock crushes scissors!')
    elif comp == 3 and user == 2:
       print('You lose - scissors cut paper!')

    # else it's a draw!
    else:
       print('Draw - no winner!')




def play_game():   
    display_details()

    play = 'y'
    noGames = 0
    while play == 'y':
     
        user = get_choice()
        

        # Display user's choice as text to the screen
        if user == 1:
            print('You chose rock.')
        elif user == 2:
            print('You chose paper.')
        elif user == 3:
            print('You chose scissors.')

        # Randomly generate computer's choice
        comp = generate_number()

        # Display computer's "choice" as text to the screen
        if comp == 1:
            print('Computer chose rock.')
        elif comp == 2:
            print('Computer chose paper.')
        elif comp == 3:
            print('Computer chose scissors.')

        # Find a winner
        determine_winner(user, comp)
        
        noGames = noGames + 1
        
        play = input('\n\nPlay again (y|n)? ')

    return noGames



###
###

# Call function play_game
#num_games = play_game()

#if num_games == 1:
#   print("\n\nYou played", num_games, "game!")
#else:
#   print("\n\nYou played", num_games, "games!")

#print('\nThanks for playing!')