# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

# Time Complexity: O(log n) – binary search
# Space Complexity: O(1) – constant space

def findMin(nums):
    """
    Approach:
        - Use binary search to locate the inflection point where rotation happens.
        - The array is sorted but rotated, so the smallest element is the point where order breaks.
        - If nums[mid] > nums[right], minimum is in the right half (excluding mid).
        - Otherwise, it's in the left half (including mid).
        - Continue until left and right converge on the minimum.
    """

    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2

        if nums[mid] > nums[r]:
            l = mid + 1  # Minimum must be to the right of mid
        else:
            r = mid  # Minimum is at mid or to the left

    return nums[r]  # or nums[l], both are same when l == r


def main():
    # Test - 1
    nums1 = [3,4,5,1,2]
    print(f"output-1: {findMin(nums1)}")

    # Test - 2
    nums2 = [4,5,6,7,0,1,2]
    print(f"output-2: {findMin(nums2)}")

    # Test - 3
    nums3 = [11,13,15,17]
    print(f"output-3: {findMin(nums3)}")

if __name__ == "__main__":
    main()
