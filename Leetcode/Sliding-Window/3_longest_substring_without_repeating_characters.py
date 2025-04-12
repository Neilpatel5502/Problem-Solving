# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time Complexity: O(n) – each character is visited at most twice
# Space Complexity: O(k) – where k is the size of the character set used (at most O(26) for lowercase letters, O(128/256) for ASCII)

def lengthOfLongestSubstring(s):
    """
    Approach:
        - Use a sliding window with a set to track characters in the current window.
        - Initialize left (L) pointer to start of the window.
        - Move right (R) pointer through the string:
            - If s[R] is already in the window, shrink the window from the left until it's removed.
            - Add s[R] to the set and update the maximum length.
        - The window always contains unique characters.
    """

    window = set()  # Set to store unique characters in the current window
    L = 0           # Left pointer
    output = 0      # Maximum length of substring without duplicates

    for R in range(len(s)):
        while s[R] in window:
            window.remove(s[L])  # Shrink window from the left
            L += 1
        window.add(s[R])  # Add new character to window
        output = max(output, len(window))  # Update max length

    return output


def main():
    # Test - 1
    s1 = "abcabcbb"
    print(f"output-1: {lengthOfLongestSubstring(s1)}")

    # Test - 2
    s2 = "bbbbb"
    print(f"output-2: {lengthOfLongestSubstring(s2)}")

    # Test - 3
    s3 = "pwwkew"
    print(f"output-3: {lengthOfLongestSubstring(s3)}")

if __name__ == "__main__":
    main()
