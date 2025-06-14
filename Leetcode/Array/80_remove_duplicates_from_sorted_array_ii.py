# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

# Time Complexity: O(n)              # Single pass through the list
# Space Complexity: O(1)             # In-place operation

def removeDuplicates(nums):
    """
    Approach:
        - Goal: Allow at most 2 duplicates of each element in the sorted array.
        - Use two pointers:
            - `left`: points to the last valid index for writing unique or allowed duplicates.
            - `right`: iterates over the array starting from index 1.
        - Maintain a `dup` counter to track how many times the current value has appeared.
        - If nums[right] == nums[left]:
            - If dup == 0, allow it (second occurrence), update `dup`, and write to nums.
        - If nums[right] != nums[left], it's a new number:
            - Reset dup to 0 and update the next position.
        - Return the new length as `left + 1`.
    """
    left, dup = 0, 0  # left: position to write next, dup: # of extra duplicates seen

    for right in range(1, len(nums)):
        if nums[left] == nums[right]:
            # Duplicate found
            if dup == 0:
                # First duplicate is allowed
                dup += 1
                left += 1
                nums[left] = nums[right]

            # If dup == 1, skip this element (more than two duplicates not allowed)

        else:
            # New number found, reset duplicate counter
            dup = 0
            left += 1
            nums[left] = nums[right]

    return left + 1


def main():
    # Test - 1
    nums1 = [1,1,1,2,2,3]
    res1 = removeDuplicates(nums1)
    print(f"output-1: {res1}, nums: {nums1[:res1]}")

    # Test - 2
    nums2 = [0,0,1,1,1,1,2,3,3]
    res2 = removeDuplicates(nums2)
    print(f"output-2: {res2}, nums: {nums2[:res2]}")

if __name__ == "__main__":
    main()
