# Problem: https://leetcode.com/problems/longest-repeating-character-replacement/
# Time Complexity: O(n) – single pass through the string
# Space Complexity: O(1) – only 26 uppercase letters stored in the frequency dictionary

def characterReplacement(s, k):
    """
    Approach:
        - Use a sliding window to maintain a valid substring.
        - For each window, track the frequency of characters using a hashmap.
        - The main idea is:
            If (window length - count of most frequent char) <= k:
                It's valid — we can change other chars to match the most frequent one.
            Else:
                Shrink the window from the left.
        - Keep updating the maximum valid window size.
    """

    window_freq = {}
    L = 0
    output = 0
    max_count = 0  # Tracks the count of the most frequent character in the window

    for R in range(len(s)):
        window_freq[s[R]] = 1 + window_freq.get(s[R], 0)
        max_count = max(max_count, window_freq[s[R]])

        # If we need to replace more than k chars, shrink the window
        if (R - L + 1) - max_count > k:
            window_freq[s[L]] -= 1
            L += 1

        output = max(output, R - L + 1)

    return output


def main():
    # Test - 1
    s1 = "ABAB"
    k1 = 2
    print(f"output-1: {characterReplacement(s1, k1)}")

    # Test - 2
    s2 = "AABABBA"
    k2 = 1
    print(f"output-2: {characterReplacement(s2, k2)}")

if __name__ == "__main__":
    main()
