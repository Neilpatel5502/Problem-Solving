# Problem: https://leetcode.com/problems/factorial-trailing-zeroes

# Time Complexity: O(log₅(n)) – because we divide n by powers of 5
# Space Complexity: O(1)

def trailingZeroes(n):
    """
    Approach:
        - A trailing zero is created with every pair of (2, 5) in the factors.
        - Since there are always more 2s than 5s in a factorial, we just count the number of 5s.
        - For each power of 5 (5, 25, 125, ...), count how many times it divides `n`.
        - This gives the total number of trailing zeros in n!.
    """
    out = 0
    div = 5

    # Keep dividing n by powers of 5
    while div <= n:
        out += n // div  # Count how many numbers <= n are divisible by current power of 5
        div *= 5         # Move to next power of 5

    return out


def main():
    # Test - 1
    n1 = 3
    print(f"output-1: {trailingZeroes(n1)}")

    # Test - 2
    n2 = 5
    print(f"output-2: {trailingZeroes(n2)}")

    # Test - 3
    n3 = 0
    print(f"output-3: {trailingZeroes(n3)}")

if __name__ == "__main__":
    main()
