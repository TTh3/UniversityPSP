#
#  PSP Assignment 2, SP2 2024 - Provided module blackjack.py.
#
#  File:   blackjack.py
#
#  Description:  Play one game of blackJack(dice) against the computer.
#
#  DO NOT modify this file.
#

import random


# Define BlackJack constants.
SCORE = 21
PLAYER_MIN_SCORE = 15
DEALER_MIN_SCORE = 17
MAX = 11

#
# Function to play one game of blackJack(dice) against the computer.
# Parameters: no_chips player owns.
# Returns:    result of game - 3 for win, 1 for a draw, 0 for a loss.
#             no_chips - no of chips player owns after playing one game.
#
def play_one_game(no_chips):

    bet = 0     # bet amount

    print('\n\n---------------------- START GAME ----------------------')

    # Roll player's hand.
    player_die1 = random.randint(1,MAX)
    player_die2 = random.randint(1,MAX)

    # Roll computer's hand (only one die).
    comp_die1 = random.randint(1,MAX)
    comp_die2 = random.randint(1,MAX)

    # Work out current hand totals.
    player_total = player_die1 + player_die2
    comp_total = comp_die1 + comp_die2

    # Display player's and dealer's hand - one die only so can place bet.
    print('| Dealer\'s hand is:', comp_die1)
    print('| Player\'s hand is:', player_die1)    

    # Place bet on hand.
    print('|\n| --> Number of chips:', no_chips)

    bet = int(input("| --> Place your bet:  "))

    while bet < 0 or bet > no_chips:
        print('|\n| --> Sorry, you can only bet what you have (0-' + str(no_chips) + ')!');
        bet = int(input('| --> Place your bet:  '))
        
    score = 0
    # Check for BlackJack on first roll.
    if player_total == SCORE and comp_total == SCORE:
        print('| *** Blackjack --')
        print('|\n| Dealer\'s hand is:', comp_die1, '+', comp_die2, '=', comp_total)
        print('| Player\'s hand is:', player_die1, '+', player_die2, '=', player_total)
        print('|\n| *** Blackjack! Push - no winners! ***')
        print('| -->', no_chips, 'chips left!')
        score = 1
    elif player_total == SCORE:
        no_chips = no_chips + bet
        print('|\n| Player\'s hand is:', player_die1, '+', player_die2, '=', player_total)
        print('|\n| *** Blackjack! Player Wins! ***')
        print('| -->', no_chips, 'chips left!')
        score = 3
    elif comp_total == SCORE:
        no_chips = no_chips - bet
        print('|\n| Dealer\'s hand is:', comp_die1, '+', comp_die2, '=', comp_total)
        print('|\n| *** Blackjack! Dealer Wins! ***')
        print('| -->', no_chips, 'chips left!')
    else:

        # *** Else if neither player or dealer have Blackjack then play out hand. ***
 
        # Display player's hand.
        print('|\n| Player\'s hand is:', player_die1, '+', player_die2, '=', player_total)

        # Play out player's hand - only if they don't bust on first roll.
        if player_total < SCORE:      

            # Hit or stand?
            play = input("| Please enter h or s (h = Hit, s = Stand): ")

            while play != 'h' and play != 's':
                play = input("| Please enter h or s (h = Hit, s = Stand): ")
                
            while player_total < PLAYER_MIN_SCORE and play == 's':
                print("|\n| Cannot stand on value less than ", PLAYER_MIN_SCORE, "!\n|", sep='')
                play = input("| Please enter h or s (h = Hit, s = Stand): ")

        # While player hasn't busted and player continues to 'hit'.
        while player_total < SCORE and play == 'h':

          player_die1 = random.randint(1,MAX)
                   
          print('| Player\'s hand is:', player_total, '+', player_die1, '=', end=' ')
          player_total = player_total + player_die1
          print(player_total)

          if player_total < SCORE: 
              play = input("| Please enter h or s (h = Hit, s = Stand): ")
     
              while play != 'h' and play != 's':
                 play = input("| Please enter h or s (h = Hit, s = Stand): ")
                
              while player_total < PLAYER_MIN_SCORE and play == 's':
                  print("|\n| Cannot stand on value less than ", PLAYER_MIN_SCORE, "!\n|", sep='')
                  play = input("| Please enter h or s (h = Hit, s = Stand): ")
        
        if player_total > SCORE:
            print("| *** Player busts!")


        # Play out dealer's hand.
        print('|\n| Dealer\'s hand is:', comp_die1, '+', comp_die2, '=', comp_total)
            
        while comp_total < DEALER_MIN_SCORE:
     
          comp_die1 = random.randint(1,MAX)
         
          print('| Dealer\'s hand is:', comp_total, '+', comp_die1, '=', end=' ')
          comp_total = comp_total + comp_die1
          print(comp_total)

        if comp_total > SCORE:
          print("| *** Dealer busts!")
        

        # Determine winner and display to the screen.
        print("|\n| *** Dealer:", comp_total, " Player:", player_total, ' - ', end=' ');

        # If the player busts, or 
        # if the dealer is 21 or under and the dealers hand is greater than the players hand,
        # then dealer wins the hand.        
        if ((player_total > SCORE) or (comp_total > player_total and comp_total <= SCORE)): 
          no_chips = no_chips - bet
          print("Dealer Wins! ***")
        
        # If dealer and player hold the same point value, no one wins.
        elif comp_total == player_total:
          print("Push - no winners! ***")
          score = 1
        
        # Otherwise, the player wins.
        else:
          no_chips = no_chips + bet
          print("Player Wins! ***")
          score = 3

        print('| -->', no_chips, 'chips left!')
              
    print('----------------------- END GAME -----------------------\n')
    

    # Return game score - 3 for a win, 1 for a draw and 0 for a loss
    # and return no_chips remaining.
    return [score, no_chips]


