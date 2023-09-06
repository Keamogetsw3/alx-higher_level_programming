#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard
"""

from sys import argv

if __name__ == "__main__":
    chessboard = []
    """ Initialize the chessboard """
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

    # Initialize the answer list
    for i in range(n):
        chessboard.append([i, None])

    def queen_exists_in_column(y):
        """ Check if a queen already exists in that column (y-value)"""
        for x in range(n):
            if y == chessboard[x][1]:
                return True
        return False

    def reject(x, y):
        """ Determine whether or not to reject the solution"""
        if queen_exists_in_column(y):
            return False
        i = 0
        while i < x:
            if abs(chessboard[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_chessboard(x):
        """ Clears the chessboard from the point of failure on"""
        for i in range(x, n):
            chessboard[i][1] = None

    def nqueens(x):
        """ Recursive backtracking function to find the solution"""
        for y in range(n):
            clear_chessboard(x)
            if reject(x, y):
                chessboard[x][1] = y
                if x == n - 1:  # Accepts the solution
                    print(chessboard)
                else:
                    nqueens(x + 1)  # Moves on to the next x-value to continue

    nqueens(0)
