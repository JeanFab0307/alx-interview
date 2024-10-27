#!/usr/bin/python3
'''solving nqueens problem'''
import sys


def is_valid(board, row, col):
    """
    Checks if a position of the queen is valid
    """
    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False

    return True


def solve_nqueens(board, row, solutions):
    """ return the same board with the solution"""
    n = len(board)
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, solutions)
            board[row] = -1


def main():
    """Check for correct argument count"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n
    solve_nqueens(board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
