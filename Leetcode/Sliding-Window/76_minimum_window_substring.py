# Problem: https://leetcode.com/problems/minimum-window-substring

# Time Complexity: O(m + n) – m = len(s), n = len(t)
# Space Complexity: O(n) – for storing character counts of `t` and the current window

def minWindow(s, t):
    """
    Approach:
        - Use a sliding window to expand and contract the window.
        - Maintain two hash maps:
            1. `countT`: frequency of characters in `t`.
            2. `window`: frequency of characters in current window in `s`.
        - Expand the right pointer until all required characters are in the window.
        - Then contract from the left while still maintaining all required characters.
        - Track the smallest valid window seen.
    """

    if t == "":
        return ""

    countT, window = {}, {}

    for char in t:
        countT[char] = countT.get(char, 0) + 1

    have, need = 0, len(countT)
    out, outLen = [-1, -1], float("inf")
    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in countT and window[char] == countT[char]:
            have += 1

        while have == need:
            # Update output if this window is smaller
            if (right - left + 1) < outLen:
                out = [left, right]
                outLen = (right - left + 1)

            # Try to contract window from the left
            window[s[left]] -= 1
            if s[left] in countT and window[s[left]] < countT[s[left]]:
                have -= 1
            left += 1

    l, r = out
    return s[l:r+1] if outLen != float("inf") else ""


def main():
    # Test - 1
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    print(f"output-1: {minWindow(s1, t1)}")

    # Test - 2
    s2 = "a"
    t2 = "a"
    print(f"output-2: {minWindow(s2, t2)}")

    # Test - 3
    s3 = "a"
    t3 = "aa"
    print(f"output-3: {minWindow(s3, t3)}")

if __name__ == "__main__":
    main()
