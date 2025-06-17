# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array

# Time Complexity: O(log n) – binary search
# Space Complexity: O(1) – constant space

def search(nums, target):
    """
    Approach:
        - Use binary search to find the target in a rotated sorted array.
        - At each step, check if the left or right half is sorted:
            - If left half is sorted and target is within it, discard the right half.
            - If right half is sorted and target is within it, discard the left half.
        - Adjust pointers accordingly to narrow the search space.
    """

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid  # Target found

        # Determine which half is sorted
        if nums[l] <= nums[mid]:  # Left half is sorted
            if nums[l] <= target < nums[mid]:
                r = mid - 1  # Target in left half
            else:
                l = mid + 1  # Target in right half
        else:  # Right half is sorted
            if nums[mid] < target <= nums[r]:
                l = mid + 1  # Target in right half
            else:
                r = mid - 1  # Target in left half

    return -1  # Target not found


def main():
    # Test - 1
    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    print(f"output-1: {search(nums1, target1)}")

    # Test - 2
    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    print(f"output-2: {search(nums2, target2)}")

    # Test - 3
    nums3 = [1]
    target3 = 0
    print(f"output-3: {search(nums3, target3)}")

if __name__ == "__main__":
    main()
