board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-" ]

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
print_board(board)    


#take player input

#check for win or tie

#switch the player

#check for win or tie 2