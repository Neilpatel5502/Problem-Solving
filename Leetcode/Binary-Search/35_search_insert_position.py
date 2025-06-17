# Problem: https://leetcode.com/problems/search-insert-position

# Time Complexity: O(log n) - Binary search halves the search space each iteration
# Space Complexity: O(1) - Constant extra space used

def searchInsert(nums, target):
    """
    Approach:
        - Use binary search to find the index of the target or where it should be inserted.
        - Initialize two pointers `left` and `right` to denote the search boundaries.
        - While left < right:
            - Calculate mid index.
            - If nums[mid] == target, return mid (found target).
            - If nums[mid] < target, discard left half including mid.
            - Else, discard right half excluding mid.
        - If target not found, `left` will point to the correct insert position.
    """
    # Took right = len(nums) to handle case where number will be inserted at last.
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        # If the mid element is the target, return its index
        if nums[mid] == target:
            return mid
        # If mid element is less than target, search right half
        elif nums[mid] < target:
            left = mid + 1
        # If mid element is greater, search left half including mid
        else:
            right = mid

    # Target not found, return insertion index
    return left


def main():
    # Test - 1
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(f"output-1: {searchInsert(nums1, target1)}")

    # Test - 2
    nums2 = [1, 3, 5, 6]
    target2 = 2
    print(f"output-2: {searchInsert(nums2, target2)}")

    # Test - 3
    nums3 = [1, 3, 5, 6]
    target3 = 7
    print(f"output-3: {searchInsert(nums3, target3)}")

if __name__ == "__main__":
    main()
