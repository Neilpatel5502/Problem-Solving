# Problem: https://leetcode.com/problems/roman-to-integer

# Time Complexity: O(n)
# Space Complexity: O(1)

def romanToInt(s):
    """
    Approach:
        - Use a dictionary to map Roman numerals to their integer values.
        - Traverse the string from left to right.
        - If the current character is less than the next one (e.g., I before V), subtract it from the total.
        - Otherwise, add it to the total.
        - Finally, add the value of the last character (always added).
    """
    rti_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0

    # Traverse the string up to the second last character
    for i in range(len(s) - 1):
        if rti_dict[s[i]] < rti_dict[s[i + 1]]:
            ans -= rti_dict[s[i]]  # Subtractive notation case
        else:
            ans += rti_dict[s[i]]  # Normal addition

    # Always add the last character's value
    return ans + rti_dict[s[-1]]

def main():
    # Test - 1
    s1 = "III"
    print(f"output-1: {romanToInt(s1)}")

    # Test - 2
    s2 = "LVIII"
    print(f"output-2: {romanToInt(s2)}")

    # Test - 3
    s3 = "MCMXCIV"
    print(f"output-3: {romanToInt(s3)}")

if __name__ == "__main__":
    main()
