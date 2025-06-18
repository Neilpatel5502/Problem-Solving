# Problem: https://leetcode.com/problems/house-robber

from functools import lru_cache

# Time Complexity: O(n)        — Each house is visited once
# Space Complexity: O(n)       — Due to memoization cache (implicit recursion stack)
def rob_top_down(nums):
    """
    Approach:
        - Use top-down recursion with memoization (DFS).
        - Define dfs(i) as the max money we can rob starting at index i.
        - At each house, we can:
            1. Rob it and jump to i+2 or i+3
            2. Skip it (handled by trying both dfs(0) and dfs(1))
        - Use lru_cache to store and reuse intermediate results.
    """
    n = len(nums)

    # Recursive DFS with memoization
    @lru_cache
    def dfs(i):
        if i >= n:
            return 0

        # Rob current house and move to i+2 or i+3
        out = nums[i] + max(dfs(i + 2), dfs(i + 3))
        return out

    # Try robbing from index 0 or 1
    return max(dfs(0), dfs(1))



# Time Complexity: O(n)        # One pass through the list
# Space Complexity: O(n)       # DP array of size n + 3
def rob_bottom_up(nums):
    """
    Approach:
        - Use bottom-up dynamic programming.
        - Define dp[i] as the maximum amount we can rob starting from house i.
        - For each house, we have two choices:
            1. Rob current house and move to i+2
            2. Rob current house and move to i+3
        - We fill the dp array from the end toward the beginning.
        - Finally, we return the max of dp[0] and dp[1], covering both entry points.
    """
    n = len(nums)
    dp = [0] * (n + 3)  # Extra 3 to avoid index out of range for i+2 and i+3

    # Build the dp array in reverse
    for i in range(n - 1, -1, -1):
        # Rob current house and take best of robbing at i+2 or i+3 next
        dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])

    # Either rob from index 0 or skip to 1
    return max(dp[0], dp[1])


def main():
    # Test 1:
    nums1 = [1, 2, 3, 1]

    print(f"Top- Down output-1: {rob_top_down(nums1)}")
    print(f"Bottom-UP output-1: {rob_bottom_up(nums1)}\n")

    # Test 2:
    nums2 = [2, 7, 9, 3, 1]
    print(f"Top- Down output-2: {rob_top_down(nums2)}")
    print(f"Bottom-UP output-2: {rob_bottom_up(nums2)}")

if __name__ == "__main__":
    main()
