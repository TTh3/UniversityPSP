#
# File: siljd001_battle_p1.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Game of Dragon Battleground - Part 1
# This is my own work as defined by the University's Academic Misconduct policy.
#

import random
import dice  # Import dice module to display the die face values to the screen


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

    # Player and Dragon's Health
    player_health = 100
    dragon_health = 100

    # Divider
    print("")

    num_battles = input(
        "Please enter number of battle rounds: "
    )  # Determines the number of battle rounds

    # Prevents user inputting non-digit values and number values that are not within the range of 1 to 6.
    while num_battles.isdigit() == False or int(num_battles) not in range(1, 6):
        print("Must be between an integer from 1 to 5 inclusive.\n")
        num_battles = input("Please enter number of battle rounds: ")

    # Divider
    print("")

    print(
        f"-- Battle -- Player versus Dragon: {num_battles} rounds --"
    )  # Display number of rounds in battle between player versus dragon

    game_result[0] += 1  # Adds 1 to number of games
    loop_index = 0

    # If loop_index is not equal to integer value of num_battles (number of battle rounds) and player and dragon's health is not less than or equal to 0. Run loop below
    while loop_index != int(num_battles) and player_health >= 0 and dragon_health >= 0:

        # Divider
        print("")

        print(f"Round {loop_index+1}")  # Display Number of Round
        num_turns = 0  # There are 2 turns per battle round, it could be either player or dragon's turn
        turn = "Player"  # Stores which turn it is values could be 'Player' | 'Dragon'
        damage_store = [
            0,  # Damage Taken by Player
            0,  # Damage Taken by Dragon
        ]

        # If player and dragon haven't done their turns and player and dragon's health is not less than or equal to 0. Run while loop below.
        while num_turns <= 1 and player_health >= 0 and dragon_health >= 0:

            total_damage = (
                0  # Total Damage = Adding every number of rolling 5 six-sided dice
            )
            current_damage = 0  # Stores damage during roll damage calculation phase
            player_roll = []  # List of value of six-sided dices
            dice_count = [0, 0, 0, 0, 0, 0]
            num_of_rolls = 5

            for damage_count in range(
                num_of_rolls
            ):  # Purpose: Appends each random value of 5 dices to var dice_count
                damage_value = random.randint(1, 6)
                total_damage += damage_value
                player_roll.append(damage_value)
                dice_count[damage_value - 1] += 1 # Adds 1 to the index matching in dice_count. Since list indexing starts at 0, the damage_value must be decreased by 1.

            # Divider
            print("")

            print(f"{turn} rolled:")  # Prints whose turn, either Player or Dragon

            dice.display_dice(
                player_roll
            )  # Displays graphic of every rolled dice values in player_roll

            # Divider
            print("")

            # Using sets to manipulate list of dices getting rid of duplications
            dice_count_no_duplication = list(set(player_roll))

            # Standard Roll (All 5 different values)
            if len(dice_count_no_duplication) == 5:
                # If dice count has no duplication, deal total damage of dice values to opponent
                current_damage = total_damage
                print("-- Hit - Normal Damage!")
                print(f"-- {turn} has dealt {current_damage} damage")

            # Three of a kind Roll
            if 3 in dice_count and current_damage == 0:
                # Even if there are 3 same dice values, as long as current_damage has not been changed the if statement below runs. Implementing the statement (current_damage == 0) improves performance especially with more rolls.
                dice_count_key = dice_count.index(3) + 1
                # Grabs the key that has a value of 3. The value is added by 1 as indexing starts at 0
                if dice_count_key in [1, 3, 5]:
                    # Roll: Three of a kind (swing and miss) => Three dice have the same face value and the other two have different values. If three of a kind is 1, 3 or 5, then no damage inflicted.
                    current_damage = 0
                    print("-- Swing and miss - no damage inflicted!")
                    print(f"-- {turn} has dealt {current_damage} damage")
                elif len(dice_count_no_duplication) == 2:
                    # 3 same values and a pair results triple damage
                    current_damage = total_damage * 3
                    print("-- Critical Hit - triple the damage!")
                    print(f"-- {turn} has dealt {current_damage} damage")

                elif len(dice_count_no_duplication) == 3:
                    # Roll: Three of a kind (critical hit) => Three dice have the same face value and the other two have different values. Triple the damage dealt.
                    current_damage = total_damage * 3
                    print("-- Critical hit - triple the damage!")
                    print(f"-- {turn} has dealt {current_damage} damage")

                else:
                    # Wont be reached due to only 5 six-dices or are used
                    current_damage = total_damage

            # Pair (hit)
            if 2 in dice_count and current_damage == 0:
                # Even if 1 or more pairs are present, as long as current_damage has not been changed the if statement below runs
                if (
                    len(dice_count_no_duplication) == 4
                    or len(dice_count_no_duplication) == 3
                ):
                    # If there is a pair or 2 pairs, damage dealt is 38
                    current_damage = total_damage * 2
                    print("-- Hit - double the damage!")
                    print(f"-- {turn} has dealt {current_damage} damage")
                else:
                    # Wont be reached due to only 5 six-dices or are used
                    current_damage = total_damage

            # 4 or Full similar dice
            if 4 in dice_count or 5 in dice_count:
                current_damage = total_damage
                print("-- Hit - Normal Damage!")
                print(f"-- {turn} has dealt {current_damage} damage")

            # Stores current_damage in var damage_store for displaying after battle round
            if turn == "Player":
                dragon_health -= current_damage  # Damage deals to opponent
                turn = "Dragon"  # turn swaps to dragon after player's turn

                # If player's turn, damage dealt will be towards dragon. Dragon's damage taken count is stored at index 1 of var damage_store.
                damage_store[1] = current_damage
            else:
                player_health -= current_damage
                turn = "Player"  # turn swaps to player after dragon's turn

                # If dragon's turn, damage dealt will be towards player. Player's damage taken count is stored at index 0 of var damage_store.
                damage_store[0] = current_damage

            # Divider
            print("")

            # If statement below runs when turn is for Dragon OR Player or Dragon's health is less than or equal to 0
            if num_turns == 1 or player_health <= 0 or dragon_health <= 0:
                # Prints Damages taken per turn
                print(
                    f"> Player - Damage taken: {damage_store[0]} - Current health: {player_health}"
                )

                print(
                    f"> Dragon - Damage taken: {damage_store[1]} - Current health: {dragon_health}"
                )

                # Resetting damage store every battle round
                damage_store[0] = 0
                damage_store[1] = 0

            num_turns += 1  # Adds 1 to every battle round turn

        loop_index = loop_index + 1  # Increases loop_index preventing infinite loops

    # Divider
    print("\n")

    print("-- End of battle --")

    # Divider
    print("")

    # Death Results
    if (
        player_health <= 0
    ):  # if player's health is less than or equal to 0, then player is dead
        print("-- Player has died!   :(")
    elif (
        dragon_health <= 0
    ):  # if dragon's health is less than or equal to 0, then dragon is dead
        print("-- Dragon has died!   :(")
        game_result[4] += 1

    # Divider
    print("")

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
        print("** Dragon wins! **")
        game_result[2] += 1  # Player lost add 1 to Game Lost count

    # Divider
    print("")

    # User decides if they want to play again after Battle. If not, Game ends and is shown the Game Summary Display.
    play_dragon_battleground = input("Play again [y|n]? ")
    while play_dragon_battleground not in ["y", "n"]:

        # Divider
        print("")

        play_dragon_battleground = input("Please enter either 'y' or 'n': ")

# Divider
print("\n")

print("Game Summary")
print("=" * 12)
print(f"You played {game_result[0]} games")
print(f"    |--> Games won:     {game_result[1]}")
print(f"    |--> Games lost:    {game_result[2]}")
print(f"    |--> Games drawn:   {game_result[3]}")
print(f"    |--> Dragons killed:  {game_result[4]}")

# Divider
print("")

print("Thanks for playing! \n")
