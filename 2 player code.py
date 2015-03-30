from random import randint

#Sets initial values for game
playerOnePts = 0
playerTwoPts = 0
playerOneMoves = 0
playerTwoMoves = 0
board = []
board2 = []

#Creates game board
for i in range(15):
    board.append(["O"]*15)

def print_board(board):
    for row in board:
        print (" ".join(row))

#Game starts
print ("*****************************")
print ("**  Let's play battleship  **")
print ("***************************** \n")

gameMode = int(input("Choose game mode: \n(1) Player vs. Computer \n(2) Player vs. Player"
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
    print_board(board) #Prints game board(ocean)
    for turn in range(100):
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
        print ("Turns taken", (turn + 1))
#Player vs. Player Mode
if gameMode == 2:
<<<<<<< HEAD
    players = [] #List for player's names
    #Player One's name and ship location
    player1 = input("Enter Player 1 Name:")
    players.append(player1)
    ship_row1 = int(input("Player 1, enter row location of your ship: "))
    ship_col1 = int(input("Player 1, enter column location of your ship: "))
    #Player Two's name and ship location
    player2 = input("Enter Player 2 Name:")
    players.append(player2)
    ship_row2 = int(input("Player 2, enter row location of your ship: "))
    ship_col2 = int(input("Player 2, enter column location of your ship: "))

    while True:
        #Player One's Turn
        playerOneGuess_row = int(input("Player 1 Guess Ship's Row: "))
        playerOneGuess_col = int(input("Player 1 Guess Ship's Column: "))
        if playerOneGuess_row == ship_row2 and playerOneGuess_col == ship_col2:
            board[playerOneGuess_row][playerOneGuess_col] = "#"
            print_board(board)
            playerOnePts += 1
            print ("Congratulations! You sank my battleship!")
            print ("Game Over!")
            print (players[0], " Points: ", playerOnePts)
            print (players[0], " Total Moves: ", playerOneMoves)
            break
        elif playerOneGuess_row not in range(15) or playerOneGuess_col not in range(15):
            print ("Oops, that's not even in the ocean.")
            playerOneMoves += 1
            print_board(board)
        elif board[playerOneGuess_row][playerOneGuess_col] == "X":
            print ("You guessed that already. Try again!")
            playerOneMoves += 1
            print_board(board)
        else:
            print ("You missed my battleship!")
            board[playerOneGuess_row][playerOneGuess_col] = "X"
            playerOneMoves += 1
            print_board(board)
        #Player Two's Turn
        playerTwoGuess_row = int(input("Player 2, guess ship's row:"))
        playerTwoGuess_col = int(input("Player 2, guess ship's column:"))
        if playerTwoGuess_row == ship_row1 and playerTwoGuess_col == ship_col1:
            board[playerTwoGuess_row][playerTwoGuess_col] = "#"
            playerTwoPts += 1
            playerTwoMoves += 1
            print_board(board)
            print ("Congratulations! You sank my battleship!")
            print ("Game Over!")
            break
        elif playerTwoGuess_row not in range(15) or playerTwoGuess_col not in range(15):
            print ("Oops, that's not even in the ocean.")
            playerTwoMoves += 1
            print_board(board)
        elif board[playerTwoGuess_row][playerTwoGuess_col] == "X":
            print ("You guess that location already.")
            playerTwoMoves += 1
            print_board(board)
        else:
            print ("You missed my battleship!")
            board2[playerTwoGuess_row][playerTwoGuess_col] = "X"
            playerTwoMoves += 1
            print_board(board)
=======
    players = []
    player1 = input("Enter Player 1 Name:")
    players.append(player1)
    player2 = input("Enter Player 2 Name:")
    players.append(player2)
    print (players) #Prints Players list for debugging purposes
    print_board(board)
    while ship_row != "#" and ship_col != "#":
        for player in players:
            playerOneGuess_row = int(input("Player 1: Guess Ship's Row: "))
            playerOneGuess_col = int(input("Player 1: Guess Ship's Column: "))
            if playerOneGuess_row == ship_row and playerOneGuess_col == ship_col:
                board[playerOneGuess_row][playerOneGuess_col] = "#"
                print_board(board)
                playerOnePts += 1
                print ("Congratulations! You sank my battleship!")
                print ("Game Over!")
                print (players[0], " Points: ", playerOnePts)
                print (players[0], " Total Moves: ", playerOneMoves)
                print (players[1], " Points: ", playerOnePts)
                print (players[1], " Total Moves: ", playerOneMoves)
                break
            elif playerOneGuess_row not in range(15) or playerOneGuess_col not in range(15):
                print ("Oops, that's not even in the ocean.")
                playerOneMoves += 1
                print_board(board)
            elif board[playerOneGuess_row][playerOneGuess_col] == "X":
                print ("You guessed that one already.")
                playerOneMoves += 1
                print_board(board)
            else:
                print ("You missed my battleship!")
                board[playerOneGuess_row][playerOneGuess_col] = "X"
                playerOneMoves += 1
                print_board(board)
            print (player1, "Turns:", playerOneMoves)
            print (player2, "Turns:", playerTwoMoves)
                
                    
                
>>>>>>> 0a2aed35a122f613d7be50c7f865548659d054e4
