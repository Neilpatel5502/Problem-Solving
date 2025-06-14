# Problem: https://leetcode.com/problems/is-subsequence

# Time Complexity: O(n), where n = len(t)
# Space Complexity: O(1)

def isSubsequence(s, t):
    """
    Approach:
        - Use two pointers to traverse both strings.
        - Pointer `i` tracks the position in string `s`, and `j` tracks in `t`.
        - When characters match (`s[i] == t[j]`), move `i` forward.
        - Always move `j` forward.
        - If `i` reaches the end of `s`, it means all characters of `s` were found in order in `t`.
    """
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)

def main():
    # Test - 1
    s1 = "abc"
    t1 = "ahbgdc"
    print(f"output-1: {isSubsequence(s1, t1)}")

    # Test - 2
    s2 = "axc"
    t2 = "ahbgdc"
    print(f"output-2: {isSubsequence(s2, t2)}")

if __name__ == "__main__":
    main()
