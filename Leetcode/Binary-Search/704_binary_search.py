# Problem: https://leetcode.com/problems/binary-search/
# Time Complexity: O(log n) – binary search divides the array in half each time
# Space Complexity: O(1) – constant space usage

def search(nums, target):
    """
    Approach:
        - Use binary search to find the target.
        - Initialize two pointers: l (left) and r (right).
        - While l <= r:
            - Calculate mid = (l + r) // 2
            - If nums[mid] == target, return mid.
            - If nums[mid] > target, discard right half by setting r = mid - 1.
            - If nums[mid] < target, discard left half by setting l = mid + 1.
        - If not found, return -1.
    """

    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2  # Midpoint of the current range

        if nums[mid] == target:
            return mid  # Target found
        elif nums[mid] > target:
            r = mid - 1  # Search in the left half
        else:
            l = mid + 1  # Search in the right half

    return -1  # Target not found


def main():
    # Test - 1
    nums1 = [-1,0,3,5,9,12]
    target1 = 9
    print(f"output-1: {search(nums1, target1)}")

    # Test - 2
    nums2 = [-1,0,3,5,9,12]
    target2 = 2
    print(f"output-2: {search(nums2, target2)}")

if __name__ == "__main__":
    main()
