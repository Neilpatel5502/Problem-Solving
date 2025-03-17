# Problem Link: https://leetcode.com/problems/partition-array-according-to-given-pivot

# Time Complexity: O(n)
# Space Complexity: O(n)    In worst case we can get len of n less or equal or more list.

def pivotArray(nums, pivot):
    """
    Approach:
        - Simple Approach loop throght the nums and check if number is Less, more or equal
        to pivot number and maintain three list for that and return appended list of less, equal, greater.
    """

    less = []
    equal = []
    greater = []
    out = []

    # Loop through the elements of nums
    for n in nums:
        if n < pivot:
            less.append(n)
        elif n > pivot:
            greater.append(n)
        else:
            equal.append(n)

    # Append list less, equal and greater in order.
    out = less + equal + greater

    return out


def main():
    # Test - 1
    nums1 = [9,12,5,10,14,3,10]
    pivot1 = 10
    print(f"output-1: {pivotArray(nums1, pivot1)}")

    # Test - 2
    nums2 = [-3,4,3,2]
    pivot2 = 2
    print(f"output-2: {pivotArray(nums2, pivot2)}")

if __name__ == "__main__":
    main()
