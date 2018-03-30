# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Mary McGrail
# Created: 3/26/18
symbol = [ " ", "x", "o" ]
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
    ]
player = ""
row = 0
col = 0
#where the first '' in row 1 has the identity [0][0]
#and the second '' in row 1 is [0][1] and so on
def printRow(row):
    # initialize output to the left border
    # for each square in the row...
    # add to output the symbol for this square followed by a border
    # print the completed output for this row
    
    pass
def printBoard(board):
    loc00 = ' '
    loc01 = ' '
    loc02 = ' '
    loc10 = ' '
    loc11 = ' '
    loc12 = ' '
    loc20 = ' '
    loc21 = ' '
    loc22 = ' '
    #eleven dashes for fully extended lines
    print("+-----------+")
    print('|', loc00, '|', loc01, '|', loc02, '|')
    print("+-----------+")
    print('|', loc10, '|', loc11, '|', loc12, '|')
    print("+-----------+")
    print('|', loc20, '|', loc21, '|', loc22, '|')
    print("+-----------+")
    pass
def markBoard(board, row, col, player):
    loc00 = ' '
    loc01 = ' '
    loc02 = ' '
    loc10 = ' '
    loc11 = ' '
    loc12 = ' '
    loc20 = ' '
    loc21 = ' '
    loc22 = ' '
    board = [
        [loc00, loc01, loc02],
        [loc10, loc11, loc12],
        [loc20, loc12, loc22]
        ]
    if player == 1:
        if col == 0:
            if row ==0:
               loc00 = "x"
            elif row == 1:
                loc01 = "x"
            elif row ==2:
                loc02 = "x"
        if col == 1:
            if row == 0:
                loc10 = "x"
            elif row == 1:
                loc11 = "x"
            elif row ==2:
                loc12 = "x"
        if col == 2:
            if row == 0:
                loc20 = "x"
            if row == 1:
                loc21 = "x"
            if row == 2:
                loc22 = "x"
    return board   
def getPlayerMove(row, col):
    player = 1
    row = 0
    col = 0
    col = int(input("Enter the column (0-2) for Player 1's move:"))
    row = int(input("Enter the row (0-2) for Player 2's move:"))
    if col > 2:
        print("Please try to enter a value between 0-2 for the column")
    elif row > 2:
        print("Please try to enter a value between 0-2 for the column")
    elif col < 0:
        print("Please try to enter a value between 0-2 for the column")
    elif row < 0:
        print("Please try to enter a value between 0-2 for the column")
    else: 
        return (row, col)
    
def hasBlanks(board):
    # for each row in the board...
    # for each square in the row...
    # check whether the square is blank
    # if so, return True
    return True # if no square is blank, return False
def main():
    board = [] # TODO replace this with a three-by-three matrix of zeros
    player = 1
    row = 0
    col = 0
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove(row, col)
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn
main()
