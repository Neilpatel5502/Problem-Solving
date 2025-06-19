# Problem: https://leetcode.com/problems/minimum-path-sum

from functools import lru_cache

# Time Complexity: O(m * n)        (Each cell is visited once and memoized)
# Space Complexity: O(m * n)       (Recursion stack and memoization cache)
def minPathSum_top_down(grid):
    """
    Approach:
        - Use DFS with memoization (Top-Down DP).
        - Starting from the top-left corner, recursively calculate the minimum path sum
          to the bottom-right by moving only right or down.
        - Cache the results for each cell to avoid redundant calculations.
    """
    m = len(grid)
    n = len(grid[0])

    @lru_cache
    def dfs(i, j):
        # Base case: reached bottom-right corner
        if i == m - 1 and j == n - 1:
            return grid[i][j]

        # Return inf if out of bounds
        if i >= m or j >= n:
            return float('inf')

        # Compute min path sum by going right and down
        out = grid[i][j] + min(dfs(i, j + 1), dfs(i + 1, j))

        return out

    return dfs(0, 0)


# Time Complexity: O(m * n)        (Each cell is visited once)
# Space Complexity: O(m * n)       (DP table of size m x n)
def minPathSum_bottom_up(grid):
    """
    Approach:
        - Use Bottom-Up Dynamic Programming.
        - Start from the bottom-right cell and move backwards to fill the minimum path sums
          for each cell based on the right and bottom neighbors.
        - dp[i][j] will store the minimum sum to reach the bottom-right from cell (i, j).
        - Final answer is stored in dp[0][0] (top-left corner).
    """
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Base case: bottom-right cell is the destination
    dp[m - 1][n - 1] = grid[m - 1][n - 1]

    # Fill the last row (can only move right)
    for j in range(n - 2, -1, -1):
        dp[m - 1][j] = grid[m - 1][j] + dp[m - 1][j + 1]

    # Fill the last column (can only move down)
    for i in range(m - 2, -1, -1):
        dp[i][n - 1] = grid[i][n - 1] + dp[i + 1][n - 1]

    # Fill the rest of the table
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]


def main():
    # Test - 1
    grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(f"Top-Down output-1: {minPathSum_top_down(grid1)}")
    print(f"Bottom-Up output-1: {minPathSum_bottom_up(grid1)}\n")

    # Test - 2
    grid2 = [[1, 2, 3], [4, 5, 6]]
    print(f"Top-Down output-2: {minPathSum_top_down(grid2)}")
    print(f"Bottom-Up output-2: {minPathSum_bottom_up(grid2)}")

if __name__ == "__main__":
    main()
