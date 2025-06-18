# Problem: https://leetcode.com/problems/longest-increasing-subsequence

from functools import lru_cache

# Time Complexity: O(n^2) - for each index, we may explore all subsequent indices
# Space Complexity: O(n) - due to recursion stack and caching
def lengthOfLIS_top_down(nums):
    """
    Approach:
        - Use DFS with memoization to find the longest increasing subsequence starting at each index.
        - For each index `i`, recursively find the LIS that can be formed by considering all elements after `i`.
        - If nums[i] < nums[j], then nums[j] can be part of the subsequence.
        - Memoize the results to avoid recomputation and return the maximum LIS from any index.
    """
    n = len(nums)

    @lru_cache
    def dfs(i):
        LIS = 1  # At minimum, LIS starting at index i includes nums[i] itself

        # Explore further elements to extend the subsequence
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                LIS = max(LIS, 1 + dfs(j))  # Update LIS if nums[j] extends the sequence

        return LIS

    # Run dfs starting at each index and return the maximum LIS found
    return max(dfs(i) for i in range(n))



# Time Complexity: O(n^2) - nested loop over the array
# Space Complexity: O(n) - to store the LIS values
def lengthOfLIS_bottom_up(nums):
    """
    Approach:
        - Use bottom-up dynamic programming to compute LIS at each index.
        - Initialize a DP array `LIS` where LIS[i] stores the length of the longest increasing subsequence starting at index i.
        - Iterate from the end of the array to the beginning.
        - For each index `i`, look at all `j > i` and update LIS[i] if nums[j] > nums[i].
        - Return the maximum value from the LIS array as the final result.
    """
    LIS = [1] * len(nums)  # Initialize LIS array with 1 for each element

    # Build the LIS array from right to left
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])  # Update LIS if increasing subsequence found

    return max(LIS)  # Final result is the maximum value in the LIS array


def main():
    # Test - 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Top-Down output-1: {lengthOfLIS_top_down(nums1)}")
    print(f"Bottom-Up output-1: {lengthOfLIS_bottom_up(nums1)}\n")

    # Test - 2
    nums2 = [0, 1, 0, 3, 2, 3]
    print(f"Top- Down output-2: {lengthOfLIS_top_down(nums2)}")
    print(f"Bottom-Up output-2: {lengthOfLIS_bottom_up(nums2)}\n")

    # Test - 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    print(f"Top- Down output-3: {lengthOfLIS_top_down(nums3)}")
    print(f"Bottom-Up output-3: {lengthOfLIS_bottom_up(nums3)}")

if __name__ == "__main__":
    main()
