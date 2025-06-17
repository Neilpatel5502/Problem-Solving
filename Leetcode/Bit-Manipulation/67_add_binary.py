# Problem: https://leetcode.com/problems/add-binary

# Time Complexity: O(max(n, m))        # n = len(a), m = len(b)
# Space Complexity: O(max(n, m))       # Output string size

def addBinary(a, b):
    """
    Approach:
        - Use two pointers starting from the end of both strings.
        - Iterate through both strings and simulate binary addition:
            0 + 0 = 0
            1 + 0 or 0 + 1 = 1
            1 + 1 = 0 with carry 1
            1 + 1 + carry = 1 with carry 1 (and so on)
        - This can be achieved with total_sum % 2 and carry = total_sum // 2
        - Keep appending the binary result to the output string.
        - Reverse the result at the end since we built it backwards.
    """
    carry = 0
    out = ""  # Result string

    i, j = len(a) - 1, len(b) - 1  # Start from the last digit of both strings

    while i >= 0 or j >= 0 or carry == 1:
        if i >= 0:
            carry += int(a[i])  # Add digit from a
            i -= 1
        if j >= 0:
            carry += int(b[j])  # Add digit from b
            j -= 1

        out += str(carry % 2)   # Add binary digit to result (0 or 1)
        carry //= 2             # Update carry (0 or 1)

    return out[::-1]  # Reverse the output string before returning


def main():
    # Test - 1
    a1 = "11"
    b1 = "1"
    print(f"output-1: {addBinary(a1, b1)}")

    # Test - 2
    a2 = "1010"
    b2 = "1011"
    print(f"output-2: {addBinary(a2, b2)}")

if __name__ == "__main__":
    main()
