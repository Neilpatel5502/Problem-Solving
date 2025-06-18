# Problem: https://leetcode.com/problems/climbing-stairs

from functools import lru_cache

# Time Complexity: O(n)
# Space Complexity: O(n) due to recursion stack and caching
def climbStairs_top_down(n):
    """
    Approach:
        - Use top-down dynamic programming (DFS + memoization).
        - At each step i, you can either take 1 or 2 steps forward.
        - Use recursion to explore all ways to reach step `n` starting from step `i`.
        - Base Case 1: If i == n, we reached the top => return 1 way.
        - Base Case 2: If i > n, it's an invalid path => return 0 ways.
        - Use cache to store intermediate results to avoid recomputation.
    """

    @lru_cache
    def dfs(i):
        if i == n:
            return 1  # One valid way to reach the top
        if i > n:
            return 0  # Invalid step beyond n

        # Recursive calls for 1-step and 2-step moves
        out = dfs(i + 1) + dfs(i + 2)
        return out

    return dfs(0)


# Time Complexity: O(n)
# Space Complexity: O(n)
def climbStairs_bottom_up(n):
    """
    Approach:
        - Use bottom-up dynamic programming.
        - We initialize dp[n] = 1 because there's 1 way to be at the top (step n).
        - We initialize dp[n+1] = 0 since we can't go beyond the top.
        - We build the solution from the end (step n-1 to 0) going backward.
        - dp[i] = number of ways to reach step n from step i.
        - For each step i, you can go either to i+1 or i+2, hence:
              dp[i] = dp[i+1] + dp[i+2]
        - Final result is dp[0], i.e., number of ways from step 0 to n.
    """
    dp = [0] * (n + 2)  # Extra space for dp[n+1] to avoid index error
    dp[n] = 1           # Base case: 1 way to stand at the top
    dp[n + 1] = 0       # No way to go beyond top

    # Fill dp table from n-1 down to 0
    for i in range(n - 1, -1, -1):
        dp[i] = dp[i + 1] + dp[i + 2]

    return dp[0]


def main():
    # Test - 1
    n1 = 2

    print(f"Top-Down output-1: {climbStairs_top_down(n1)}")
    print(f"Bottom-Up output-1: {climbStairs_bottom_up(n1)}\n")

    # Test - 2
    n2 = 3
    print(f"Top-Down output-2: {climbStairs_top_down(n2)}")
    print(f"Bottom-Up output-2: {climbStairs_bottom_up(n2)}")

if __name__ == "__main__":
    main()
