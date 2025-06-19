# Problem: https://leetcode.com/problems/valid-sudoku

# Time Complexity: O(1) — always processes a 9x9 board (constant size)
# Space Complexity: O(1) — at most stores 81 values across rows, columns, and boxes

from collections import defaultdict

def isValidSudoku(board):
    """
    Approach:
        - Use three hash sets to track:
            - Digits seen in each row
            - Digits seen in each column
            - Digits seen in each 3x3 sub-box (indexed by (i//3, j//3))
        - For every cell:
            - Skip if the cell is '.'
            - Check if the digit already exists in the corresponding row, column, or box
            - If so, return False (violation of Sudoku rule)
            - Otherwise, add the digit to respective sets
        - If no violations are found, return True
    """

    n, m = len(board), len(board[0])
    rows = defaultdict(set)   # digits seen in each row
    cols = defaultdict(set)   # digits seen in each column
    boxes = defaultdict(set)  # digits seen in each 3x3 sub-box

    for i in range(n):
        for j in range(m):
            if board[i][j] == ".":
                continue

            val = board[i][j]

            # If digit already seen in row, column, or box => invalid
            if (
                val in rows[i] or
                val in cols[j] or
                val in boxes[(i // 3, j // 3)]
            ):
                return False

            # Mark digit as seen
            rows[i].add(val)
            cols[j].add(val)
            boxes[(i // 3, j // 3)].add(val)

    return True


def main():
    # Test - 1
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(f"output-1: {isValidSudoku(board1)}")

    # Test - 2
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(f"output-2: {isValidSudoku(board2)}")

if __name__ == "__main__":
    main()
