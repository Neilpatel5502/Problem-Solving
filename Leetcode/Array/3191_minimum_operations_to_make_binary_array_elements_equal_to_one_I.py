# Problem Link: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i

# Time Complexity: O(n)
# Space Complexity: O(1)

def minOperations(nums):
    """
    Approach:
        - Simple brute force approach, whenever we find 0 flip bits from that 0 to and next 2 numbers.
        - Loop through n - 2, and check if last two elements are not 1 then it's impossible to get all
        elemnts 1 hence return -1. otherwise return `out` count.
    """

    n = len(nums)
    out = 0

    for i in range(n - 2):
        # Flip values when we found 0 in the nums for valid range.
        if nums[i] == 0:
            nums[i] = 1
            nums[i + 1] = 1 - nums[i + 1]
            nums[i + 2] = 1 - nums[i + 2]
            out += 1

    # If last two element does not conatin any 0 then return out otherwise return -1.
    if nums[-1] == 1 and nums[-2] == 1:
        return out
    else:
        return -1


def main():
    # Test - 1
    nums1 = [0,1,1,1,0,0]
    print(f"output-1: {minOperations(nums1)}")

    # Test - 2
    nums2 = [0,1,1,1]
    print(f"output-2: {minOperations(nums2)}")

    # Test - 3
    nums3 = [1,1,1]
    print(f"output-3: {minOperations(nums3)}")


if __name__ == "__main__":
    main()
