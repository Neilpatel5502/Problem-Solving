# Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

# Time Complexity: O(log n + k), where k is the number of occurrences of target (O(log n) for binary search + O(k) for expansion)
# Space Complexity: O(1) - No extra space used beyond variables

def searchRange(nums, target):
    """
    Approach:
        - Perform binary search to find any occurrence of the target.
        - If found, expand to the left and right to find the full range where the target appears.
        - Return the start and end indices.
        - If not found, return [-1, -1].
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Found target, now expand outward to find full range
        if nums[mid] == target:
            start = mid
            end = mid

            # Expand leftward while matching target
            while start - 1 >= 0 and nums[start - 1] == target:
                start -= 1

            # Expand rightward while matching target
            while end + 1 < len(nums) and nums[end + 1] == target:
                end += 1

            return [start, end]

        # If target is greater, discard left half
        elif nums[mid] < target:
            left = mid + 1
        # If target is smaller, discard right half
        else:
            right = mid - 1

    # Target not found
    return [-1, -1]


def main():
    # Test - 1
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    print(f"output-1: {searchRange(nums1, target1)}")

    # Test - 2
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    print(f"output-2: {searchRange(nums2, target2)}")

    # Test - 3
    nums3 = []
    target3 = 0
    print(f"output-3: {searchRange(nums3, target3)}")

if __name__ == "__main__":
    main()
