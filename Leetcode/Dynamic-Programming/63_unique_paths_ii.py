# Problem: https://leetcode.com/problems/unique-paths-ii

from functools import lru_cache

# Time Complexity: O(m * n)         # Each cell is visited once and stored in cache
# Space Complexity: O(m * n)        # For recursion stack and memoization
def uniquePathsWithObstacles_top_down(obstacleGrid):
    """
    Approach:
        - Use DFS with memoization to explore all valid paths from top-left to bottom-right.
        - Base case: If the current cell is out of bounds or an obstacle, return 0.
        - If we reach the bottom-right cell and it's not an obstacle, return 1.
        - Recursively sum the paths from the cell to the right and the cell below.
        - Cache results to avoid redundant computation.
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    @lru_cache
    def dfs(i, j):
        # If out of bounds or on an obstacle, no path
        if i >= m or j >= n or obstacleGrid[i][j] == 1:
            return 0

        # If destination is reached and not an obstacle
        if i == m - 1 and j == n - 1:
            return 1

        # Sum of paths from right and down cells
        return dfs(i + 1, j) + dfs(i, j + 1)

    # If destination is an obstacle, no path exists
    return 0 if obstacleGrid[m - 1][n - 1] == 1 else dfs(0, 0)



# Time Complexity: O(m * n)       # Each cell in the grid is visited once
# Space Complexity: O(m * n)      # 2D DP table of size m x n is used
def uniquePathsWithObstacles_bottom_up(obstacleGrid):
    """
    Approach:
        - Use bottom-up dynamic programming starting from the bottom-right corner.
        - Initialize a 2D DP table with zeros.
        - If the destination cell is an obstacle, return 0 immediately.
        - Set dp[m-1][n-1] = 1 as the base case (destination is reachable).
        - Fill the last column and last row while checking for obstacles.
        - For the rest of the grid, if the cell is not an obstacle,
          calculate the number of ways by summing paths from the cell below and to the right.
        - The result will be in dp[0][0], representing paths from the start.
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    # If destination is an obstacle, no path exists
    if obstacleGrid[m - 1][n - 1] == 1:
        return 0

    dp[m - 1][n - 1] = 1  # Base case

    # Fill the last column
    for i in range(m - 2, -1, -1):
        if obstacleGrid[i][n - 1] == 0:
            dp[i][n - 1] = dp[i + 1][n - 1]

    # Fill the last row
    for j in range(n - 2, -1, -1):
        if obstacleGrid[m - 1][j] == 0:
            dp[m - 1][j] = dp[m - 1][j + 1]

    # Fill the rest of the grid
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

    return dp[0][0]


def main():
    # Test - 1
    grid1 = [[0,0,0],[0,1,0],[0,0,0]]
    print(f"Top-Down output-1: {uniquePathsWithObstacles_top_down(grid1)}")
    print(f"Bottom-Up output-1: {uniquePathsWithObstacles_bottom_up(grid1)}\n")

    # Test - 2
    grid2 = [[0,1],[0,0]]
    print(f"Top-Down output-2: {uniquePathsWithObstacles_top_down(grid2)}")
    print(f"Bottom-Up output-2: {uniquePathsWithObstacles_bottom_up(grid2)}")

if __name__ == "__main__":
    main()
