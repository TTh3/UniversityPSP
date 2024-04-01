'''

Things to ask:
What would happen if user got 4 or 5 number of values equal?
What if there are 3 of a kind and the other 2 have the same value (pair?)

'''

#
# File: siljd001_battle_p1.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Game of Dragon Battleground
# This is my own work as defined by the University's Academic Misconduct policy.
#

import random
import dice # Import dice module to display the die face values to the screen

# Player and Dragon's Health
player_health = 100
dragon_health = 100

# Total Damage = Adding every number of rolling 5 six-sided dice
total_damage = 0
all_dice = []  # List of value of six-sided dices
num_of_dices = 5  # No. of six-sided dice
for damage_count in range(num_of_dices):
    damage_value =random.randint(1, 6)
    total_damage += damage_value
    all_dice.append(damage_value)

# Manipulate all_dice to debug results
all_dice = [3,3,3,4,1]

current_damage = 0 # Current Damage for each round

# Standard Roll (All different values)
if total_damage == 21: # if each dice values 1-6 are unique, total die must be equal to (1+2+3+4+5+6) = 21
    current_damage = 17

# Pair (hit) Roll (2 dice have the same value)
# non_pair_values = set(all_dice) 
non_duplicated = set(all_dice)
pair_values = set()
# The List stores non pair values, later it acts like a Set but keeps it's storing functionality as a List
pair_count = 0
# Stores every pair
for each_dice in non_duplicated:
    print('debig',each_dice in non_duplicated)
    # TODO: more time!
    if each_dice in pair_values:
        pair_count+=1
    else:
        pair_values.add(each_dice)
    # else:
    #     non_pair_values=list(set(non_pair_values))
    #     non_pair_values.append(all_dice[each_dice])
print(non_duplicated, pair_values,pair_count)
if len(non_duplicated)>=3: # Makes sure that there are 3 non pair values
    if pair_count==2:
        # [3,3,3,4,4]
        current_damage = 54
    elif pair_count==1:
        # Checks if there is only one pair
        current_damage=38

# Three of a kind (swing and miss)
if len(non_duplicated) == 2: # If there are dice counts of 3 to 2 same values or 4 to 1 same values
    if pair_count==2: # TODO: What if there are 3 of a kind and the other 2 have the same value (pair?)
        current_damage = 0
    elif pair_count==1:
        current_damage=54
        
    
        
    


dice.display_dice(all_dice)

print("The current damage is", current_damage)
