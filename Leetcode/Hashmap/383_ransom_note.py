# Problem: https://leetcode.com/problems/ransom-note

# Time Complexity: O(m + n), where m = len(magazine), n = len(ransomNote)
# Space Complexity: O(1), since character set is limited to lowercase letters

from collections import defaultdict

def canConstruct(ransomNote, magazine):
    """
    Approach:
        - Count the frequency of each character in the magazine using a dictionary.
        - Traverse the ransomNote and check if each character is available in the magazine.
        - Decrease the count for each used character.
        - If any character is unavailable or exhausted, return False.
        - Otherwise, return True after successful verification.
    """
    counter = defaultdict(int)

    # Count characters in magazine
    for ch in magazine:
        counter[ch] += 1

    # Check if ransomNote can be formed
    for ch in ransomNote:
        if ch not in counter:
            return False
        counter[ch] -= 1
        if counter[ch] < 0:
            return False

    return True

def main():
    # Test - 1
    ransomNote1 = "a"
    magazine1 = "b"
    print(f"output-1: {canConstruct(ransomNote1, magazine1)}")

    # Test - 2
    ransomNote2 = "aa"
    magazine2 = "ab"
    print(f"output-2: {canConstruct(ransomNote2, magazine2)}")

    # Test - 3
    ransomNote3 = "aa"
    magazine3 = "aab"
    print(f"output-3: {canConstruct(ransomNote3, magazine3)}")

if __name__ == "__main__":
    main()
