# Problem: https://leetcode.com/problems/length-of-last-word

# Time Complexity: O(n)
# Space Complexity: O(1)

def lengthOfLastWord(s):
    """
    Approach:
        - First, remove any trailing spaces using `rstrip()`.
        - Then iterate through the string to find the index of the last space character.
        - The length of the last word is then `len(s) - last_i - 1` (i.e., characters after the last space).
        - If there are no spaces (i.e., a single word), return the full length of the string.
    """
    s = s.rstrip()       # Remove trailing spaces
    last_i = -1          # Track index of last seen space

    # Iterate through the string to find the last space
    for i in range(len(s)):
        if s[i] == " ":
            last_i = i

    # Length of last word = total length - position of last space - 1
    return len(s) - last_i - 1 if last_i >= 0 else len(s)

def main():
    # Test - 1
    s1 = "Hello World"
    print(f"output-1: {lengthOfLastWord(s1)}")

    # Test - 2
    s2 = "   fly me   to   the moon  "
    print(f"output-2: {lengthOfLastWord(s2)}")

    # Test - 3
    s3 = "luffy is still joyboy"
    print(f"output-3: {lengthOfLastWord(s3)}")

if __name__ == "__main__":
    main()
