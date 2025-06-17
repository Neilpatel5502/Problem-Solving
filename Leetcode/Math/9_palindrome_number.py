# Problem: https://leetcode.com/problems/palindrome-number

# Time Complexity: O(log₁₀(x)) – Number of digits in x
# Space Complexity: O(1)

def isPalindrome(x):
    """
    Approach:
        - Negative numbers are not palindromes due to the '-' sign.
        - Reverse the number by extracting its digits and constructing the reversed version.
        - Compare the reversed number with the original.
        - If they are equal, the number is a palindrome.
    """
    if x < 0:
        return False  # Negative numbers cannot be palindromes

    target = x         # Store the original number
    out = 0            # Reversed number

    # Build the reversed number
    while x > 0:
        out = out * 10 + x % 10   # Append last digit
        x = x // 10               # Remove last digit

    # Compare reversed number with original
    return out == target


def main():
    # Test - 1
    x1 = 121
    print(f"output-1: {isPalindrome(x1)}")

    # Test - 2
    x2 = -121
    print(f"output-2: {isPalindrome(x2)}")

    # Test - 3
    x3 = 10
    print(f"output-3: {isPalindrome(x3)}")

if __name__ == "__main__":
    main()
