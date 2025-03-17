# Problem Link: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values

# Time Complexity: O(n + m) -> n is len of nums1 and m is nums2.
# Space Complexity: O(n + m)

def mergeArrays(nums1, nums2):
    """
    Approach:
        - Use two pointers (`left` for `nums1` and `right` for `nums2`) to traverse both lists.
        - Compare the first element (`id`) of both lists:
            - If `id` matches in both lists, sum their values and add to the result.
            - If `id` in `nums1` is smaller, add `nums1[left]` to the result and move `left` forward.
            - If `id` in `nums2` is smaller, add `nums2[right]` to the result and move `right` forward.
        - Once one list is fully processed, append the remaining elements from the other list.
    """

    left = 0
    right = 0
    out = []

    while left < len(nums1) and right < len(nums2):
        if nums1[left][0] == nums2[right][0]:               # If IDs match, sum the values
            out.append([nums1[left][0], nums1[left][1] + nums2[right][1]])
            left += 1
            right += 1
        elif nums1[left][0] < nums2[right][0]:              # If nums1's ID is smaller, take it
            out.append(nums1[left])
            left += 1
        else:                                               # If nums2's ID is smaller, take it
            out.append(nums2[right])
            right += 1

    # If any elements remain in nums1, add them to output
    if left < len(nums1):
        out.extend(nums1[left:])

    # If any elements remain in nums2, add them to output
    if right < len(nums2):
        out.extend(nums2[right:])

    return out


def main():
    # Test - 1
    nums11 = [[1,2],[2,3],[4,5]]
    nums12 = [[1,4],[3,2],[4,1]]
    print(f"output-1: {mergeArrays(nums11, nums12)}")

    # Test - 2
    nums21 = [[2,4],[3,6],[5,5]]
    nums22 = [[1,3],[4,3]]
    print(f"output-2: {mergeArrays(nums21, nums22)}")


if __name__ == "__main__":
    main()
