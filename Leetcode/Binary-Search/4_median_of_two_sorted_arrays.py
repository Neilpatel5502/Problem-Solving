# Problem: https://leetcode.com/problems/median-of-two-sorted-arrays

# Time Complexity: O(log(min(m, n))) – binary search on the shorter array
# Space Complexity: O(1) – constant space

def findMedianSortedArrays(nums1, nums2):
    """
    Approach:
        - Use binary search on the shorter array to partition both arrays.
        - Let A and B be the two arrays, and we ensure A is the smaller one.
        - Partition A and B such that left half has same number of elements as right half (or one more for odd).
        - Compare max of left parts and min of right parts to find the median.
        - If total length is odd, return min of right halves.
        - If even, return the average of max(lefts) and min(rights).
    """

    A, B = nums1, nums2
    total_len = len(A) + len(B)
    half = total_len // 2

    if len(A) > len(B):
        A, B = B, A  # Always binary search the shorter array

    l, r = 0, len(A) - 1

    while True:
        i = (l + r) // 2  # Partition index in A (Mid element of A)
        j = half - i - 2  # Corresponding partition in B (Mid element of B)

        Aleft = A[i] if i >= 0 else float("-inf")
        Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
        Bleft = B[j] if j >= 0 else float("-inf")
        Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

        # Partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            if total_len % 2 == 1:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

        # Move left in A
        elif Aleft > Bright:
            r = i - 1
        # Move right in A
        else:
            l = i + 1


def main():
    # Test - 1
    nums1 = [1, 3]
    nums2 = [2]
    print(f"output-1: {findMedianSortedArrays(nums1, nums2)}")

    # Test - 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(f"output-2: {findMedianSortedArrays(nums1, nums2)}")

if __name__ == "__main__":
    main()
