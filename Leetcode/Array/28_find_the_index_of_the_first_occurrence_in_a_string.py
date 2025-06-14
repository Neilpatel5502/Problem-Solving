# Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

# Time Complexity: O((h - n + 1) * n), where h = len(haystack), n = len(needle)
# Space Complexity: O(1)

def strStr(haystack, needle):
    """
    Approach:
        - Loop through the haystack string, checking each substring of length equal to the needle.
        - If a substring matches the needle, return the starting index.
        - If no match is found after checking all valid positions, return -1.
        - Edge case: if needle is an empty string, return 0 (as per problem definition).
    """
    h = len(haystack)
    n = len(needle)

    for i in range(h - n + 1):
        if haystack[i:i + n] == needle:
            return i  # Return index where needle is found

    return -1  # Return -1 if needle is not found

def main():
    # Test - 1
    haystack1 = "sadbutsad"
    needle1 = "sad"
    print(f"output-1: {strStr(haystack1, needle1)}")  # Expected: 2

    # Test - 2
    haystack2 = "leetcode"
    needle2 = "leeto"
    print(f"output-2: {strStr(haystack2, needle2)}")  # Expected: -1

if __name__ == "__main__":
    main()
