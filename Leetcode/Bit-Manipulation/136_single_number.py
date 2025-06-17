# Problem: https://leetcode.com/problems/single-number

# Time Complexity: O(n)              # One pass through the array
# Space Complexity: O(1)             # Constant space used

def singleNumber(nums):
    """
    Approach:
        - Use XOR to find the element that appears only once.
        - Properties of XOR:
            * x ^ x = 0
            * x ^ 0 = x
        - When every element appears twice except one, XORing all of them cancels out pairs.
        - The result will be the single unpaired number.
    """
    out = 0

    for n in nums:
        out ^= n  # XOR current number with result

    return out


def main():
    # Test - 1
    nums1 = [2, 2, 1]
    print(f"output-1: {singleNumber(nums1)}")

    # Test - 2
    nums2 = [4, 1, 2, 1, 2]
    print(f"output-2: {singleNumber(nums2)}")

    # Test - 3
    nums3 = [1]
    print(f"output-3: {singleNumber(nums3)}")

if __name__ == "__main__":
    main()
