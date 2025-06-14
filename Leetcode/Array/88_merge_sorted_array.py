# Problem: https://leetcode.com/problems/merge-sorted-array/

# Time Complexity: O(m + n)        # Each element is visited at most once
# Space Complexity: O(1)           # In-place modification of nums1

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.

    Approach:
        - We are given two sorted arrays, nums1 and nums2.
        - nums1 has a size of m + n with the last n elements being empty space (zeros).
        - Goal is to merge nums2 into nums1 so that nums1 becomes a single sorted array.
        - We use two pointers `i` for nums1 and `j` for nums2, and `c` to count valid elements from original nums1.
        - If nums1[i] is smaller, we move ahead.
        - If nums2[j] needs to be inserted, we pop the last element (extra zero) from nums1 and insert nums2[j] at the correct position.
    """

    i = j = 0       # i for nums1, j for nums2
    c = 0           # counter for elements in original nums1 used (up to m)

    while i < len(nums1) and j < len(nums2):
        if c >= m:
            # If we've placed all original nums1 elements, copy over from nums2
            nums1[i:] = nums2[j:]
            break
        elif nums1[i] < nums2[j]:
            c += 1
            i += 1
        else:
            nums1.pop()
            nums1.insert(i, nums2[j])
            i += 1
            j += 1


def main():
    # Test - 1
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)
    print(f"output-1: {nums1}")

    # Test - 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    print(f"output-2: {nums1}")

    # Test - 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(f"output-3: {nums1}")

if __name__ == "__main__":
    main()
