"""

Things to ask:
What would happen if user got 4 or 5 number of values equal?
What if there are 3 of a kind and the other 2 have the same value (pair?)

"""

#
# File: siljd001_battle_p1.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Game of Dragon Battleground
# This is my own work as defined by the University's Academic Misconduct policy.
#
import sys # TODO: GET RID OF ME PLEESAESEAEASESA!

sys.dont_write_bytecode = True # Gets rid of python cache in vscode

import random
import dice  # Import dice module to display the die face values to the screen

# Player and Dragon's Health
player_health = 100
dragon_health = 100

# Game Summary
game_result = [
    0,  # 0) Number of Games
    0,  # 1) Games won
    0,  # 2) Games lost
    0,  # 3) Games drawn
    0,  # 4) Dragons killed
]

play_dragon_battleground = input("Would you like to play Dragon Battleground [y|n] ? ")
while play_dragon_battleground not in ["y", "n"]:
    print("Please enter either 'y' or 'n'.\n")
    play_dragon_battleground = input(
        "Would you like to play Dragon Battleground [y|n] ? "
    )
# num_battles = input("Please enter number of battle rounds: ")
while play_dragon_battleground == "y":
    num_battles = input("Please enter number of battle rounds: ")
    while num_battles.isdigit() == False or int(num_battles) not in range(1, 6):
        print("Must be between an integer from 1 to 5 inclusive.\n")
        num_battles = input("Please enter number of battle rounds: ")
    print(
        f"-- Battke -- Player versus Dragon: {num_battles}"
    )  # Display number of rounds in battle between player versus dragon

    turn = "Player"  # Stores which turn it is values could be 'Plahyer' | 'Dragon'
    game_result[0] += 1  # Adds 1 to number of games
    loop_index = 0
    while loop_index != int(num_battles) and player_health >= 0 and dragon_health >= 0:
        print(f"Round {loop_index+1}")  # Display Number of Round
        # Total Damage = Adding every number of rolling 5 six-sided dice
        total_damage = 0
        current_damage = 0
        player_roll = []  # List of value of six-sided dices
        dice_count = [0, 0, 0, 0, 0, 0]
        num_of_rolls = 5
        for damage_count in range(num_of_rolls):
            damage_value = random.randint(1, 6)
            total_damage += damage_value
            player_roll.append(damage_value)
            dice_count[damage_value - 1] += 1

        # Using sets to manipulate list of dices to simplify algorithm
        dice_count_no_duplication = list(
            set(player_roll)
        )  # Gets rid of any duplication in the list

        # Standard Roll (All different values)
        if total_damage == 21:
            # if each dice values 1-6 are unique, total die must be equal to (1+2+3+4+5+6) = 21
            current_damage = total_damage
            print("-- Hit - Normal Damage!")

        # Three of a kind Roll
        if 3 in dice_count:
            dice_count_key = dice_count.index(3)  # Grabs the key that has a value of 3
            if dice_count_key in [1, 3, 5]:
                # Roll: Three of a kind (swing and miss) => Three dice have the same face value and the other two have different values. If three of a kind is 1, 3 or 5, then no damage inflicted.
                current_damage = 0
                print("-- Swing and miss - no damage inflicted!")
            elif len(dice_count_no_duplication) == 2:
                # TODO: What if there are 3 same dice values and a pair present on a rolled dice?

                current_damage = total_damage
                print("-- Hit - Normal Damage!")

            elif len(dice_count_no_duplication) == 3:
                # Roll: Three of a kind (critical hit) => Three dice have the same face value and the other two have different values. Triple the damage dealt.
                current_damage = total_damage * 3
                print("-- Critical hit - triple the damage!")
            else:
                # Wont be reached due to only 5 six-dices or are used
                current_damage = total_damage

        # Pair (hit)
        if 2 in dice_count:
            if len(dice_count_no_duplication) == 4:
                # If there is a pair and the rest are different values, current_damage must be 38
                current_damage = total_damage * 2
                print("-- Hit - double the damage!")
            else:
                current_damage = total_damage

        # 4 or Full similar dice
        if 4 in dice_count or 5 in dice_count:
            current_damage = total_damage
            print("-- Hit - Normal Damage!")

        print(f"{turn} rolled:")
        dice.display_dice(player_roll)
        if turn == "Player":  # human attacks dragon by amount of current_damage
            dragon_health -= current_damage
            turn = "Dragon"  # turns waps to dragon after player's turn
            print(
                f"> Dragon - Damage taken: {current_damage} - Current health: {player_health}"
            )

        else:  # if turn is 'dragon', dragon attacks human by amount of current_damage
            player_health -= current_damage
            turn = "Player"  # turn swaps to player after dragon's turn
            print(
                f"> Player - Damage taken: {current_damage} - Current health: {player_health}"
            )

        loop_index = loop_index + 1  # Increases loop_index preventing infinite loops

    # Divider
    print("\n")

    # Death Results
    if player_health <= 0:
        print("-- Player has died!   :(")
    elif dragon_health <= 0:
        print("-- Dragon has died!   :(")
        game_result[4] += 1

    # Divider
    print("\n")

    # Battle Results
    if (
        player_health <= 0 and dragon_health <= 0
    ) or player_health == dragon_health:  # If the healths of player and dragon are less than 0 or equal to 0, battle ends as draw. If player and dragon's health are same, battle ends as draw
        print("** Draw! **")
        game_result[3] += 1  # Player and Dragon Draw! Adds 1 to Game Draw count
    elif (
        player_health > dragon_health
    ):  # If player's health is greater than dragon's health, player wins!
        print("** Player wins! **")
        game_result[1] += 1  # Player wins add 1 to Game Win count
    else:  # Otherwise if dragon's health is greater than player's health, dragon wins!
        print("** Dragon wins!** ")
        game_result[2] += 1  # Player lost add 1 to Game Lost count

    print("-- End of battle --")

    # Don't display "play again input" if player or dragon died
    if player_health <= 0 or dragon_health <= 0:
        play_dragon_battleground = "n"
    else:
        play_dragon_battleground = input("Play again [y|n]? ")
        
# Divider
print("\n\n")

print("Game Summary")
print("=" * 15)
print(f"You played {game_result[0]} games")
print(f"    |--> Games won:     {game_result[1]}")
print(f"    |--> Games lost:    {game_result[2]}")
print(f"    |--> Games drawn:   {game_result[3]}")
print(f"    |--> Dragons killed:  {game_result[4]}")
print("Thanks for playing!")
