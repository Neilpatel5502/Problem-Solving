# Problem: https://leetcode.com/problems/valid-palindrome/

# Time Complexity: O(n) – where n is the length of the string
# Space Complexity: O(1)

def isPalindrome(s):
    """
    Approach:
        - Use two pointers (L and R) starting from beginning and end of the string.
        - Skip characters that are not alphanumeric using isalpha() and isdigit().
        - Compare lowercase version of characters at L and R.
        - If any mismatch is found, return False.
        - If the entire string passes the checks, return True.
    """
    L = 0
    R = len(s) - 1

    while L < R:
        # Skip non-alphanumeric characters from the left
        while L < R and not s[L].isalpha() and not s[L].isdigit():
            L += 1

        # Skip non-alphanumeric characters from the right
        while L < R and not s[R].isalpha() and not s[R].isdigit():
            R -= 1

        # Compare characters
        if s[L].lower() != s[R].lower():
            return False

        L += 1
        R -= 1

    return True


def main():
    # Test - 1
    s1 = "A man, a plan, a canal: Panama"
    print(f"output-1: {isPalindrome(s1)}")

    # Test - 2
    s2 = "race a car"
    print(f"output-2: {isPalindrome(s2)}")

    # Test - 3
    s3 = " "
    print(f"output-3: {isPalindrome(s3)}")

if __name__ == "__main__":
    main()
