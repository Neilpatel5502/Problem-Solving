# Problem: https://leetcode.com/problems/plus-one

# Time Complexity: O(n) – where n is the number of digits
# Space Complexity: O(n) – for the reversed digits list

def plusOne(digits):
    """
    Approach:
        - Reverse the input digits to make addition easier (starting from least significant digit).
        - Add 1 to the first digit (which is the least significant after reversing).
        - Propagate the carry if any digit becomes >= 10.
        - If a carry is still left after processing all digits, append 1 at the end.
        - Finally, reverse the list back to restore the original order.
    """
    carry = 0

    # Reverse digits to simulate addition from right to left
    inv_digits = digits[::-1]
    inv_digits[0] += 1  # Add one to the least significant digit

    for i, num in enumerate(inv_digits):
        if num + carry >= 10:
            inv_digits[i] = (num + carry) % 10  # Keep last digit
            carry = 1                           # Carry over to next digit
        elif carry:
            inv_digits[i] += carry              # Add carry if it exists
            carry = 0                           # Reset carry once used

    # If there's still a carry left, add a new digit
    if carry:
        inv_digits.append(1)

    # Reverse again to return result in original order
    return inv_digits[::-1]


def main():
    # Test - 1
    digits1 = [1, 2, 3]
    print(f"output-1: {plusOne(digits1)}")

    # Test - 2
    digits2 = [4, 3, 2, 1]
    print(f"output-2: {plusOne(digits2)}")

    # Test - 3
    digits3 = [9]
    print(f"output-3: {plusOne(digits3)}")

if __name__ == "__main__":
    main()
