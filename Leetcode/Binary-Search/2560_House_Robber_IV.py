# Problem Link: https://leetcode.com/problems/house-robber-iv

# Time Complexity: O(n log m) -> n is len of nums and m is max(nums) - min(nums).
# Space Complexity: O(1).

def minCapability(nums, k):
    """
    Approach:
        - The solution uses binary search on the range of possible values (from min(nums) to max(nums)).
        - A greedy approach is used to count how many houses can be robbed given a threshold `mid`
        (current binary search middle value)
    Steps:
        1. Set `left` as the smallest house value and `right` as the largest.
        2. Perform **binary search** on this range to find the minimum possible capability.
        3. For a given middle value `mid`, count how many non-adjacent houses can be robbed with values ≤ `mid`.
        4. If the count is at least `k`, search in the lower half (`right = mid`).
        5. Otherwise, search in the upper half (`left = mid + 1`).
        6. The final answer is stored in `left` when `left == right`.
    """
    left, right = min(nums), max(nums)

    while left < right:
        mid = (left + right) // 2
        c = 0           # Count of non-adjacent houses that can be robbed
        i = 0           # Index pointer

        # Try to rob houses without picking adjacent ones
        while i < len(nums):
            if nums[i] <= mid:
                c += 1
                i += 1
            i += 1

        # If at least `k` houses can be robbed, search in the lower range
        if c >= k:
            right = mid
        else:
            left = mid + 1

    return left

def main():
    # Test - 1
    nums1 = [2,3,5,9]
    k1 = 2
    print(f"output-1: {minCapability(nums1, k1)}")

    # Test - 2
    nums2 = [2,7,9,3,1]
    k2 = 2
    print(f"output-2: {minCapability(nums2, k2)}")


if __name__ == "__main__":
    main()
