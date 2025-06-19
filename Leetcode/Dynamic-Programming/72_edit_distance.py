# Problem: https://leetcode.com/problems/edit-distance

from functools import lru_cache

# Time Complexity: O(m * n)       # m = len(word1), n = len(word2)
# Space Complexity: O(m * n)      # For memoization cache and recursion stack
def minDistance_top_down(word1, word2):
    """
    Approach:
        - Use DFS with memoization to recursively compute the minimum edit distance between word1 and word2.
        - At each step, we try three operations:
            1. Insert a character into word1
            2. Delete a character from word1
            3. Replace a character in word1
        - If characters match, skip without increasing the count.
        - Base cases:
            - If one word is exhausted, return remaining length of the other (only inserts or deletes needed).
    """

    m = len(word1)
    n = len(word2)

    @lru_cache
    def dfs(i, j):
        # If word1 is exhausted, insert remaining characters of word2
        if i == m:
            return n - j

        # If word2 is exhausted, delete remaining characters of word1
        if j == n:
            return m - i

        # If characters match, no operation needed
        if word1[i] == word2[j]:
            return dfs(i + 1, j + 1)

        # Try all three operations and choose the one with minimum cost
        out = min(
            dfs(i + 1, j),     # Delete from word1
            dfs(i, j + 1),     # Insert into word1
            dfs(i + 1, j + 1)  # Replace in word1
        )

        return out + 1

    return dfs(0, 0)


# Time Complexity: O(m * n)       # m = len(word1), n = len(word2)
# Space Complexity: O(m * n)      # 2D DP table of size (m+1) x (n+1)
def minDistance_bottom_up(word1, word2):
    """
    Approach:
        - Use bottom-up dynamic programming to compute the minimum number of operations
          to convert word1 to word2.
        - Define dp[i][j] as the minimum edit distance between word1[i:] and word2[j:].
        - Base Case:
            - If one word is exhausted, remaining operations = length of the other word.
        - If characters match, no operation is needed → take diagonal value dp[i+1][j+1].
        - Else, consider:
            1. Insert → dp[i][j+1]
            2. Delete → dp[i+1][j]
            3. Replace → dp[i+1][j+1]
          and take minimum of those + 1.
    """

    m = len(word1)
    n = len(word2)

    # Initialize dp table with infinity
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

    # Fill base cases when one string is empty
    for i in range(m + 1):
        dp[i][n] = m - i  # Delete remaining characters from word1
    for j in range(n + 1):
        dp[m][j] = n - j  # Insert remaining characters into word1

    # Fill table from bottom-right to top-left
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i + 1][j],     # Delete
                    dp[i][j + 1],     # Insert
                    dp[i + 1][j + 1]  # Replace
                )

    return dp[0][0]



def main():
    # Test - 1
    word1 = "horse"
    word2 = "ros"
    print(f"Top-Down output-1: {minDistance_top_down(word1, word2)}")
    print(f"Bottom-Up output-1: {minDistance_bottom_up(word1, word2)}\n")

    # Test - 2
    word1 = "intention"
    word2 = "execution"
    print(f"Top-Down output-2: {minDistance_top_down(word1, word2)}")
    print(f"Bottom-Up output-2: {minDistance_bottom_up(word1, word2)}")

if __name__ == "__main__":
    main()
