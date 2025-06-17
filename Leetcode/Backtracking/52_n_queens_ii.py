# Problem: https://leetcode.com/problems/n-queens-ii

# Time Complexity: O(n!)                 # Each row has at most n options, reduced by constraints
# Space Complexity: O(n)                 # For column, positive and negative diagonal sets

def totalNQueens(n):
    """
    Approach:
        - Use backtracking to place queens row by row.
        - At each step, keep track of:
            * Columns with a queen (col set)
            * Positive diagonals (r + c) with a queen (pos_diag set)
            * Negative diagonals (r - c) with a queen (neg_diag set)
        - If a safe position is found, place the queen and recurse to the next row.
        - On reaching row n, increment the solution count.
        - Backtrack by removing the placed queen and trying the next column.
    """
    out = 0
    col = set()         # Tracks columns with queens
    pos_diag = set()    # Tracks positive diagonals (r + c)
    neg_diag = set()    # Tracks negative diagonals (r - c)

    def backtrack(r):
        nonlocal out

        # Base case: all queens are placed successfully
        if r == n:
            out += 1
            return

        for c in range(n):
            # Skip if column or diagonals are under attack
            if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            # Place queen at (r, c)
            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)

            backtrack(r + 1)  # Move to next row

            # Backtrack: remove queen from (r, c)
            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)

    backtrack(0)  # Start placing queens from the first row
    return out


def main():
    # Test - 1
    n1 = 4
    print(f"output-1: {totalNQueens(n1)}")

    # Test - 2
    n2 = 1
    print(f"output-2: {totalNQueens(n2)}")

if __name__ == "__main__":
    main()
