# Problem Link: https://leetcode.com/problems/longest-nice-subarray

# Time Complexity: O(n)
    # For loops runs for n - 1 times and while loop only runs when (summation & nums[right]) != 0, and in total,
    # the left pointer moves across all elements at most once.

# Space Complexity: O(1)

def longestNiceSubarray(nums):
    """
    Approach:
        - This is Sliding window problem, Here we are checking that bitwise AND of all pair in
        Window left to right is 0.
        - To check that we are increasing right pointer every time, but we only increase left pointer
        When one of the Pair has AND not 0.
        - If we increase window that means all the previous elements are valid so, we can check previous
        elements total sum and try to AND with right pointer's element is 0 or not. That will check for all
        other elemts with newly added number in the window.
    """
    left = 0
    output = 1
    summation = nums[0]         # Intially sum is first number

    # Loop through right pointer from 1 to end.
    for right in range(1, len(nums)):
        # Loop till we find 0 for previous numbers sum and right's AND ans 0.
        while (summation & nums[right]) != 0:
            # Discard left element from window
            summation -= nums[left]
            left += 1               # Increment left pointer

        # Add right pointer element
        summation += nums[right]
        output = max(output, right - left + 1)

    return output


def main():
    # Test - 1
    nums1 = [1,3,8,48,10]
    print(f"output-1: {longestNiceSubarray(nums1)}")

    # Test - 2
    nums2 = [3,1,5,11,13]
    print(f"output-2: {longestNiceSubarray(nums2)}")


if __name__ == "__main__":
    main()
