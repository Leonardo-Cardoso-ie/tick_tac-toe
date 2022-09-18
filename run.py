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


"""When horizon var is true, we can break out the loop"""

def horizontal_line(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True 
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
    elif board[6] == board[7] == board[8] and board[6] != "-": 
        winner = board[6] 
        return True


"""check the Rows"""

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-": 
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-": 
        winner = board[1]      
        return True 
    elif board[2] == board[5] == board[8] and board[2] != "-": 
        winner = board[2] 
        return True 

"""Add another global winner variable"""

def check_diagonal(board):
    global winner
if  board[0] == board[4] == board[8] and board[0] != "-": 
    winner = board[0]
    return True 
elif board[2] == board[4] == board[6] == board[2] != "-": 
    winner = board[2]
    return True   


#switch the player


#check for win or tie  

while game_running:
    print_board(board)
    player_input(board)




