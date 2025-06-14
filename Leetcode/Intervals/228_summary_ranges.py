# Problem: https://leetcode.com/problems/summary-ranges

# Time Complexity: O(n)
# Space Complexity: O(n)

def summaryRanges(nums):
    """
    Approach:
        - Iterate through the sorted list of numbers.
        - Track the start of each sequence.
        - When the sequence breaks, add a range to the output list.
        - Format ranges as "a->b" if a != b, otherwise just "a".
    """
    if not nums:
        return []

    out = []
    start = nums[0]  # Start of current range

    for i in range(1, len(nums)):
        # If current number is not consecutive
        if nums[i] != nums[i - 1] + 1:
            end = nums[i - 1]  # End of the current range
            if start == end:
                out.append(f"{start}")
            else:
                out.append(f"{start}->{end}")
            start = nums[i]  # Start a new range

    # Handle the last range
    end = nums[-1]
    if start == end:
        out.append(f"{start}")
    else:
        out.append(f"{start}->{end}")

    return out

def main():
    # Test - 1
    nums1 = [0, 1, 2, 4, 5, 7]
    print(f"output-1: {summaryRanges(nums1)}")

    # Test - 2
    nums2 = [0, 2, 3, 4, 6, 8, 9]
    print(f"output-2: {summaryRanges(nums2)}")

if __name__ == "__main__":
    main()
