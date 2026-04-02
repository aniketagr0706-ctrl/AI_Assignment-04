# AI Assignment – Constraint Satisfaction Problems (CSP)

## Problem Statement

Implement Constraint Satisfaction Problem (CSP) techniques to solve different types of problems such as map coloring, Sudoku, and cryptarithmetic. The goal is to model each problem using variables, domains, and constraints, and compute valid solutions.

---

## Approach

* Each problem is modeled using:

  * Variables
  * Domains
  * Constraints
* Constraint propagation (AC-3) is used to reduce domains
* Backtracking search is used to find solutions
* Heuristics are applied to improve efficiency:

  * Minimum Remaining Values (MRV)
  * Forward Checking
* Problems are solved using a combination of inference and search

---

## User Input

The programs support:

* Predefined problem instances (map coloring, cryptarithmetic)
* Custom input for Sudoku puzzles

---

## Technologies Used

* Python
* VS Code

---

## Requirements

No external libraries required. Uses standard Python modules.

---

## Project Structure

```
.
├── aus_map-colour.py
├── telangana_map-colour.py
├── sudoku.py
├── crypt-arithmetic.py
├── README.md
└── LICENSE
```

---

## How to Run

1. Clone the repository
2. Navigate to the folder
3. Run the required file:

```bash
python aus_map-colour.py
python telangana_map-colour.py
python sudoku.py
python crypt-arithmetic.py
```

---

## Sample Output

Map Coloring:
WA → Red
NT → Green
SA → Blue

Sudoku:
Solved Grid:
5 3 4 | 6 7 8 | 9 1 2
...

---

## Features

* Implements CSP framework from AIMA
* Uses AC-3 for constraint propagation
* Applies MRV and forward checking
* Works for both small and large problems
* Supports real-world and standard CSP examples

---

## Conclusion

This assignment demonstrates how different problems can be solved using CSP techniques. By combining constraint propagation with backtracking and heuristics, the search space is significantly reduced, making it possible to efficiently solve complex problems like Sudoku and cryptarithmetic.

---

## Q2: Sudoku as a CSP

* Modeled as 81 variables (cells)
* Domain: values 1 to 9
* Constraints:

  * Each row must have distinct values
  * Each column must have distinct values
  * Each 3×3 box must have distinct values
* Uses Alldiff constraint
* AC-3 reduces domains before search
* Backtracking completes the solution

---

## Q3: Cryptarithmetic Problem (TWO + TWO = FOUR)

* Each letter represents a unique digit
* Includes carry variables (C1, C2, C3)
* Constraints are applied column-wise
* Leading digits cannot be zero
* Alldiff constraint ensures unique assignments
* Backtracking is used to explore valid assignments

---

## Q4: Map Coloring

* Regions/districts are modeled as variables
* Colors are the domain
* Adjacent regions must have different colors
* Constraint graph represents adjacency
* AC-3 and backtracking are used to find solutions

---

## Reference

Russell, S., Norvig, P.
Artificial Intelligence: A Modern Approach
Chapter 6 – Constraint Satisfaction Problems
