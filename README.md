# Sudoku Solver

This repository hosts a Python implementation of a Sudoku solver leveraging NumPy. The solver endeavors to address the vacant cells of a Sudoku puzzle utilizing fundamental constraint propagation methodologies .

## Table of Contents

- [Sudoku Solver](#sudoku-solver)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Usage](#usage)
  - [How It Works](#how-it-works)
  - [Future Plans](#future-plans)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

The Sudoku solver provided here attempts to solve Sudoku puzzles by iteratively filling in empty cells based on valid constraints. It employs a straightforward algorithm to identify potential values for each cell by considering the current state of the rows, columns, and 3x3 subgrids. 

## Requirements

- Python 3.x
- NumPy

## Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/Mugta1/sudokusolver.git
   cd sudokusolver
   ```

2. Verify NumPy installation:
   ```sh
   pip install numpy
   ```

3. Execute the solver:
   ```sh
   python sudokusolver.py
   ```


## How It Works

1. **Input Validation:** Initial scrutiny ensures the integrity of the Sudoku grid, confirming each row comprises precisely 9 elements.

2. **Potential Values Calculation:** For each empty cell (designated by 0), the program computes feasible values by assessing the current row, column, and 3x3 subgrid states.

3. **Constraint Propagation:** Intersection of potential values from the row, column, and 3x3 subgrid determines a unique value, if available, which is then assigned to the cell.

4. **Iterative Process:** Steps 2 and 3 iteratively execute until all cells are filled or no further deterministic assignments are feasible.

5. **Output:** The solved Sudoku grid is printed upon completion. It also prints the time used and the number of times the loop ran to solve the sudoku.


## Future Plans

- **Optimization:** Harness NumPy to condense codebase and bolster performance.
- **Graphical User Interface:** Integrate a **GUI** for enhanced user interaction.


## Contributing

Contributions are encouraged! Should you identify areas for enhancement or detect bugs, please initiate an issue or submit a pull request.

## License

This project is licensed under the MIT License. Refer to the [LICENSE](LICENSE) file for further details.



