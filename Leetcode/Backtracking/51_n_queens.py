# Problem Link: https://leetcode.com/problems/n-queens/
# Time Complexity: O(n!)           # Trying all valid queen placements
# Space Complexity: O(n^2)         # For storing board configurations

def solveNQueens(n):
    """
    Approach:
        - Use backtracking to place queens row by row.
        - For each row, try placing a queen in a valid column.
        - Use three sets to track restricted positions:
            - col: columns under attack
            - pos_diag: positive diagonals (r + c)
            - neg_diag: negative diagonals (r - c)
        - If all n rows are filled, convert board to list of strings and add to output.
        - Backtrack by removing the queen and clearing the attack paths.
    """

    col = set()             # Columns where queens are placed
    pos_diag = set()        # r + c diagonal
    neg_diag = set()        # r - c diagonal

    out = []                # Final list of valid board configurations
    board = [["."] * n for _ in range(n)]  # Initialize empty board

    def backtrack(r):
        # If all rows are processed, save board
        if r == n:
            copy = ["".join(row) for row in board]
            out.append(copy)
            return

        for c in range(n):
            # Skip if current column or diagonals are under attack
            if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            # Place queen at (r, c)
            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"

            # Recurse for next row
            backtrack(r + 1)

            # Backtrack: remove queen and reset attacks
            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."

    # Start from first row
    backtrack(0)

    return out

def main():
    # Test - 1
    n1 = 4
    print(f"output-1: {solveNQueens(n1)}")

    # Test - 2
    n2 = 1
    print(f"output-2: {solveNQueens(n2)}")

if __name__ == "__main__":
    main()
