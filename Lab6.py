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
    RowCheck = False
    ColCheck = False
    GameBoard[row][col] = chip_type
    #Check across row
    InRow=0
    for val in GameBoard[row]:
        if val != chip_type:
            InRow = -1
        InRow+=1
        if InRow == 4:
            RowCheck = True
            break
    #Check across column
    InRow=0
    for index, i in enumerate(GameBoard):
        if GameBoard[index][col] != chip_type:
            InRow = -1
        InRow+=1
        if InRow == 4:
            ColCheck = True
            break
    return RowCheck or ColCheck

Height = int(input("What would you like the height of the board to be? "))
Length = int(input("What would you like the length of the board to be? "))
GameBoard = initialize_board(Height, Length)
print_board(GameBoard)
print()
Turn = 1
GameWon = False
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
if Turn == 1:
    print("Player 2 won the game!")
else:
    print("Player 1 won the game!")