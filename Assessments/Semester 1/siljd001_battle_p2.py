#
# File: siljd001_battle_p2.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Assignment 1 - Game of Dragon Battleground - Part 2
# This is my own work as defined by the University's Academic Misconduct policy.
#

import random  # Used for generating random integers


# Display Details
def display_details():
    print("File: siljd001_battle_p2.py")
    print("Author: Jaylord Silverio")
    print("Stud ID: 110445405")
    print("Email Id: siljd001@mymail.unisa.edu.au")
    print("File: siljd001_battle_p2.py")


def roll_die():
    random_generator = random.randint(1, 6)
    return random_generator


die = roll_die()


def roll_damage(max_dice):
    player_roll = []
    for damage_count in range(max_dice):
        player_roll.append(roll_die()) # Append each rolled die value to player_roll list
    return player_roll


def calculate_damage(hand):
    current_damage = 0
    total_damage = 0
    dice_count = [0, 0, 0, 0, 0, 0]
    for val in hand:
        total_damage += val
        dice_count[val - 1] += 1

    # Using sets to manipulate list of dices getting rid of duplications
    dice_count_no_duplication = list(set(hand))

    # Standard Roll (All 5 different values)
    if len(dice_count_no_duplication) == 5:
        # If dice count has no duplication, deal total damage of dice values to opponent
        current_damage = total_damage

        # Three of a kind Roll
    if 3 in dice_count and current_damage == 0:
        # Even if there are 3 same dice values, as long as current_damage has not been changed the if statement below runs. Implementing the statement (current_damage == 0) improves performance especially with more rolls.
        dice_count_key = dice_count.index(3) + 1
        # Grabs the key that has a value of 3. The value is added by 1 as indexing starts at 0
        if dice_count_key in [1, 3, 5]:
            # Roll: Three of a kind (swing and miss) => Three dice have the same face value and the other two have different values. If three of a kind is 1, 3, 5 current_damage = 0
            current_damage = 0
        elif len(dice_count_no_duplication) == 2:
            # 3 same values and a pair results triple damage
            current_damage = total_damage * 3

        elif len(dice_count_no_duplication) == 3:
            # Roll: Three of a kind (critical hit) => Three dice have the same face value and the other two have different values. Triple the damage dealt.
            current_damage = total_damage * 3

        else:
            # Wont be reached due to only 5 six-dices or are used
            current_damage = total_damage

        # Pair (hit)
    if 2 in dice_count and current_damage == 0:
        # Even if 1 or more pairs are present, as long as current_damage has not been changed the if statement below runs
        if len(dice_count_no_duplication) == 4 or len(dice_count_no_duplication) == 3:
            # If there is a pair or 2 pairs, damage dealt is 38
            current_damage = total_damage * 2

        else:
            # Wont be reached due to only 5 six-dices or are used
            current_damage = total_damage

    # 4 or Full similar dice
    if 4 in dice_count or 5 in dice_count:
        current_damage = total_damage

    return current_damage
