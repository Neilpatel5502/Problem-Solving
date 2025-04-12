# Problem: https://leetcode.com/problems/sliding-window-maximum/
# Time Complexity: O(n) – each element is added and removed from deque at most once
# Space Complexity: O(k) – for deque that stores indices of elements in the window

from collections import deque

def maxSlidingWindow(nums, k):
    """
    Approach:
        - Use a deque to store indices of elements in decreasing order of values.
        - The front of the deque always holds the index of the maximum value in the current window.
        - For each new element:
            - Remove indices from the back if their corresponding values are less than the current value.
            - Remove the front if it's outside the current window.
            - Append current index.
        - Start adding max values to output once the first window is formed.
    """

    out = []
    queue = deque()  # Stores indices, values are in decreasing order
    left = right = 0

    while right < len(nums):
        # Remove smaller elements from the back
        while queue and nums[queue[-1]] < nums[right]:
            queue.pop()

        queue.append(right)

        # Remove indices from the front if they are out of the current window
        if queue[0] < left:
            queue.popleft()

        # Append to output once the first full window is reached
        if (right + 1) >= k:
            out.append(nums[queue[0]])
            left += 1  # Move the window

        right += 1

    return out


def main():
    # Test - 1
    nums1 = [1,3,-1,-3,5,3,6,7]
    k1 = 3
    print(f"output-1: {maxSlidingWindow(nums1, k1)}")

    # Test - 2
    nums2 = [1]
    k2 = 1
    print(f"output-2: {maxSlidingWindow(nums2, k2)}")

if __name__ == "__main__":
    main()
