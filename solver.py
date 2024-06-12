# Representing a 9x9 Sudoku board, where 0 represents empty cells
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def is_valid(board, row, col, num):
    # Check if 'num' can be placed in the cell (row, col)
    for i in range(9):
        # Check the row and column
        if board[row][i] == num or board[i][col] == num:
            return False
    # Determine the starting indices of the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    # Check the 3x3 subgrid
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True


def solve_sudoku(board):
    # Iterate through each cell in the 9x9 board
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers from 1 to 9
                    if is_valid(board, row, col, num):  # Check if the number is valid
                        board[row][col] = num  # Place the number
                        if solve_sudoku(board):  # Recursively solve the board
                            return True
                        # Reset the cell if no solution found
                        board[row][col] = 0
                return False  # No valid number found, trigger backtracking
    return True  # All cells are filled correctly


def print_board(board):
    # Print the board in a readable format
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


# Solve the Sudoku puzzle and print the result
if solve_sudoku(sudoku_board):
    print_board(sudoku_board)
else:
    print("No solution exists")


# def load_sudoku_board(filename):
#     board = []
#     with open(filename, 'r') as file:
#         for line in file:
#             board.append([int(num) for num in line.split()])
#     return board


# sudoku_board = load_sudoku_board('sudoku.txt')
