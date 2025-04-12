# Problem: https://leetcode.com/problems/permutation-in-string/
# Time Complexity: O(n) – where n is the length of s2
# Space Complexity: O(1) – fixed alphabet size (26 letters)

def checkInclusion(s1, s2):
    """
    Approach:
        - Use sliding window of size len(s1) over s2.
        - Create frequency maps (dictionaries) for s1 and the current window in s2.
        - Slide the window one character at a time:
            - Add the right character.
            - Remove the left character.
        - Compare the two maps at each step. If equal, return True.
    """

    if len(s1) > len(s2):
        return False

    s1_map, s2_map = {}, {}

    # Initialize frequency maps for s1 and the first window in s2
    for i in range(len(s1)):
        s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
        s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1

    left = 0
    for right in range(len(s1), len(s2)):
        if s1_map == s2_map:
            return True

        # Add new character to window
        s2_map[s2[right]] = s2_map.get(s2[right], 0) + 1

        # Remove leftmost character from window
        s2_map[s2[left]] -= 1
        if s2_map[s2[left]] == 0:
            del s2_map[s2[left]]
        left += 1

    return s1_map == s2_map  # Check last window


def main():
    # Test - 1
    s1 = "ab"
    s2 = "eidbaooo"
    print(f"output-1: {checkInclusion(s1, s2)}")

    # Test - 2
    s1 = "ab"
    s2 = "eidboaoo"
    print(f"output-2: {checkInclusion(s1, s2)}")

if __name__ == "__main__":
    main()
