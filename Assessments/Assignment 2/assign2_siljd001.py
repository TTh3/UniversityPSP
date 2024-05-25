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

    return player_list

# Function display_details()
def display_details():
    print("File     : assign2_siljd001.py")
    print("Author   : Jaylord Silverio")
    print("Stud ID  : 110445405")
    print("Email ID : siljd001")
    print("This is my own work as defined by the University's Academic Misconduct Policy.")
    
# Function display_players() - place your own comments here...  : )
def display_players(player_list):
    # Provides the spacing required for each text
    def text_spacing (total_space, text):
        return " "*(total_space-len(f'{text}'))+f"{text}"
    
        
    # This line will eventually be removed - used for development purposes only.
    print("In function display_players()")

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


### Place the rest of your function definitions here...  : )


### Define list to store player information
player_list = []


### Place your code here... : )


# Read player information from file and store in player_list
player_list = read_file("players.txt")


### you will remove some of the following code as it's been included for development purposes only...  : )

# Displaying details
display_details()

# Display player list to the screen to ensure read_file is working correctly
display_players(player_list)

# User Choice
USER_CHOICES = ["list", "buy", "search", "high", "add", "remove", "play", "chips", "quit"]
print("Please enter choice")
user_choice = input(f'{USER_CHOICES} :  ')

while user_choice not in USER_CHOICES:
    print("\n Not a valid command - please try again.", end="\n\n\n")
    print("Please enter choice")
    user_choice = input(f'{USER_CHOICES} :  ')


    

no_chips = 100
game_result = 0

# Plays one game of blackJack and assigns the result of the game and the chip balance
# to variables game_result and no_chips respectively.
game_result, no_chips = blackjack.play_one_game(no_chips)

# Display to the screen the result of play_one_game() – game result (value of 3, 1 or 0)
# and number of chips remaining.
print(game_result, no_chips)


print("\n\n-- Program terminating --\n")
