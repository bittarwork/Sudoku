import random
import tkinter as tk
from tkinter import messagebox


class Sudoku:
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]
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

    def run_gui(self):
        root = tk.Tk()
        root.title("Sudoku")

        self.gui_board = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(root, width=2, font=(
                    'Arial', 18), textvariable=self.gui_board[i][j], justify='center')
                entry.grid(row=i, column=j, padx=5, pady=5)
                if self.board[i][j] != 0:
                    entry.insert(0, str(self.board[i][j]))
                    entry.config(state='readonly')
                self.entries[i][j] = entry

        btn_solve = tk.Button(root, text="Solve", command=self.solve_gui)
        btn_solve.grid(row=9, column=0, columnspan=3, sticky='ew')

        btn_check = tk.Button(root, text="Check Solution",
                              command=self.check_gui_solution)
        btn_check.grid(row=9, column=3, columnspan=3, sticky='ew')

        btn_reset = tk.Button(root, text="Reset", command=self.reset_gui)
        btn_reset.grid(row=9, column=6, columnspan=3, sticky='ew')

        root.mainloop()

    def solve_gui(self):
        if self.solve():
            for i in range(9):
                for j in range(9):
                    self.gui_board[i][j].set(str(self.board[i][j]))
        else:
            messagebox.showerror(
                "Error", "No solution exists for the given Sudoku.")

    def check_gui_solution(self):
        user_board = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                if val.isdigit():
                    user_board[i][j] = int(val)

        if self.check_user_solution(user_board):
            messagebox.showinfo(
                "Success", "Congratulations! Your solution is correct.")
        else:
            messagebox.showerror("Error", "Your solution is incorrect.")

    def reset_gui(self):
        for i in range(9):
            for j in range(9):
                if self.entries[i][j]['state'] != 'readonly':
                    self.gui_board[i][j].set("")


# Testing the enhanced Sudoku class with GUI
sudoku = Sudoku()
print("Generated Sudoku Board:")
sudoku.print_board()

print("\nUnsolved Sudoku Board (Medium Difficulty):")
unsolved_board = sudoku.create_unsolved_board("medium")
for row in unsolved_board:
    print(row)

# Assuming user_board is a user provided solution to be checked
user_board = [[cell for cell in row] for row in sudoku.board]
is_valid_solution = sudoku.check_user_solution(user_board)
print("\nUser solution is valid:", is_valid_solution)

# Saving the Sudoku board
sudoku.save_to_file("sudoku.txt")

# Running the Sudoku GUI
sudoku.run_gui()
