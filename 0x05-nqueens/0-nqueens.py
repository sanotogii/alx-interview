#!/usr/bin/python3
"""initializing the board"""
import sys

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


def solve():
    def backtrack(row):
        if row == n:
            result.append([list(pos) for pos in positions])
            return
        for col in range(n):
            if (
                col in cols
                or (row + col) in positive_diagonal
                or (row - col) in negative_diagonal
            ):
                continue
            cols.add(col)
            positive_diagonal.add(row + col)
            negative_diagonal.add(row - col)
            positions.append((row, col))
            backtrack(row + 1)
            cols.remove(col)
            positive_diagonal.remove(row + col)
            negative_diagonal.remove(row - col)
            positions.pop()

    cols = set()
    positive_diagonal = set()
    negative_diagonal = set()
    positions = []
    result = []
    backtrack(0)
    return result


def print_solutions(solutions):
    for solution in solutions:
        print(solution)


solutions = solve()
print_solutions(solutions)
