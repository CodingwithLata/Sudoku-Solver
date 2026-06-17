def is_valid(board, row, col, num):

    # Check row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(board):

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                for num in range(1, 10):

                    if is_valid(board, row, col, num):

                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0

                return False

    return True


# 🔹 PRINT UNSOLVED SUDOKU (clean format)
def print_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                print(".", end=" ")
            else:
                print(board[i][j], end=" ")
        print()


# 🔹 Sudoku Puzzle (given)
board = [
    [0, 0, 5, 0, 8, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 8],
    [0, 0, 2, 3, 4, 0, 9, 0, 0],
    [3, 0, 6, 0, 0, 9, 8, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 8, 0, 0, 6, 0, 3],
    [0, 0, 3, 0, 1, 4, 5, 0, 0],
    [6, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 5, 0, 3, 0, 0]
]

# 🔹 STEP 1: Print unsolved puzzle
print("UNSOLVED SUDOKU:")
print_board(board)

# 🔹 STEP 2: Solve (optional)
choice = input("\nDo you want solution? (y/n): ")

if choice.lower() == 'y':
    if solve_sudoku(board):
        print("\nSOLVED SUDOKU:")
        for row in board:
            print(row)
    else:
        print("No solution exists")
    
