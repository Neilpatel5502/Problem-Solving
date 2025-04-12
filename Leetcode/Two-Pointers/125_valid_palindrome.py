# Problem: https://leetcode.com/problems/valid-palindrome/
# Time Complexity: O(n) – where n is the length of the string
# Space Complexity: O(n) – due to the filtered and lowercased string

def isPalindrome(s):
    """
    Approach:
        - Filter out all non-alphanumeric characters using `str.isalpha()` and `str.isdigit()`.
        - Convert the remaining characters to lowercase.
        - Use two-pointer technique to check if the cleaned string is a palindrome by comparing characters from both ends.
    """

    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(filter(lambda x: x.isalpha() or x.isdigit(), s)).lower()

    # Initialize two pointers
    L = 0
    R = len(s) - 1

    # Compare characters from both ends moving toward the center
    while L < R:
        if s[L] != s[R]:
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
