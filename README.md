## Sudoku Game - Command Line Interface (CLI) and Graphical User Interface (GUI)

### Overview

This project implements a Sudoku game with both a Command Line Interface (CLI) and a Graphical User Interface (GUI). Sudoku is a popular logic-based number puzzle game where the objective is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids that compose the grid contain all of the digits from 1 to 9.

### Features

#### Command Line Interface (CLI)

1. **Generate Sudoku Board**:
   - Generates a complete and valid Sudoku board.
   - Supports various difficulty levels (easy, medium, hard, expert).

2. **Display Board**:
   - Prints the current state of the Sudoku board in a formatted manner.

3. **Solve Sudoku**:
   - Solves the Sudoku board using a backtracking algorithm.

4. **Check User Solution**:
   - Allows the user to input their solution and checks if it's correct.

5. **Provide Hint**:
   - Provides a hint by suggesting a valid number for a blank cell.

6. **Reset Board**:
   - Resets the board to its original state.

7. **Save and Load Board**:
   - Saves the current Sudoku board to a file.
   - Loads a Sudoku board from a saved file.

8. **Logging**:
   - Logs important actions and operations performed on the Sudoku board to a log file (`sudoku_log.txt`).

#### Graphical User Interface (GUI)

1. **Interactive Sudoku Board**:
   - Displays the Sudoku board graphically.
   - Allows the user to interact with the board by entering numbers and checking solutions.

2. **Options**:
   - New Game: Generates a new Sudoku board.
   - Solve: Automatically solves the Sudoku board.
   - Check Solution: Verifies the user-entered solution.
   - Hint: Provides a hint to solve the board.
   - Save and Load: Saves and loads Sudoku boards from files.
   - Difficulty Levels: Allows selection of difficulty levels (easy, medium, hard, expert).

3. **Feedback and Notifications**:
   - Provides feedback on the correctness of solutions and actions taken.
   - Displays notifications for successful operations and errors.

### Installation and Usage

#### Command Line Interface (CLI)

1. **Requirements**:
   - Python 3.x installed on your system.

2. **Setup**:
   - Clone or download the Python script `sudoku_cli.py`.

3. **Usage**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `sudoku_cli.py`.
   - Run the script using `python sudoku_cli.py`.
   - Follow the prompts and options displayed in the terminal.

#### Graphical User Interface (GUI)

1. **Requirements**:
   - Python 3.x installed on your system.
   - Tkinter library installed (usually included with Python).

2. **Setup**:
   - Clone or download the Python script `sudoku_gui.py`.

3. **Usage**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `sudoku_gui.py`.
   - Run the script using `python sudoku_gui.py`.
   - The Sudoku game window will open.
   - Interact with the Sudoku board using mouse clicks and keyboard inputs.
   - Use buttons and menus to perform actions like solving, checking, saving, and loading.

### Example Screenshots

- **CLI Example**:

![image](https://github.com/bittarwork/Sudoku/assets/81069087/a3cf585e-cedf-4632-93fd-9ab6526bdd18)

- **GUI Example**:

![image](https://github.com/bittarwork/Sudoku/assets/81069087/895f6713-2c6b-4e88-8166-7a5d3969d467)

### Contributors

- Developed by [Your Name]
- Contributions and improvements welcome! Fork the repository at [GitHub Repository URL].

### License

This project is licensed under the [License Name]. See the LICENSE file for details.

### Acknowledgments

- [List any acknowledgments or libraries used, if applicable.]

### Contact

For issues, questions, or suggestions, please contact [Your Email Address].

---

This README.md file provides an overview of the Sudoku game project, detailing its features, setup instructions, usage guidelines for both CLI and GUI versions, example screenshots, contributors, license information, acknowledgments, and contact details. Adjust the placeholders and sections as per your specific project details.
