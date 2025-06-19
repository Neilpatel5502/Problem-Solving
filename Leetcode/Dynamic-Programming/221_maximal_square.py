# Problem: https://leetcode.com/problems/maximal-square

from functools import lru_cache

# Time Complexity: O(m * n)        where m is number of rows and n is number of columns
# Space Complexity: O(m * n)       due to memoization (cache)
def maximalSquare_top_down(matrix):
    """
    Approach:
        - Use DFS with memoization to compute the size of the largest square
          with all '1's starting at each cell.
        - For each cell (r, c), compute the minimum of:
            * dfs(r + 1, c)      → square size going down
            * dfs(r, c + 1)      → square size going right
            * dfs(r + 1, c + 1)  → square size going diagonally
          If current cell is '1', return 1 + min(all three above), else return 0.
        - Keep track of the maximum square size found during the traversal.
    """
    m, n = len(matrix), len(matrix[0])  # Dimensions of the matrix

    @lru_cache
    def dfs(r, c):
        # If out of bounds, return 0
        if r >= m or c >= n:
            return 0

        out = 0

        # Recursive DFS calls for bottom, right, and bottom-right neighbors
        down = dfs(r + 1, c)
        right = dfs(r, c + 1)
        diag = dfs(r + 1, c + 1)

        # If current cell is '1', compute square size
        if matrix[r][c] == "1":
            out = 1 + min(down, right, diag)

        return out

    out = 0  # Track the largest square size
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == "1":
                out = max(out, dfs(r, c))

    return out * out  # Return area of largest square


# Time Complexity: O(m * n)        where m is number of rows and n is number of columns
# Space Complexity: O(m * n)       for the dp table
def maximalSquare_bottom_up(matrix):
    """
    Approach:
        - Use bottom-up dynamic programming to find the largest square of 1's.
        - Create a (m+1) x (n+1) DP table initialized to 0.
        - Iterate from bottom-right to top-left of the input matrix.
        - For each cell (r, c), if matrix[r][c] == "1":
            * dp[r][c] = 1 + min(dp[r+1][c], dp[r][c+1], dp[r+1][c+1])
            * This ensures the square is extended only if all 3 neighbors can also form a square.
        - Track the maximum square side during traversal.
        - Return the area by squaring the maximum side.
    """
    m, n = len(matrix), len(matrix[0])

    # Initialize DP table with an extra row and column to handle borders easily
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    out = 0  # To track the largest square side length

    # Fill the dp table from bottom-right to top-left
    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            if matrix[r][c] == "1":
                # Update dp[r][c] using min of right, down, and diagonal neighbors
                dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
                # Update maximum square side found so far
                out = max(out, dp[r][c])

    # Return area of the largest square
    return out * out


def main():
    # Test - 1
    matrix1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(f"Top-Down output-1: {maximalSquare_top_down(matrix1)}")
    print(f"Bottom-Up output-1: {maximalSquare_bottom_up(matrix1)}\n")

    # Test - 2
    matrix2 = [["0","1"],["1","0"]]
    print(f"Top-Down output-2: {maximalSquare_top_down(matrix2)}")
    print(f"Bottom-Up output-2: {maximalSquare_bottom_up(matrix2)}\n")

    # Test - 3
    matrix3 = [["0"]]
    print(f"Top-Down output-3: {maximalSquare_top_down(matrix3)}")
    print(f"Bottom-Up output-3: {maximalSquare_bottom_up(matrix3)}")

if __name__ == "__main__":
    main()
