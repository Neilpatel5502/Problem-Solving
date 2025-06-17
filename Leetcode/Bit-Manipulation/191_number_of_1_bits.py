# Problem: https://leetcode.com/problems/number-of-1-bits

# Time Complexity: O(k)             # k = number of 1's in binary representation of n
# Space Complexity: O(1)            # Constant space

def hammingWeight(n):
    """
    Approach:
        - Use Brian Kernighan's Algorithm to count set bits (1s).
        - Each operation `n = n & (n - 1)` removes the rightmost 1-bit from n.
        - Count how many times this operation can be performed until n becomes 0.
        - The number of such operations equals the number of 1s in the binary representation.
    """
    out = 0

    while n:
        n = n & (n - 1)  # Remove the rightmost 1-bit
        out += 1         # Increment the count

    return out


def main():
    # Test - 1
    n1 = 11
    print(f"output-1: {hammingWeight(n1)}")

    # Test - 2
    n2 = 128
    print(f"output-2: {hammingWeight(n2)}")

    # Test - 3
    n3 = 2147483645
    print(f"output-3: {hammingWeight(n3)}")

if __name__ == "__main__":
    main()
