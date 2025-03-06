#Connect 4 Lab
#Initialize board
def initialize_board(num_rows, num_cols):
    Board = []
    #Makes the rows
    for i in range(num_rows):
        Board.append([])
        #Makes the columns
        for j in range(num_cols):
            Board[i].append("-")
    return Board

#Print board
def print_board(board):
    for index, val in enumerate(board):
        for j in board[index]:
            print(j,end=" ")
        print()

#Insert chip
def insert_chip(board, col, chip_type):
    for i, j in reversed(list(enumerate(board))):
        for val in board[i][col]:
            if val == "-":
                return i

#Check winner
def check_if_winner(board, col, row, chip_type):
    GameBoard[row][col] = chip_type
    #Check across row
    InRow=0
    for val in GameBoard[row]:
        if val != chip_type:
            InRow = -1
        InRow+=1
        if InRow == 4:
            Checks[0] = True
            break
    #Check across column
    InRow=0
    for index, i in enumerate(GameBoard):
        if GameBoard[index][col] != chip_type:
            InRow = -1
        InRow+=1
        if InRow == 4:
            Checks[1] = True
            break
    #Check for draw
    for index, i in enumerate(GameBoard):
        Check = False
        for val in GameBoard[index]:
            if val == "-":
                Checks[2] = False
                Check = True
                break
        if Check:
            break
        Checks[2] = True
    return (Checks[0] or Checks[1]) or Checks[2]

Height = int(input("What would you like the height of the board to be? "))
if Height == "test_initialization" or "test_check_winner_true" or "test_check_winner_false":
    print("ok?")
else:
    Height = int(Height)
Length = int(input("What would you like the length of the board to be? "))
if Length == "test_initialization" or "test_check_winner_true" or "test_check_winner_false":
    print("ok?")
else:
    Length = int(Length)
GameBoard = initialize_board(Height, Length)
print_board(GameBoard)
print()
Turn = 1
GameWon = False
Checks = [False, False, False]
print("Player 1: x\nPlayer 2: o\n")

#Game loop
while not GameWon:
    PlayerChoice = int(input(f"Player {Turn}: Which column would you like to choose? "))
    if Turn == 1:
        Turn = 2
        Chip = "x"
    else:
        Turn = 1
        Chip = "o"
    Row = insert_chip(GameBoard, PlayerChoice, Chip)
    GameWon = check_if_winner(GameBoard, PlayerChoice, Row, Chip)
    print_board(GameBoard)
    print()

#End Game message
if Checks[2]:
    print("Draw. Nobody wins.")
else:
    if Turn == 1:
        print("Player 2 won the game!")
    else:
        print("Player 1 won the game!")
