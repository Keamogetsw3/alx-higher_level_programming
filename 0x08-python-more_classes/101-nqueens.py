#!/usr/bin/python3
"""
N-Queens backtracking algorithm to find and print all possible solutions.

This program determines all valid configurations of N queens placed on an N×N
chessboard such that no two queens can attack each other.
"""

from sys import argv

if __name__ == "__main__":
    solutions = []

    # Validate command-line arguments
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)

    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the solution list with N rows
    for i in range(n):
        solutions.append([i, None])

    def already_exists(y):
        """Checks if a queen already exists in the given column (y)."""
        for x in range(n):
            if y == solutions[x][1]:
                return True
        return False

    def reject(x, y):
        """
        Determines whether placing a queen at position (x, y) is valid.

        A position is invalid if:
        - A queen already exists in column y.
        - The placement creates a diagonal conflict with a previously placed queen.
        """
        if already_exists(y):
            return False
        for i in range(x):
            if abs(solutions[i][1] - y) == abs(i - x):
                return False
        return True

    def clear_solutions(x):
        """Clears queen placements from row x onwards (backtracking step)."""
        for i in range(x, n):
            solutions[i][1] = None

    def nqueens(x):
        """
        Recursively attempts to place queens row by row using backtracking.

        If a valid placement is found for all rows, the solution is printed.
        Otherwise, the function continues searching for valid configurations.
        """
        for y in range(n):
            clear_solutions(x)
            if reject(x, y):
                solutions[x][1] = y
                if x == n - 1:  # If all queens are placed, print the solution
                    print(solutions)
                else:
                    nqueens(x + 1)  # Recur to place the next queen

    # Start the recursive process from row 0
    nqueens(0)
