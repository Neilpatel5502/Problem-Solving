# Problem: https://leetcode.com/problems/minimum-size-subarray-sum

# Time Complexity: O(n)
# Space Complexity: O(1)

def minSubArrayLen(target, nums):
    """
    Approach:
        - Use a sliding window approach with two pointers: left (l) and right (r).
        - Expand the window by moving `r` and add nums[r] to the current window sum.
        - When window_sum >= target, try to shrink the window from the left while maintaining the condition.
        - Update the minimum length whenever the condition is met.
        - If no valid subarray is found, return 0.
    """
    out = float('inf')  # To store minimum length found
    l = r = 0           # Sliding window pointers
    window_sum = 0      # Current sum of the window

    while r < len(nums):
        window_sum += nums[r]  # Expand window

        # Shrink window from the left as long as condition is satisfied
        while window_sum >= target:
            out = min(out, r - l + 1)
            window_sum -= nums[l]
            l += 1

        r += 1

    return 0 if out == float('inf') else out

def main():
    # Test - 1
    target1 = 7
    nums1 = [2,3,1,2,4,3]
    print(f"output-1: {minSubArrayLen(target1, nums1)}")

    # Test - 2
    target2 = 4
    nums2 = [1,4,4]
    print(f"output-2: {minSubArrayLen(target2, nums2)}")

    # Test - 3
    target3 = 11
    nums3 = [1,1,1,1,1,1,1,1]
    print(f"output-3: {minSubArrayLen(target3, nums3)}")

if __name__ == "__main__":
    main()
