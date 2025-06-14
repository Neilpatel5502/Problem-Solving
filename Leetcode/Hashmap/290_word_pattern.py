# Problem: https://leetcode.com/problems/word-pattern

# Time Complexity: O(n), where n = number of words in s
# Space Complexity: O(n), for storing mappings and visited words

def wordPattern(pattern, s):
    """
    Approach:
        - Split the string `s` into words.
        - Use a dictionary `temp` to map pattern characters to words.
        - Use a set `visited` to ensure no two pattern characters map to the same word.
        - Check the mapping consistency while traversing the pattern and word list.
    """
    temp = {}         # Map from pattern character to word
    visited = set()   # Set to track already mapped words

    s_list = s.split(" ")

    # If pattern and word list lengths differ, return False
    if len(pattern) != len(s_list):
        return False

    # Iterate through each character and word in parallel
    for ch, w in zip(pattern, s_list):
        if ch not in temp:
            # If the word is already assigned to another character, return False
            if w in visited:
                return False

            # Map the pattern character to the word
            temp[ch] = w
            visited.add(w)  # Mark the word as used
        else:
            # If the current word doesn't match the previously mapped word, return False
            if w != temp[ch]:
                return False

    return True  # All pattern characters matched correctly to words

def main():
    # Test - 1
    pattern1 = "abba"
    s1 = "dog cat cat dog"
    print(f"output-1: {wordPattern(pattern1, s1)}")

    # Test - 2
    pattern2 = "abba"
    s2 = "dog cat cat fish"
    print(f"output-2: {wordPattern(pattern2, s2)}")

    # Test - 3
    pattern3 = "aaaa"
    s3 = "dog cat cat dog"
    print(f"output-3: {wordPattern(pattern3, s3)}")

if __name__ == "__main__":
    main()
