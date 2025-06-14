# Problem: https://leetcode.com/problems/longest-consecutive-sequence/

# Time Complexity: O(n)
# Space Complexity: O(n)

def longestConsecutive(nums):
    """
    Approach:
        - Convert the list to a set for O(1) lookups and eliminate duplicates.
        - Use a hash map `temp` to store the length of consecutive sequences at boundary elements.
        - For each number:
            - Check lengths of sequences on the left (n - 1) and right (n + 1).
            - The new sequence length = left + right + 1.
            - Update both boundaries of the sequence in the hash map.
        - Keep track of the maximum sequence length seen so far.
    """
    nums = set(nums)  # Remove duplicates and allow O(1) lookup
    temp = {}         # Stores sequence lengths at boundaries
    out = 0           # Stores the longest sequence length

    for n in nums:
        a = temp.get(n - 1, 0)       # Length of left sequence
        b = temp.get(n + 1, 0)       # Length of right sequence
        value = a + b + 1            # New sequence length including n

        # Update sequence boundaries
        temp[n - a] = value          # Left boundary
        temp[n + b] = value          # Right boundary

        out = max(out, value)        # Update max length

    return out


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
