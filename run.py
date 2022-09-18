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
    if inp >= 1 and inp <= 9 and board[inp-1] == "-": #the first two Inp expression check is valid number 1-9
        board[inp-1] = var_player
    else:
        print("Player is already in that place!")   


#check for win or tie

while game_running:
    print_board(board)
    player_input(board)

#check for win or tie 2