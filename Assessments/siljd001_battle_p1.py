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

import random
import dice  # Import dice module to display the die face values to the screen

# Player and Dragon's Health
player_health = 100
dragon_health = 100

# Total Damage = Adding every number of rolling 5 six-sided dice
total_damage = 0
all_dice = []  # List of value of six-sided dices
dice_counter = {}
num_of_dices = 5  # No. of six-sided dice
for damage_count in range(num_of_dices):
    damage_value = random.randint(1, 6)
    total_damage += damage_value
    all_dice.append(damage_value)
    if damage_value in dice_counter:
        dice_counter[damage_value] += 1
    else:
        dice_counter[damage_value] = 1


# Manipulate Dices to debug errors
all_dice = [1, 1, 1, 4, 3]
dice_counter = {1: 3, 3: 1, 4: 1}

print(dice_counter)

current_damage = 0  # Current Damage for each round

# Standard Roll (All different values)
if total_damage == 21:
    # if each dice values 1-6 are unique, total die must be equal to (1+2+3+4+5+6) = 21
    current_damage = 17

# Three of a kind Roll
if 3 in dice_counter.values():
    dice_counter_key = list(dice_counter.keys())[
        list(dice_counter.values()).index(3)
    ]  # Grabs the key that has a value of 3
    if dice_counter_key in [
        1,
        3,
        5,
    ]:
        # Roll: Three of a kind (swing and miss) => Three dice have the same face value and the other two have different values. If three of a kind is 1, 3 or 5, then no damage inflicted.
        current_damage = 0

    elif len(dice_counter) == 2:
        # TODO: What if a pair and 3 same dice values are pressent?
        current_damage = total_damage
    elif len(dice_counter) == 3:
        # Roll: Three of a kind (critical hit) => Three dice have the same face value and the other two have different values. Triple the damage dealt.
        current_damage = 54
    else:
        # Wont be reached due to only 5 six-dices are used
        current_damage = total_damage

# Pair (hit)
# TODO: Work On Pair Rolls

# Displaying dice values
dice.display_dice(all_dice)

print("The current damage is", current_damage)
