# Problem: https://leetcode.com/problems/valid-anagram

# Time Complexity: O(n) - where n is the length of the strings
# Space Complexity: O(1) - constant space since the hash maps store at most 26 lowercase letters

def isAnagram(s, t):
    """
    Approach:
        - If the lengths of the two strings are not equal, they cannot be anagrams.
        - Use two hash maps to count the frequency of each character in both strings.
        - Iterate over each character of the strings, update their respective frequency maps.
        - If both frequency maps are equal at the end, the strings are anagrams.
    """

    # Early return if lengths are not equal
    if len(s) != len(t):
        return False

    tempS, tempT = {}, {}  # Dictionaries to store character frequencies

    # Populate frequency maps
    for i in range(len(s)):
        tempS[s[i]] = 1 + tempS.get(s[i], 0)
        tempT[t[i]] = 1 + tempT.get(t[i], 0)

    # Check if both dictionaries are equal
    return tempS == tempT


def main():
    # Test - 1
    s1 = "anagram"
    t1 = "nagaram"
    print(f"output-1: {isAnagram(s1, t1)}")

    # Test - 2
    s2 = "rat"
    t2 = "car"
    print(f"output-2: {isAnagram(s2, t2)}")

if __name__ == "__main__":
    main()
