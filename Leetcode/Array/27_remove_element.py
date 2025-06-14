# Problem: https://leetcode.com/problems/remove-element/

# Time Complexity: O(n)              # One pass through the array
# Space Complexity: O(1)             # In-place modification

def removeElement(nums, val):
    """
    Approach:
        - We want to remove all occurrences of `val` in-place and return the new length.
        - Use two pointers: `i` for scanning and `k` for keeping count of valid elements.
        - If nums[i] == val, pop and append it to the end to avoid disturbing the current structure.
        - Otherwise, increment count `k` and move to the next element.
        - A `counter` is used to ensure we don't loop infinitely due to pop-append.
    """
    k = 0              # Count of elements not equal to val
    i = 0              # Pointer to current index
    counter = 0        # Tracks number of iterations to prevent infinite loop

    while i < len(nums) and counter < len(nums):
        if nums[i] == val:
            # Remove and push to end to avoid shrinking len(nums)
            n = nums.pop(i)
            nums.append(n)
        else:
            k += 1
            i += 1

        counter += 1

    return k


def main():
    # Test - 1
    nums1 = [3,2,2,3]
    val1 = 3
    res1 = removeElement(nums1, val1)
    print(f"output-1: {res1}, nums: {nums1[:res1]}")

    # Test - 2
    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    res2 = removeElement(nums2, val2)
    print(f"output-2: {res2}, nums: {nums2[:res2]}")

if __name__ == "__main__":
    main()
