from random import randint
from itertools import cycle 

board = [] # Where the board will be stored

for i in range(10): # determines the size of our board
    board.append(["O"]*10)
  
def print_board(board): # Turns the board into a grid
    for row in board:
        print (" ".join(row))
      
print ("Let's play battleship")
player1 = input("Enter Player 1 Name: ")
player2 = input("Enter Player 2 Name: ")
print_board(board)

def random_row(board): # Sets the horizontal location of our battleship
  return randint(0, len(board) -1)

def random_col(board): # Sets the vertical location of our battleship
  return randint(0, len(board) -1)

ship_row1 = random_row(board) #Ship 1
ship_col1 = random_col(board) 

ship_row2 = random_row(board) #Ship 2
ship_col2 = random_col(board)

print (ship_row1)
print (ship_col1)

print (ship_row2)
print (ship_col2)

for turn in range(4): # The number of turns the player gets
    print ("Your Guess ", (player1))
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Column:"))

    if guess_row == ship_row1 and guess_col == ship_col1: # If player guesses correctly
        print ("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = "*"
        break
    elif guess_row not in range(10) or guess_col not in range(10): # If player guesses outside of the grid
        print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X": # If a player's guess is the same as a previous guess
        print ("You guessed that one already.")
    else:                                       # If a player misses the battleship
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        if turn == 3:
            print ("You have used all your turns.")
            break
    print (" Took Turn ", (turn + 1)) # Prints number of guesses 
    print_board(board)

for turn in range(4): # The number of turns the player gets
    print (" Your Guess ", (player2))
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Column:"))

    if guess_row == ship_row2 and guess_col == ship_col2: # If player guesses correctly
        print ("Congratulations! You sunk my battleship!")
        print ("Game Over!")
        board[guess_row][guess_col] = "*"
        break
    elif guess_row not in range(10) or guess_col not in range(10): # If player guesses outside of the grid
        print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X": # If a player's guess is the same as a previous guess
        print ("You guessed that one already.")
    else:                                       # If a player misses the battleship
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        if turn == 3:
            break
    print (" Took Turn ", (turn + 1)) # Prints number of guesses
    print_board(board)
