# AI Assignment – Constraint Satisfaction Problems (CSP)

## Problem Statement

Implement and solve different problems using the Constraint Satisfaction Problem (CSP) framework. Each problem is modeled using variables, domains, and constraints, and solved using standard CSP techniques.

---

## Approach

* Problems are modeled as CSPs with:

  * Variables
  * Domains
  * Constraints
* Constraint propagation (AC-3) is used to reduce domains
* Backtracking search is used to find solutions
* Heuristics are applied to improve efficiency:

  * Minimum Remaining Values (MRV)
  * Forward Checking

---

## Problems Implemented

### 1. Map Coloring (Australia)

* Regions are treated as variables
* Colors are the domain
* Adjacent regions must have different colors
* Uses AC-3 and backtracking

---

### 2. Telangana District Map Coloring

* 33 districts modeled as variables
* Real-world adjacency used
* Uses 4 colors
* Demonstrates scalability of CSP

---

### 3. Sudoku Solver

* 81 variables (cells in a 9×9 grid)
* Domain: digits 1–9
* Constraints:

  * All rows, columns, and 3×3 boxes must satisfy Alldiff
* Uses AC-3 for preprocessing
* Backtracking with MRV and forward checking

---

### 4. Cryptarithmetic (TWO + TWO = FOUR)

* Letters represent unique digits
* Includes carry variables
* Constraints applied column-wise
* Uses backtracking with constraint checking

---

## Techniques Used

* Backtracking Search (DFS-based)
* Constraint Propagation (AC-3 Algorithm)
* Minimum Remaining Values (MRV)
* Forward Checking

---

## User Input

* Sudoku solver allows custom puzzle input
* Other problems run with predefined data

---

## Technologies Used

* Python
* VS Code

---

## Requirements

No external libraries required. Uses standard Python libraries.

---

## How to Run

1. Clone the repository
2. Navigate to the folder
3. Run any file:

```bash
python map_coloring.py
python telangana_coloring.py
python sudoku_solver.py
python cryptarithmetic.py
```

---

## Sample Output

Map Coloring:

```
WA    → Red
NT    → Green
SA    → Blue
...
```

Sudoku:

```
Solved Grid:
5 3 4 | 6 7 8 | 9 1 2
...
```

---

## Features

* Implements core CSP techniques from AIMA
* Works for both small and large problems
* Uses heuristics for efficiency
* Clear and modular implementation

---

## Conclusion

This assignment demonstrates how CSP techniques can be applied to different types of problems, ranging from simple map coloring to complex problems like Sudoku and cryptarithmetic. Constraint propagation and heuristics significantly reduce the search space and improve performance.

---

## Reference

Russell, S., Norvig, P.
Artificial Intelligence: A Modern Approach
Chapter 6 – Constraint Satisfaction Problems
