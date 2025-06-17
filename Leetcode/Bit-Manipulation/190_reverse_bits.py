# Problem: https://leetcode.com/problems/reverse-bits

# Time Complexity: O(1)             # Fixed 32-bit iterations
# Space Complexity: O(1)            # Constant space used

def reverseBits(n):
    """
    Approach:
        - Iterate over all 32 bits of the input number.
        - For each bit position `i`:
            * Extract the i-th bit from the right using (n >> i) & 1.
            * Shift that bit to its new reversed position (31 - i).
            * Use bitwise OR to add it to the result.
        - This effectively mirrors the bits from left to right.
    """
    out = 0

    for i in range(32):
        bit = (n >> i) & 1           # Extract i-th bit from right
        out = out | (bit << (31 - i))  # Set bit at mirrored position

    return out


def main():
    # Test - 1
    n1 = 0b00000010100101000001111010011100
    print(f"output-1: {reverseBits(n1)}")

    # Test - 2
    n2 = 0b11111111111111111111111111111101
    print(f"output-2: {reverseBits(n2)}")

if __name__ == "__main__":
    main()
