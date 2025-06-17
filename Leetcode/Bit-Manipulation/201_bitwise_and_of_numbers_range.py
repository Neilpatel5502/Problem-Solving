# Problem: https://leetcode.com/problems/bitwise-and-of-numbers-range

# Time Complexity: O(log(right - left)) – number of bits in the numbers
# Space Complexity: O(1)

def rangeBitwiseAnd(left, right):
    """
    Approach:
        - To find the bitwise AND of all numbers from left to right, observe that
          only the common prefix bits of left and right remain set in the result.
        - Any differing bit position in left and right will eventually become 0 due to the AND operation.
        - So, right shift both left and right until they become equal to find the common prefix.
        - Count the number of shifts done and left shift the common prefix back to get the result.
    """
    shift = 0

    # Keep right shifting until both numbers become equal
    while left < right:
        left >>= 1      # Remove least significant bit
        right >>= 1
        shift += 1      # Track how many shifts we did

    # Shift back to form the final result with common prefix bits
    return left << shift


def main():
    # Test - 1
    left1, right1 = 5, 7
    print(f"output-1: {rangeBitwiseAnd(left1, right1)}")

    # Test - 2
    left2, right2 = 0, 0
    print(f"output-2: {rangeBitwiseAnd(left2, right2)}")

    # Test - 3
    left3, right3 = 12, 15
    print(f"output-3: {rangeBitwiseAnd(left3, right3)}")

if __name__ == "__main__":
    main()
