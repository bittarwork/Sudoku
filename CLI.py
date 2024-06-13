import random


class Sudoku:
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]
        self.original_board = None
        self.generate_sudoku()

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def generate_sudoku(self):
        def fill_board():
            def fill_cell(i, j):
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if self.is_valid(i, j, num):
                        self.board[i][j] = num
                        if (i == 8 and j == 8) or (j == 8 and fill_cell(i + 1, 0)) or fill_cell(i, j + 1):
                            return True
                        self.board[i][j] = 0
                return False

            return fill_cell(0, 0)

        while not fill_board():
            self.board = [[0] * 9 for _ in range(9)]
        self.original_board = [row[:] for row in self.board]

    def solve(self):
        def solve_board():
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] == 0:
                        for num in range(1, 10):
                            if self.is_valid(i, j, num):
                                self.board[i][j] = num
                                if solve_board():
                                    return True
                                self.board[i][j] = 0
                        return False
            return True

        return solve_board()

    def is_sudoku_valid(self):
        for row in range(9):
            for col in range(9):
                num = self.board[row][col]
                self.board[row][col] = 0
                if not self.is_valid(row, col, num):
                    return False
                self.board[row][col] = num
        return True

    def format_sudoku(self):
        formatted_board = []
        for row in range(9):
            formatted_row = ""
            for col in range(9):
                formatted_row += str(self.board[row][col]) + " "
                if (col + 1) % 3 == 0 and col != 8:
                    formatted_row += "| "
            formatted_board.append(formatted_row.strip())
            if (row + 1) % 3 == 0 and row != 8:
                formatted_board.append("- " * 11)
        return "\n".join(formatted_board)

    def save_to_file(self, filename):
        if self.is_sudoku_valid():
            formatted_board = self.format_sudoku()
            with open(filename, "w") as f:
                f.write(formatted_board)
            print(f"Sudoku board generated and saved to {filename}")
        else:
            print("Generated Sudoku board is not valid and will not be saved.")

    def print_board(self, unsolved=False):
        if unsolved:
            board_to_print = self.create_unsolved_board("medium")
        else:
            board_to_print = self.board

        for i, row in enumerate(board_to_print):
            if i % 3 == 0 and i != 0:
                print("- " * 11)
            row_str = ""
            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_str += "| "
                row_str += f"{num} "
            print(row_str)

    def create_unsolved_board(self, difficulty):
        difficulty_levels = {
            'easy': 35,
            'medium': 45,
            'hard': 55,
            'expert': 60
        }
        if difficulty not in difficulty_levels:
            raise ValueError(
                "Invalid difficulty level. Choose from 'easy', 'medium', 'hard', 'expert'.")

        num_to_remove = difficulty_levels[difficulty]
        unsolved_board = [row[:] for row in self.board]

        while num_to_remove > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if unsolved_board[row][col] != 0:
                backup = unsolved_board[row][col]
                unsolved_board[row][col] = 0

                self.board = [r[:] for r in unsolved_board]
                if self.solve():
                    num_to_remove -= 1
                else:
                    unsolved_board[row][col] = backup

        self.board = [r[:] for r in unsolved_board]
        return unsolved_board

    def check_user_solution(self, user_board):
        for row in range(9):
            for col in range(9):
                num = user_board[row][col]
                if not (1 <= num <= 9):
                    return False
                self.board[row][col] = 0
                if not self.is_valid(row, col, num):
                    return False
                self.board[row][col] = num
        return True

    def reset_board(self):
        self.board = [row[:] for row in self.original_board]

    def provide_hint(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(i, j, num):
                            self.board[i][j] = num
                            return (i, j, num)
        return None

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
            for i in range(9):
                self.board[i] = list(map(int, lines[i].strip().split()))
            self.original_board = [row[:] for row in self.board]
            print(f"Sudoku board loaded from {filename}")
        except Exception as e:
            print(f"Error loading Sudoku board from {filename}: {e}")

    def log_step(self, action, details):
        with open("sudoku_log.txt", "a") as log_file:
            log_file.write(f"{action}: {details}\n")


# Testing the enhanced Sudoku class with command line interface
if __name__ == "__main__":
    sudoku = Sudoku()
    print("Generated Sudoku Board:")
    sudoku.print_board()

    while True:
        print("\nOptions:")
        print("1. Display current board")
        print("2. Display unsolved board (select difficulty)")
        print("3. Solve the board")
        print("4. Check user solution")
        print("5. Provide a hint")
        print("6. Reset the board to original state")
        print("7. Save the board to a file")
        print("8. Load board from a file")
        print("9. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            sudoku.print_board()
        elif choice == '2':
            difficulty = input(
                "Select difficulty (easy, medium, hard, expert): ")
            unsolved_board = sudoku.create_unsolved_board(difficulty)
            for row in unsolved_board:
                print(row)
            sudoku.log_step("Create Unsolved Board",
                            f"Difficulty: {difficulty}")
        elif choice == '3':
            if sudoku.solve():
                print("Solved Sudoku Board:")
                sudoku.print_board()
            else:
                print("No solution exists for the given Sudoku.")
            sudoku.log_step("Solve Board", "Board solved")
        elif choice == '4':
            user_board = []
            print("Enter your solution row by row, with spaces between numbers:")
            for i in range(9):
                row = list(map(int, input().strip().split()))
                user_board.append(row)
            if sudoku.check_user_solution(user_board):
                print("Congratulations! Your solution is correct.")
            else:
                print("Your solution is incorrect.")
            sudoku.log_step("Check User Solution", "Solution checked")
        elif choice == '5':
            hint = sudoku.provide_hint()
            if hint:
                print(f"Hint: Place {
                      hint[2]} at position ({hint[0]}, {hint[1]})")
            else:
                print("No hints available.")
            sudoku.log_step("Provide Hint", f"Hint: {hint}")
        elif choice == '6':
            sudoku.reset_board()
            print("Board reset to original state.")
            sudoku.log_step("Reset Board", "Board reset to original state")
        elif choice == '7':
            filename = input("Enter filename to save the board: ")
            sudoku.save_to_file(filename)
            sudoku.log_step("Save Board", f"Board saved to {filename}")
        elif choice == '8':
            filename = input("Enter filename to load the board: ")
            sudoku.load_from_file(filename)
            sudoku.log_step("Load Board", f"Board loaded from {filename}")
        elif choice == '9':
            print("Exiting Sudoku program.")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 9.")
