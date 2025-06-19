# Problem: https://leetcode.com/problems/triangle

# Time Complexity: O(n^2)       # Each node in the triangle is visited once
# Space Complexity: O(n^2)      # Memoization table stores results for each (r, c)
def minimumTotal_top_down(triangle):
    """
    Approach:
        - Use DFS with memoization to avoid recomputation.
        - At each position (r, c), choose the minimum of the two possible downward paths:
          (r+1, c) and (r+1, c+1).
        - Recursively compute the minimal path sum from top to bottom.
        - Use a memoization dictionary to store intermediate results and improve efficiency.
    """

    memo = {}  # Dictionary to store computed results for each (row, col)

    def dfs(r, c):
        # Base case: if we're past the last row, return 0 (no cost)
        if r == len(triangle):
            return 0

        # If already computed, return the stored result
        if (r, c) in memo:
            return memo[(r, c)]

        # Recursive step: value at (r, c) + min of two paths going down
        out = triangle[r][c] + min(dfs(r + 1, c), dfs(r + 1, c + 1))
        memo[(r, c)] = out  # Memoize the result

        return memo[(r, c)]

    return dfs(0, 0)



# Time Complexity: O(n^2)       # We fill a DP table of size n^2
# Space Complexity: O(n^2)      # 2D DP array of size m x n
def minimumTotal_bottom_up(triangle):
    """
    Approach:
        - Use bottom-up dynamic programming to compute the minimum path sum.
        - Start from the bottom row of the triangle, initialize it into a DP table.
        - Move upward row by row, updating each cell with the minimum path sum
          achievable from the two adjacent cells in the row below.
        - The top cell will contain the minimum path sum from top to bottom.
    """

    m = len(triangle)                # Number of rows
    n = len(triangle[-1])           # Length of the last row (widest)
    dp = [[0] * n for _ in range(m)]  # DP table with dimensions m x n

    # Initialize the last row of DP table with triangle values
    for i in range(n):
        dp[m - 1][i] = triangle[m - 1][i]

    # Fill DP table from bottom to top
    for i in range(m - 2, -1, -1):
        for j in range(i + 1):  # Only valid indices in current row
            dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])

    return dp[0][0]



def main():
    # Test - 1
    triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(f"Top-Down output-1: {minimumTotal_top_down(triangle1)}")
    print(f"Bottom-Up output-1: {minimumTotal_bottom_up(triangle1)}\n")

    # Test - 2
    triangle2 = [[-10]]
    print(f"Top-Down output-2: {minimumTotal_top_down(triangle2)}")
    print(f"Bottom-Up output-2: {minimumTotal_bottom_up(triangle2)}")

if __name__ == "__main__":
    main()
