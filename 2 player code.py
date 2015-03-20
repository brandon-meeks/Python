from random import randint
from itertools import cycle

#Sets initial values for game
playerOnePts = 0
playerTwoPts = 0
playerOneMoves = 0
playerTwoMoves = 0
board = []

#Creates game board
for i in range(15):
    board.append(["O"]*15)

def print_board(board):
    for row in board:
        print (" ".join(row))

#Game starts
print ("Let's play battleship \n")

gameMode = int(input("Choose game mode: \n1 Player vs. Computer \n2 Player vs. Player"
                 "\nEnter game mode: "))

#Player vs. Computer Mode
def random_row(board):
    return randint(0, len(board) -1)

def random_col(board):
    return randint(0, len(board) -1)

#Ships location for Player vs. Computer
ship_row = random_row(board)
ship_col = random_col(board)

#Ships location for Player vs. Player


#Used for debugging (will print ships location)
print (ship_row)
print (ship_col)

#Code for Player's turn vs. Computer
if gameMode == 1:
    playerName = input("Enter Player's Name:")
    print_board(board)
    for turn in range(4):
        guess_row = int(input("Guess Ship's Row: "))
        guess_col = int(input("Guess Ship's Column: "))
        if guess_row == ship_row and guess_col == ship_col:
            board[guess_row][guess_col] = "#"
            playerOnePts += 1
            playerOneMoves += 1
            print_board(board)
            print ("Congratulations! You sank my battleship!")
            print ("Game Over!")
            print (playerName, " Points: ", playerOnePts)
            print (playerName, " Total Moves: ", playerOneMoves)
            break
        elif guess_row not in range(15) or guess_col not in range(15):
            print ("Oops, that's not even in the ocean.")
            playerOneMoves += 1
            print_board(board)
        elif board[guess_row][guess_col] == "X":
            print ("You guessed that already. Try again!")
            playerOneMoves += 1
            print_board(board)
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            playerOneMoves += 1
            print_board(board)
            if turn == 3:
                print ("You used up all your turns! \nGame Over!")
                print (playerName, " Total Moves: ", playerOneMoves)
                print (playerName, " Points: ", playerOnePts)
        print ("Turns taken", (turn + 1))
                

#Player vs. Player Mode
if gameMode == 2:
    players = []
    player1 = input("Enter Player's Name:")
    players.append(player1)
    player2 = input("Enter Player's Name:")
    players.append(player2)
    print (players)
    for player in players:
        playerOneGuess_row = int(input("Guess Ship's Row: "))
        playerOneGuess_col = int(input("Guess Ship's Column: "))
        playerTwoGuess_row = int(input("Guess Ship's Row: "))
        playerTwoGuess_col = int(input("Guess Ship's Column: "))
        for i in range(4):
            if playerOneGuess_row == ship_row and playerOneGuess_col == ship_col:
                board[guess_row][guess_col] = "#"
                print_board(board)
                playerOnePts += 1
                print ("Congratulations! You sank my battleship!")
                print ("Game Over!")
                print (players[0], " Points: ", playerOnePts)
                print (players[0], " Total Moves: ", playerOneMoves)
                break
            elif playerTwoGuess_row == ship_row and playerTwoGuess_col == ship_col:
                board[guess_row][guess_col] = "#"
                print_board(board)
                playerTwoPts += 1
                print ("Congratulations! You sank my battleship!")
                print ("Game Over!")
                print (players[1], " Points: ", playerOnePts)
                print (players[1], " Total Moves: ", playerOneMoves)
                break
