#
#  PSP Assignment 2, SP2 2024 - Provided file (assign2_yourEmailId.py).
#  Remove this and place appropriate file comments here.
#
#  Modify this file to include your code solution.
#
#
# Write your code and function definitions in this file.
# Place your own comments in this file also.
#


import blackjack

# FIXME: DELETE below before submission!
import sys

sys.dont_write_bytecode = True


# Function read_file() - place your own comments here...  : )
def read_file(filename):

    player_list = []
    index = 0

    infile = open(filename, "r")
    # Read first line of file.
    line = infile.readline()

    # While not end of file reached i.e. empty string not returned from readline method.
    while line != "":

        # Read name
        name = line.strip("\n")

        # Read in next line
        line = infile.readline()

        # Split line into games played, no won, no lost, etc
        info_list = line.split()
        games_played = int(info_list[0])
        no_won = int(info_list[1])
        no_lost = int(info_list[2])
        no_drawn = int(info_list[3])
        chips = int(info_list[4])
        total_score = int(info_list[5])

        # Create new player list with player info
        new_player = [name, games_played, no_won, no_lost, no_drawn, chips, total_score]

        # Add new player to player_list list
        player_list.append(new_player)

        # Read next line of file.
        line = infile.readline()
    infile.close()

    return player_list

# Function write_to_file(filename,player_list)
def write_to_file(filename, player_list):
    outfile = open(filename, 'w')
    for player in player_list:
        outfile.write(player[0]+"\n"+f'{player[1]} {player[2]} {player[3]} {player[4]} {player[5]} {player[6]}\n') 
    outfile.close()
# Function display_details()
def display_details():
    print("File     : assign2_siljd001.py")
    print("Author   : Jaylord Silverio")
    print("Stud ID  : 110445405")
    print("Email ID : siljd001")
    print("This is my own work as defined by the University's Academic Misconduct Policy. \n\n")
    
# Function display_players() - place your own comments here...  : )
# list
def display_players(player_list):
    # Provides the spacing required for each text
    def text_spacing (total_space, text):
        return " "*(total_space-len(f'{text}'))+f"{text}"
    
    print() # Space for top
    # Place your code here
    print("===========================================================")
    print("-                     Player Summary                      -")
    print("===========================================================")
    print("-                             P  W  L  D   Chips   Score  -")
    print("-----------------------------------------------------------")
    for player in player_list:
        print(
            f"-  {player[0]+" "*(26-len(player[0]))}{text_spacing (2,player[1])} {text_spacing (2,player[2])} {text_spacing (2,player[3])} {text_spacing (2,player[4])}{text_spacing (7,player[5])}{text_spacing(9,player[6])} -"
        )
        print("----------------------------------------------------------")

    print("===========================================================")
    print() # Space for bottom

### Place the rest of your function definitions here...  : )

# Finds player inside list of players, returns the index if found.
#  command
def find_player(player_list, name): # search
    for player_index in range(len(player_list)):
        if player_list[player_index][0] == name:
            return player_index
        
    # If player name is not found in player list return -1
    return -1
  
# add 
def add_player(player_list,name): # add
    new_players=[*player_list, [name, 0, 0, 0, 0, 100, 0]]
    print(f"\nSuccessfully added {name} to player list.\n\n")
    return new_players
# remove
def remove_player(player_list, name): # remove
    player_index = find_player(player_list, name)
    player_list.remove(player_list[player_index])

    return player_list
# high
def display_highest_chip_holder(player_list): # high
    highest_chips = int(player_list[0][5]) 
    highest_player_index = 0
    for player in range(len(player_list)):
        chips = int(player_list[player][5])
        if chips > highest_chips:
            highest_chips = chips
            highest_player_index = player
    print(f"Highest Chip Holder => {player_list[highest_player_index][0]} with {highest_chips} chips!\n")
    return highest_chips
# buy
def buy_player_chips(player_list, name): # buy
    active_player = player_list[find_player(player_list,name)]
    print(f"{name} currently has {active_player[5]} chips.\n")
    buy_prompt = input("How many chips would you like to buy? ")
    while buy_prompt.isdigit() == False or int(buy_prompt) not in range(1,100):
        print("You may only buy between 1-100 chips at a time!\n")
        buy_prompt = input("How many chips would you like to buy? ")
    active_player[5] = int(active_player[5]) + int(buy_prompt)
    player_list[find_player(player_list,name)] = active_player
    print(f"\nSuccessfully updated {name}'s chip balance to {active_player[5]}")

# play
def play_blackjack_games(player_list, player_pos): # play
    play_blackjack = 'y'
    while play_blackjack == "y":
        no_chips = player_list[player_pos][5]
        player = player_list[player_pos]
        game_result = 0

        # Plays one game of blackJack and assigns the result of the game and the chip balance
        # to variables game_result and no_chips respectively.
        game_result, no_chips = blackjack.play_one_game(no_chips)

        # Display to the screen the result of play_one_game() – game result (value of 3, 1 or 0)
        # and number of chips remaining.
        # print(type( game_result), no_chips, "\n")
        player[1] = int(player[1]) +1
        if game_result==3:
            player[2] = int(player[1]) + 1
        elif game_result==1:
            player[4] = int(player[2])+1
        else:
            player[3] = int(player[3])+1
        
        # Play again?
        play_blackjack = input("Play again [y|n]? ")
# chips
def sort_by_chips(player_list): # chips
    copied_list = player_list + []
    sorted_list = []
    while copied_list:
        maximum = copied_list[0]
        for x in copied_list: 
            if int(x[5]) > int(maximum[5]):
                maximum = x
        sorted_list.append(maximum)
        copied_list.remove(maximum)    
    return sorted_list

### Define list to store player information
player_list = []


### Place your code here... : )


# Read player information from file and store in player_list
player_list = read_file("players.txt")


### you will remove some of the following code as it's been included for development purposes only...  : )

# Displaying details
display_details()

# # Display player list to the screen to ensure read_file is working correctly
# display_players(player_list)

# User Choice
USER_CHOICES = ["list", "buy", "search", "high", "add", "remove", "play", "chips", "quit"]


play = "y"
while play == "y":
    print("Please enter choice")
    user_choice = input(f'{USER_CHOICES} :  ')
    print() # Divider
    
    # if user's function choice is not listed in the available choices, repeat prompt until validated.
    while user_choice not in USER_CHOICES:
        print(" Not a valid command - please try again.", end="\n\n\n")
        print("Please enter choice")
        user_choice = input(f'{USER_CHOICES} :  ')
        
    if user_choice == "list":
        display_players(player_list)
        
    elif user_choice == "buy": 
        # if user's choice is to buy:
        #       1. Search and Validate prompted name
        #       2. Run buy_player_chips function
        name_prompt = input("Please enter name: ")
        player_index = find_player(player_list, name_prompt)
        if player_index == -1:
            print(f"\n{name_prompt} is not found in player list. \n\n")
        else:
            buy_player_chips(player_list, name_prompt)
            
    elif user_choice == "search":
        name_prompt = input("Please enter name: ")
        player_index = find_player(player_list, name_prompt)
        if player_index == -1:
            print(f"\n{name_prompt} is not found in player list. \n\n")
        else:
            print(f"\n{name_prompt} stats:\n")
            print("P  W  L  D  Score")
            print(f"{player_list[player_index][1]}  {player_list[player_index][2]}  {player_list[player_index][3]}  {player_list[player_index][4]}  {player_list[player_index][6]}")
            print("\n")
    elif user_choice == "high":
        display_highest_chip_holder(player_list)
    elif user_choice == "add":
        name_prompt = input("Please enter name: ")
        player_index = find_player(player_list, name_prompt)
        if player_index != -1:
            print(f"\n{name_prompt} already exists in player list \n\n")
        else:
            player_list = add_player(player_list, name_prompt)
    elif user_choice == "remove":
        name_prompt = input("Please enter name: ")
        player_index = find_player(player_list, name_prompt)
        if player_index == -1:
            print(f"\n{name_prompt} is not found in players.\n\n")
        else:
            player_list = remove_player(player_list,name_prompt)
            print(player_list)
    elif user_choice == "play":
        name_prompt = input("Please enter name: ")
        player_index = find_player(player_list, name_prompt)
        if player_index == -1:
            print(f"\n{name_prompt} is not found in player list.\n\n")
        else:
            play_blackjack_games(player_list,player_index)
    elif user_choice == "chips":
        player_list = sort_by_chips(player_list)
        display_players(player_list)
        
    elif user_choice == "quit":
        play = "quit"
        
print("\n\n-- Program terminating --\n\n")
print("NOTE: Your program should output the following information to a file - new_players.txt.\n")
write_to_file("new_players.txt", player_list)

# Printing output new_players.txt
infile = open("new_players.txt", "r")
for eachLine in infile:
    print(eachLine, end="")
infile.close()


