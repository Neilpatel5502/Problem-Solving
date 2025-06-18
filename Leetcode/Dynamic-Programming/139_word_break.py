# Problem: https://leetcode.com/problems/word-break

from functools import lru_cache

# Time Complexity: O(n * m)     # n = len(s), m = average word length in wordDict (due to slicing and comparisons)
# Space Complexity: O(n)        # Recursion depth and memoization cache
def wordBreak_top_down(s, wordDict):
    """
    Approach:
        - Use top-down dynamic programming (DFS + memoization)
          to check if the string can be broken into valid words from the dictionary.
        - At each index i, try every word in the dictionary.
        - If the substring starting at i matches a word, recursively check from the end of that word.
        - If we reach the end of the string (i == len(s)), return True.
        - Memoize results for each index to avoid recomputation.
    """
    @lru_cache
    def dfs(i):
        # If we reach the end, the string can be segmented
        if i == len(s):
            return True

        # Try each word in the dictionary
        for w in wordDict:
            # Check if the substring matches the word and is within bounds
            if (i + len(w) <= len(s) and s[i: i + len(w)] == w):
                if dfs(i + len(w)):  # Recursive call from the next position
                    return True

        return False

    return dfs(0)



# Time Complexity: O(n * m)     # n = len(s), m = number of words in wordDict (each word check takes up to O(k))
# Space Complexity: O(n)        # DP array of size n + 1
def wordBreak_bottom_up(s, wordDict):
    """
    Approach:
        - Use bottom-up dynamic programming to determine if `s` can be segmented into words from `wordDict`.
        - dp[i] represents whether the substring s[i:] can be broken into valid words.
        - Start from the end of the string and move backward.
        - For each position, check if any word in wordDict matches the substring starting at i.
            - If yes and dp[i + len(word)] is True, then set dp[i] = True.
        - Finally, return dp[0], which tells whether the full string can be segmented.
    """
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True  # Base case: empty string can always be segmented

    # Fill dp from end to start
    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            # Check if word matches substring starting at i
            if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                dp[i] = dp[i + len(w)]  # Can we segment the rest?
            if dp[i]:  # Early break if already True
                break

    return dp[0]



def main():
    # Test 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]

    print(f"Top-Down output-1: {wordBreak_top_down(s1, wordDict1)}")
    print(f"Bottom-Up output-1: {wordBreak_bottom_up(s1, wordDict1)}\n")

    # Test 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    print(f"Top-Down output-2: {wordBreak_top_down(s2, wordDict2)}")
    print(f"Bottom-Up output-2: {wordBreak_bottom_up(s2, wordDict2)}\n")

    # Test 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print(f"Top-Down output-3: {wordBreak_top_down(s3, wordDict3)}")
    print(f"Bottom-Up output-3: {wordBreak_bottom_up(s3, wordDict3)}")

if __name__ == "__main__":
    main()
