# Problem: https://leetcode.com/problems/rotate-array

# Time Complexity: O(n)              # Each element is moved exactly once
# Space Complexity: O(k)             # Temporary list of last k elements

def rotate(nums, k):
    """
    Approach:
        - If k > len(nums), reduce it using modulo to avoid unnecessary full rotations.
        - Store the last k elements in a temporary list.
        - Shift the first (n - k) elements to the right by k positions in reverse order.
        - Overwrite the first k elements with the saved values.
        - The operation is done in-place with O(k) extra space.
    """
    k %= len(nums)  # Handle cases where k > len(nums)

    if k > 0:
        n = len(nums)
        temp = nums[n - k:]  # Save last k elements

        # Shift first (n - k) elements rightward by k positions (in reverse)
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]

        # Place the saved k elements at the beginning
        for i, val in enumerate(temp):
            nums[i] = val


def main():
    # Test - 1
    nums1 = [1,2,3,4,5,6,7]
    rotate(nums1, 3)
    print(f"output-1: {nums1}")

    # Test - 2
    nums2 = [-1,-100,3,99]
    rotate(nums2, 2)
    print(f"output-2: {nums2}")

if __name__ == "__main__":
    main()
