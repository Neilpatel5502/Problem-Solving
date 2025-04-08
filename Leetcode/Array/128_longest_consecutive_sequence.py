# Problem: https://leetcode.com/problems/longest-consecutive-sequence/
# Time Complexity: O(n) - each number is processed at most once
# Space Complexity: O(n) - for storing the set of numbers

def longestConsecutive(nums):
    """
    Approach:
        - Convert the input list to a set for O(1) lookups.
        - Iterate through each number in the set:
            - Only start counting if the current number is the beginning of a sequence (i.e., n - 1 not in set).
            - Use a while loop to count how long the sequence continues.
        - Keep track of the maximum sequence length encountered.
    """

    nums = set(nums)  # Convert list to set for O(1) lookup
    lcs = 0  # Longest consecutive sequence

    for n in nums:
        # Check if n is the start of a sequence
        if n - 1 not in nums:
            counter = 1
            while (n + counter) in nums:
                counter += 1

            lcs = max(lcs, counter)  # Update max sequence length

    return lcs


def main():
    # Test - 1
    nums1 = [100, 4, 200, 1, 3, 2]
    print(f"output-1: {longestConsecutive(nums1)}")

    # Test - 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(f"output-2: {longestConsecutive(nums2)}")

    # Test - 3
    nums3 = [1,0,1,2]
    print(f"output-3: {longestConsecutive(nums3)}")

if __name__ == "__main__":
    main()
