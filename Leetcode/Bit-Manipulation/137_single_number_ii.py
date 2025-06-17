# Problem: https://leetcode.com/problems/single-number-ii

# Time Complexity: O(n)                 # One pass through the array
# Space Complexity: O(1)                # Constant space for bit counters

def singleNumber(nums):
    """
    Approach:
        - This problem is a variation where every element appears three times except one.
        - Use bitwise manipulation with two counters:
            * `ones` keeps bits which have appeared once so far.
            * `twos` keeps bits which have appeared twice so far.
        - When a bit appears the third time, it gets removed from both `ones` and `twos`.
        - The logic ensures bits appearing exactly once stay in `ones`, and that's the result.
    """
    ones = 0  # Tracks bits seen once
    twos = 0  # Tracks bits seen twice

    for n in nums:
        # Add current number to `ones` if not in `twos`
        ones = (ones ^ n) & ~twos

        # Add current number to `twos` if not in updated `ones`
        twos = (twos ^ n) & ~ones

    return ones  # Only the number that appeared once remains in `ones`


def main():
    # Test - 1
    nums1 = [2, 2, 3, 2]
    print(f"output-1: {singleNumber(nums1)}")

    # Test - 2
    nums2 = [0, 1, 0, 1, 0, 1, 99]
    print(f"output-2: {singleNumber(nums2)}")

if __name__ == "__main__":
    main()
