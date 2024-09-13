import collections
from math import sqrt
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    size = len(board)
    small_size = sqrt(size)
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    sub_boards = collections.defaultdict(set)

    for i in range(size):
        for j in range(size):
            value = board[i][j]
            if value == ".":
                continue

            a1 = rows[i]
            a2 = cols[j]
            a3 = sub_boards[(i // small_size, j // small_size)]

            if (
                value in rows[i]
                or value in cols[j]
                or value in sub_boards[(i // small_size, j // small_size)]
            ):
                return False

            rows[i].add(value)
            cols[j].add(value)
            sub_boards[(i // small_size, j // small_size)].add(value)

    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

valid = isValidSudoku(board)

print(valid)
