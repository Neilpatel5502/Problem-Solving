# Problem: https://leetcode.com/problems/jump-game-ii

# Time Complexity: O(n)              # Each index is visited at most once
# Space Complexity: O(1)             # No extra space used

def jump(nums):
    """
    Approach:
        - Use a greedy strategy to minimize the number of jumps.
        - `l` and `r` define the current range (window) we can reach with the current number of jumps.
        - Within each window, find the farthest index we can reach (max_jump).
        - Once we process the full window, increment the jump count and move the window forward.
        - Repeat until the end of the array is reachable.
    """
    out = 0         # Total jumps
    l = r = 0       # Current window bounds

    # Continue until the right pointer reaches or crosses the last index
    while r < len(nums) - 1:
        max_jump = 0

        # Within the current window, find the farthest jump possible
        for i in range(l, r + 1):
            max_jump = max(max_jump, i + nums[i])

        # Move the window to the new range
        l = r + 1
        r = max_jump
        out += 1    # Increment the jump count

    return out


def main():
    # Test - 1
    nums1 = [2,3,1,1,4]
    print(f"output-1: {jump(nums1)}")

    # Test - 2
    nums2 = [2,3,0,1,4]
    print(f"output-2: {jump(nums2)}")

if __name__ == "__main__":
    main()
