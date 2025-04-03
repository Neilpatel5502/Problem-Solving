# Problem Link: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i
# Problem Link: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii

# Time Complexity: O(n)
# Space Complexity: O(1)

def maximumTripletValue(nums):
    """
    Approach:
    - Iterate through the array while keeping track of:
        - max_value: The maximum value encountered so far.
        - max_diff: The maximum difference (nums[i] - nums[j]) encountered so far.
        - output: The maximum triplet value found.
    - For each element:
        - Update the maximum possible triplet value using max_diff * nums[k].
        - Update max_diff by considering the current max_value - nums[j].
        - Update max_value if the current element is the largest seen so far.
    - Return the maximum triplet value found, or 0 if all are negative.
    """
    output = 0
    max_diff = 0    # Tracks the maximum (nums[i] - nums[j]) encountered
    max_value = 0   # Tracks the maximum nums[i] encountered

    for n in nums:
        # Compute the potential maximum triplet value using current max_diff and n
        output = max(output, max_diff * n)

        # Update max_diff using the current max_value
        max_diff = max(max_diff, max_value - n)

        # Update max_value to the maximum element seen so far
        max_value = max(max_value, n)

    return output


def main():
    # Test - 1
    nums1 = [12,6,1,2,7]
    print(f"output-1: {maximumTripletValue(nums1)}")

    # Test - 2
    nums2 = [1,10,3,4,19]
    print(f"output-2: {maximumTripletValue(nums2)}")

    # Test - 3
    nums3 = [1,2,3]
    print(f"output-3: {maximumTripletValue(nums3)}")

if __name__ == "__main__":
    main()
