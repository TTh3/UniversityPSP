BOARD = [[]]
PLAYER_TURN = "O"
BOARD_SIZE = input("What is the board size of your tic tac toe board? e.g. 3 or 4 or 5: ")
# Validating the size of the board
# Checked for length of string must be 1
# Checked the instance of BOARD_SIZE if it is an integer
# Checked the value if its within range of 3 to 6
while len(BOARD_SIZE) != 1 or isinstance(BOARD_SIZE, int) or [3,4,5,6].count(int(BOARD_SIZE))==0:
    BOARD_SIZE = input("Please enter an integer between 3 to 6: ")

for row in range(int(BOARD_SIZE)):
    if row % 3 !=0:
        BOARD[0].append("")
    
def start_game ():
    return
    



