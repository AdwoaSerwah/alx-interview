#!/usr/bin/python3
"""Main function to process the input and solve the N Queens problem."""
import sys


def print_solution(board):
    """Print the current solution board as a list of [row, col] pairs."""
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board):
    """Solve the N Queens problem using backtracking."""
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(N, row + 1, board)
            board[row] = -1  # Backtrack


def main():
    """Main function to process the input and solve the N Queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with -1 (no queens placed)
    board = [-1] * N
    solve_nqueens(N, 0, board)


if __name__ == "__main__":
    main()
