board = ["-", "-" , "-",
        "-", "-" , "-",
        "-", "-" , "-" ]

""" Create variables"""       

var_player = "x"
var_winner = None
game_running = True

#print the tic toc toe game board
def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("----------")
    print(board[3] + "|" + board[2] + "|" + board[5])
    print("----------")
    print(board[6] + "|" + board[7] + "|" + board[8]) 


"""Take a player input and ad the function to return a value string"""

def player_input(board):
    inp = int(input("Type a number a number 1 between 9: "))

#check for win or tie

#switch the player

#check for win or tie 2