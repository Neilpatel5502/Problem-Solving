# Problem: https://leetcode.com/problems/product-of-array-except-self/
# Time Complexity: O(n) - single pass for prefix, suffix, and final output
# Space Complexity: O(n) - for storing prefix and suffix arrays

def productExceptSelf(nums):
    """
    Approach:
        - Create two arrays: prefix_mul and suffix_mul.
        - prefix_mul[i] stores the product of all elements before index i.
        - suffix_mul[i] stores the product of all elements after index i.
        - Final result at index i is the product of prefix_mul[i] and suffix_mul[i].
        - This avoids using division and ensures O(n) time complexity.
    """

    prefix_mul = [1] * len(nums)  # To store prefix products
    suffix_mul = [1] * len(nums)  # To store suffix products

    # Build prefix product array
    for i in range(1, len(nums)):
        prefix_mul[i] = prefix_mul[i - 1] * nums[i - 1]

    # Build suffix product array
    for j in range(len(nums) - 1, 0, -1):
        suffix_mul[j - 1] = suffix_mul[j] * nums[j]

    # Final result: product of prefix and suffix at each index
    return [prefix_mul[i] * suffix_mul[i] for i in range(len(nums))]


def main():
    # Test - 1
    nums1 = [1, 2, 3, 4]
    print(f"output-1: {productExceptSelf(nums1)}")

    # Test - 2
    nums2 = [-1,1,0,-3,3]
    print(f"output-2: {productExceptSelf(nums2)}")

if __name__ == "__main__":
    main()
