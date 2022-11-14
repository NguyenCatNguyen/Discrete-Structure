"""
Authour: Nguyen Cat Nguyen
KUID: 3077463
Date: Tuesday Nov 9, 2022
Assignment: Assignment 6
"""

"""
Sudoku puzzle solver step
- Function to read the file
- Create a list of list
- Create a function to check if the move is valid
- Create a function to solve the sudoku board using backtracking.
- If the board is solved, print the board
- If the board is not solved, print "No solution"
- Create a function to print the sudoku board
- Create a main function
"""

#Function to read the file and create a list of list
def read_file(filename):
    file = open(filename, "r")
    board = []
    for i in range(9):
        #Loop through each line and and append each line to the board.
        line = file.readline()
        board.append(line.split())
        for j in range(9):
            if board[i][j] == "_":
                board[i][j] = 0
            #Convert the string to int
            board[i][j] = int(board[i][j])
    file.close()
    return board

#Function to check if the move is valid.
def is_valid_move(board, row, col, num):
    #Check if the number is in the row
    for i in range(9):
        if board[row][i] == num:
            return False
    #Check if the number is in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    corner_row = row - row % 3
    corner_col = col - col % 3
    #Check if the number is in the 3x3 square
    for i in range(3):
        for j in range(3):
            if board[corner_row+i][corner_col+j] == num:
                return False
    return True

#Create a function to solve the sudoku board
def solve(board,row, col):
    #Check if the board is solved
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    
    if board[row][col] > 0:
        #If the cell is not empty, move to the next cell
        return solve(board, row, col+1)

    #Try all the numbers
    for num in range(1,10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve(board, row, col+1):
                return True
        
        board[row][col] = 0
    return False


#Function to print the sudoku board
def print_board(board):
    for row in board:
        print(row)
    print()

#Main function
def main(filename):
    #Line to separate the output
    print("="*40)
    print(f"{filename}:\n")
    board = read_file(filename)
    print_board(board)
    print("Board solution is: \n")
    if solve(board, 0, 0):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=" ")
            print()
        print()
    else:
        print("No solution")


#Execute the main function
main("puzzle1.txt")
main("puzzle2.txt")
main("puzzle3.txt")
main("puzzle4.txt")
main("puzzle5.txt")
