# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array

# Time Complexity: O(n)              # Single pass through the list
# Space Complexity: O(1)             # In-place operation

def removeDuplicates(nums):
    """
    Approach:
        - We use the two-pointer technique (`left` and `right`) to overwrite duplicates in-place.
        - `left` points to the last unique element's position.
        - For each `right`, if it's different from `nums[left]`, we increment `left` and update nums[left].
        - The array is modified in-place with the first (left + 1) elements being unique.
        - Return `left + 1` as the new length of the unique part of the array.
    """
    left = 0     # Pointer to last unique element

    for right in range(1, len(nums)):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]  # Overwrite the next position with the unique value

    return left + 1


def main():
    # Test - 1
    nums1 = [1,1,2]
    res1 = removeDuplicates(nums1)
    print(f"output-1: {res1}, nums: {nums1[:res1]}")

    # Test - 2
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    res2 = removeDuplicates(nums2)
    print(f"output-2: {res2}, nums: {nums2[:res2]}")

if __name__ == "__main__":
    main()
