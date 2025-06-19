# Problem: https://leetcode.com/problems/interleaving-string

from functools import lru_cache

# Time Complexity: O(m * n)       # m = len(s1), n = len(s2), memoization avoids recomputation
# Space Complexity: O(m * n)      # For the recursion stack and cache
def isInterleave_top_down(s1, s2, s3):
    """
    Approach:
        - Use DFS with memoization to check if s3 can be formed by interleaving s1 and s2.
        - At each step, try to match a character from s1 or s2 to the current position in s3.
        - If both match fail, return False.
        - Use caching to avoid recomputing overlapping subproblems.
        - Start recursion from index 0 of both s1 and s2.
    """

    @lru_cache
    def dfs(i, j):
        # If both s1 and s2 are fully used, interleaving is valid
        if i == len(s1) and j == len(s2):
            return True

        # Try to take character from s1 if it matches s3 at position i + j
        if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
            return True

        # Try to take character from s2 if it matches s3 at position i + j
        if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
            return True

        # Neither option matched
        return False

    # If total length doesn't match, early return False
    return dfs(0, 0) if len(s1) + len(s2) == len(s3) else False



# Time Complexity: O(m * n)       # m = len(s1), n = len(s2)
# Space Complexity: O(m * n)      # 2D DP table of size (m+1) x (n+1)
def isInterleave_bottom_up(s1, s2, s3):
    """
    Approach:
        - Use bottom-up dynamic programming to determine if s3 is an interleaving of s1 and s2.
        - Create a DP table where dp[i][j] represents whether s3[i+j:] can be formed by interleaving s1[i:] and s2[j:].
        - Start filling the table from the bottom-right corner (base case) and move towards top-left.
        - For each cell, check if the current character in s1 or s2 matches the corresponding character in s3,
          and if the rest of the string can also be formed accordingly.
    """

    m = len(s1)
    n = len(s2)

    # If lengths don't add up, s3 can't be an interleaving
    if m + n != len(s3):
        return False

    # Initialize a (m+1) x (n+1) DP table with False
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: all strings exhausted
    dp[m][n] = True

    # Fill the table from bottom-right to top-left
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            # If current char of s1 matches and remaining can interleave
            if i < m and s1[i] == s3[i + j] and dp[i + 1][j]:
                dp[i][j] = True

            # If current char of s2 matches and remaining can interleave
            if j < n and s2[j] == s3[i + j] and dp[i][j + 1]:
                dp[i][j] = True

    # Final answer at top-left of DP table
    return dp[0][0]



def main():
    # Test - 1
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(f"Top-Down output-1: {isInterleave_top_down(s1, s2, s3)}")
    print(f"Bottom-Up output-1: {isInterleave_bottom_up(s1, s2, s3)}\n")

    # Test - 2
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(f"Top-Down output-2: {isInterleave_top_down(s1, s2, s3)}")
    print(f"Bottom-Up output-2: {isInterleave_bottom_up(s1, s2, s3)}\n")

    # Test - 3
    s1 = ""
    s2 = ""
    s3 = ""
    print(f"Top-Down output-3: {isInterleave_top_down(s1, s2, s3)}")
    print(f"Bottom-Up output-3: {isInterleave_bottom_up(s1, s2, s3)}")

if __name__ == "__main__":
    main()
