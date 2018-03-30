# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Mary McGrail
# Created: 3/26/18

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
    ]
player = ""
row = 0
col = 0

def printBoard(loc00, loc01, loc02, loc10, loc11, loc12, loc20, loc21, loc22):
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
    return loc00, loc01, loc02, loc10, loc11, loc12, loc20, loc21, loc22

def getPlayerMove(row, col):
    #this works fine, can get values ok
    player = 1
    row = 0
    col = 0
    col = int(input("Enter the column (0-2) for Player 1's move:"))
    row = int(input("Enter the row (0-2) for Player 1's move:"))
    if col > 2:
        print("Please try to enter a value between 0-2 for the column")
        return False
    elif row > 2:
        print("Please try to enter a value between 0-2 for the row")
        return False
    elif col < 0:
        print("Please try to enter a value between 0-2 for the column")
        return False
    elif row < 0:
        print("Please try to enter a value between 0-2 for the row")
        return False
    else: 
        return (row, col)    

def markBoard(board, row, col, player,loc00, loc01, loc02, loc10, loc11, loc12, loc20, loc21, loc22):
    loc00 = ' '
    loc01 = ' '
    loc02 = ' '
    loc10 = ' '
    loc11 = ' '
    loc12 = ' '
    loc20 = ' '
    loc21 = ' '
    loc22 = ' '
    col = 0
    row = 0
    row, col = getPlayerMove(row, col)
    if col == 0:
        if row ==0:
            loc00 = "x"
            
        elif row == 1:
            loc01 = "x"
             
        elif row ==2:
            loc02 = "x"
            
    elif col == 1:
         if row == 0:
            loc10 = "x"
            
         elif row == 1:
            loc11= "x"
            
         elif row ==2:
            loc11 = "x"
            
    elif col == 2:
        if row == 0:
            loc20 = "x"
            
        elif row == 1:
            loc21 = "x"
            
        elif row == 2:
            loc22 ="x"
              
    return loc00, loc01, loc02, loc10, loc11, loc12, loc20, loc21, loc22


def hasBlanks(board):
    loc00 = ' '
    loc01 = ' '
    loc02 = ' '
    loc10 = ' '
    loc11 = ' '
    loc12 = ' '
    loc20 = ' '
    loc21 = ' '
    loc22 = ' '
    if loc00 == " ":
        return board
    elif loc01 == " ":
        return board
    elif loc02 == " ":
        return board
    elif loc10 == " ":
        return board
    elif loc11 == " ":
        return board
    elif loc12 == " ":
        return board
    elif loc20 == " ":
        return board
    elif loc21 == " ":
        return board
    elif loc22 == " ":
        return board
    else:
        print("Game Over!")
        return False
    
def main():
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
        ['|', loc00, '|', loc01, '|', loc02, '|'],
        ['|', loc10, '|', loc11, '|', loc12, '|'],
        ['|', loc20, '|', loc21, '|', loc22, '|']
        ]
    player = 1
    row = 0
    col = 0
    while hasBlanks(board):
        printBoard(loc00, loc01, loc02, loc10, loc11, loc12, loc20, loc21, loc22)
        markBoard(board,row,col,player, loc00, loc01, loc02, loc10, loc11, loc12, loc20, loc21, loc22)
        player = player % 2 + 1 # switch player for next turn
main()
 
