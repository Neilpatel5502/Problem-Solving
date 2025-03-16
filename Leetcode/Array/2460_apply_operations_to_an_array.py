# Problem Link: https://leetcode.com/problems/apply-operations-to-an-array

# Time Complexity: O(n)
# Space Complexity: O(n)    In worst case zeros list might conatins all zeros from nums

def applyOperations(nums):
    """
    Approach:
    - Iterate through the list except for last element and apply the given operation:
        - If two consecutive elements are equal, double the first element and set the second one to 0.
    - After applying the operations, move all zeros to the end while maintaining the order of non-zero elements.
    """

    # Iterate through the list (except the last element)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] = nums[i] * 2
            nums[i + 1] = 0
        else:
            continue


    zero = nums.count(0)                # Count the number of zeros in the modified list
    nums = [i for i in nums if i!= 0]   # Remove all zeros from the list

    return nums + ([0] * zero)          # Append the zeros at the end and return the list

def main():
    # Test - 1
    nums1 = [1,2,2,1,1,0]
    print(f"output-1: {applyOperations(nums1)}")

    # Test - 2
    nums2 = [0,1]
    print(f"output-2: {applyOperations(nums2)}")

if __name__ == "__main__":
    main()
