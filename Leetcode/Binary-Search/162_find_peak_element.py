# Problem: https://leetcode.com/problems/find-peak-element

# Time Complexity: O(log n) - In the worst case, we might inspect every element.
# Space Complexity: O(1) - Constant extra space used aside from input modification.

def findPeakElement(nums):
    """
    Approach:
        - A peak element is greater than its neighbors.
        - To avoid edge conditions, insert -∞ at both ends of the array.
        - Use two pointers (`left` and `right`) starting from both ends, and move inward.
        - Check if `nums[left]` or `nums[right]` is greater than its neighbors.
        - If found, return the original index (adjusted for the inserted -∞).
        - If no peak found during the loop, return 0 (though this shouldn't happen due to problem guarantees).
    """
    left = 1
    right = len(nums)

    # Pad the list with -inf at both ends to simplify boundary checks
    nums.insert(0, float('-inf'))
    nums.append(float('-inf'))

    while left <= right:
        # Check if current left pointer is a peak
        if nums[left] > nums[left - 1] and nums[left] > nums[left + 1]:
            return left - 1  # Adjust for the inserted -inf at start

        # Check if current right pointer is a peak
        if nums[right] > nums[right - 1] and nums[right] > nums[right + 1]:
            return right - 1  # Adjust for the inserted -inf at start

        left += 1
        right -= 1

    # Fallback return (shouldn't be reached for valid inputs)
    return 0


def main():
    # Test - 1
    nums1 = [1, 2, 3, 1]
    print(f"output-1: {findPeakElement(nums1)}")

    # Test - 2
    nums2 = [1, 2, 1, 3, 5, 6, 4]
    print(f"output-2: {findPeakElement(nums2)}")

if __name__ == "__main__":
    main()
