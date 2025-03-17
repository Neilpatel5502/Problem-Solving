# Problem Link: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii

# Time Complexity: O(n)     n is the length of the word
# Space Complexity: O(1)    we are using limited values for lists and counter

from collections import Counter

def countOfSubstrings(word, k):
    """
    Approach:
        - We need to count the number of substrings that contain all vowels ('a', 'e', 'i', 'o', 'u') at least once and exactly `k` consonants.
        - We use the sliding window technique with two pointers (`left` and `right`) to explore all possible substrings.
        - Maintain a counter for vowels and consonants and track the positions of the vowels and consonants to efficiently compute valid substrings.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']

    n = len(word)
    left = 0
    counter = Counter() # Counter for vowels

    c = 0               # Count of consonants in the current window
    v = 0               # Count of different vowels in the current window
    last_vowels = {}    # Dictionary to store the last index of each vowel encountered
    c_prefix = []       # List to store the positions of consonants in the current window

    out = 0

    for right in range(n):
        # Add right pointer chars to counters and tracking maps
        ch_right = word[right]

        if ch_right in vowels:
            if counter[ch_right] == 0:
                v += 1

            counter[ch_right] += 1          # Increment the count of the vowel in the window
            last_vowels[ch_right] = right   # Update the last index of this vowel
        else:
            c += 1
            c_prefix.append(right)          # Track the position of consonants

        # Shrink the window from the left if the number of consonants exceeds k
        while c > k:
            ch_left = word[left]

            if ch_left in vowels:
                counter[ch_left] -= 1
                if counter[ch_left] == 0:   # If this vowel is no longer in the window, decrement the vowel count
                    v -= 1
            else:
                c -= 1

            left += 1

        # Now, check if we have exactly 5 distinct vowels and k consonants in the window
        if v == 5 and c == k:
            v_i = min(last_vowels.values())         # lowest critical vowel
            c_i = c_prefix[-k] if k!= 0 else right  # lowest critical consonants
            out += min(c_i, v_i) - left + 1         # calculate the amount of substrings that can be created without deleteing the lowest critical character

    return out


def main():
    # Test - 1
    word1 = "aeioqq"
    k1 = 1
    print(f"output-1: {countOfSubstrings(word1, k1)}")

    # Test - 2
    word2 = "aeiou"
    k2 = 0
    print(f"output-2: {countOfSubstrings(word2, k2)}")

    # Test - 3
    word3 = "ieaouqqieaouqq"
    k3 = 1
    print(f"output-2: {countOfSubstrings(word3, k3)}")

if __name__ == "__main__":
    main()
