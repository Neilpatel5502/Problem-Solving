# Problem Link: https://leetcode.com/problems/palindrome-partitioning/
# Time Complexity: O(2^n * n)        # 2^n for all partitions, each substring check takes O(n)
# Space Complexity: O(n)             # recursion stack and current partition list

def partition(s):
    """
    Approach:
        - Use backtracking to try all possible partitions starting from index `i`.
        - For each index, try every substring from i to j:
            - If substring s[i:j+1] is a palindrome, include it in the current path.
            - Recurse from j + 1 for the next part.
        - If we reach the end of the string, save a copy of the current partition.

    # Tree structure for s = "aab":

                                  []
                               /     \
                            ["a"]     ["aa"]
                           /             \
                     ["a","a"]         ["aa","b"]
                         |
                    ["a","a","b"]

    Valid outputs: [["a","a","b"], ["aa","b"]]

    """

    out = []       # Final list of all palindrome partitions
    subset = []    # Current list of palindromic substrings

    def backtrack(i):
        # Base case: reached end of string
        if i >= len(s):
            out.append(subset.copy())
            return

        # Explore every substring starting from index i
        for j in range(i, len(s)):
            temp = s[i:j+1]
            # Check if the current substring is a palindrome
            if temp == temp[::-1]:
                # Include the palindromic substring
                subset.append(temp)
                # Recurse from the next index
                backtrack(j + 1)
                # Backtrack
                subset.pop()

    # Start from index 0
    backtrack(0)

    return out

def main():
    # Test - 1
    s1 = "aab"
    print(f"output-1: {partition(s1)}")

    # Test - 2
    s2 = "a"
    print(f"output-2: {partition(s2)}")

    # Test - 3
    s3 = "abba"
    print(f"output-3: {partition(s3)}")

if __name__ == "__main__":
    main()
