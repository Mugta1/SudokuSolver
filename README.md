# Sudoku Solver

🚧 **Disclaimer: This software is currently under active development and its functionality may vary.** 🚧

This repository hosts a Python implementation of a Sudoku solver leveraging NumPy. The solver endeavors to address the vacant cells of a Sudoku puzzle utilizing fundamental constraint propagation methodologies.

## Table of Contents

- [Sudoku Solver](#sudoku-solver)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Usage](#usage)
  - [How It Works](#how-it-works)
  - [Limitations](#limitations)
  - [Future Plans](#future-plans)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

The Sudoku solver herein aims to resolve the unfilled cells of a Sudoku grid. Employing a rudimentary algorithm, the program evaluates potential values for each empty cell based on the extant state of the rows, columns, and 3x3 subgrids.

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

The Sudoku grid is currently hardcoded in the `sudokusolver.py` file. You can modify the initial grid by altering values within the `sudoku` array.

## How It Works

1. **Input Validation:** Initial scrutiny ensures the integrity of the Sudoku grid, confirming each row comprises precisely 9 elements.

2. **Potential Values Calculation:** For each empty cell (designated by 0), the program computes feasible values by assessing the current row, column, and 3x3 subgrid states.

3. **Constraint Propagation:** Intersection of potential values from the row, column, and 3x3 subgrid determines a unique value, if available, which is then assigned to the cell.

4. **Iterative Process:** Steps 2 and 3 iteratively execute until all cells are filled or no further deterministic assignments are feasible.

5. **Output:** The solved Sudoku grid is printed upon completion.

## Limitations

- The present implementation may not resolve all Sudoku puzzles, particularly those necessitating advanced strategies beyond basic constraint propagation.
- Potential infinite loops could occur if the algorithm fails to converge on a solution.
- The code lacks optimization and exhibits verbose, protracted lines.
- Present codebase readability and maintainability are suboptimal.

## Future Plans

- Harness NumPy to condense codebase and bolster performance.
- Enhance algorithmic efficiency to tackle more intricate Sudoku puzzles.
- Refactor codebase to enhance clarity and maintainability.
- Integrate a graphical user interface (GUI) for enhanced user interaction.
- Implement advanced Sudoku solving strategies to accommodate diverse puzzle complexities.

## Contributing

Contributions are encouraged! Should you identify areas for enhancement or detect bugs, please initiate an issue or submit a pull request.

## License

This project is licensed under the MIT License. Refer to the [LICENSE](LICENSE) file for further details.

