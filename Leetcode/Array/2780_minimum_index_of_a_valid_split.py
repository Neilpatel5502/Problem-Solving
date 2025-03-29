# Problem Link: https://leetcode.com/problems/minimum-index-of-a-valid-split

# Time Complexity: O(n)         where n is the length of nums, since we make two passes.
# Space Complexity: O(n)

from collections import Counter

def minimumIndex(nums):
    """
    Approach:
        - First, determine the dominant element (the one that appears more than half the time).
        - Iterate through the array to find the first valid split where:
        - The dominant element remains dominant in both left and right subarrays.
        - Use two counters: one for tracking occurrences in the left subarray and one for the right.
        - The first index that satisfies the split condition is returned.

    Time Complexity: O(n) where n is the length of nums, since we make two passes.
    """

    counter = Counter(nums)             # Count occurrences of each number in nums
    N = len(nums)
    dominant = -1                       # Variable to store the dominant element

    # Find the dominant element (appears more than half of the array length)
    for x in counter:
        if counter[x]*2 > N:
            dominant = x
            break

    # If no dominant element is found, return -1
    if dominant == -1:
        return -1

    left_count = 0                      # Count of dominant element in left subarray
    right_count = counter[dominant]     # Count of dominant element in right subarray

    # Iterate through the array to find the minimum valid split index
    for i, x in enumerate(nums):
        if x == dominant:
            left_count += 1             # Increment left count when encountering dominant element
            right_count -= 1            # Decrement right count

        # Check if dominant remains dominant in both subarrays
        if 2 * left_count > i + 1 and 2 * right_count > N - i - 1:
            return i                    # Return the first valid split index

    return -1


def main():
    # Test - 1
    nums1 = [1,2,2,2]
    print(f"output-1: {minimumIndex(nums1)}")

    # Test - 2
    nums2 = [2,1,3,1,1,1,7,1,2,1]
    print(f"output-2: {minimumIndex(nums2)}")

    # Test - 3
    nums3 = [3,3,3,3,7,2,2]
    print(f"output-3: {minimumIndex(nums3)}")

if __name__ == "__main__":
    main()
