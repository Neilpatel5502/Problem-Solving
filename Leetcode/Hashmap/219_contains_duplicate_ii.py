# Problem: https://leetcode.com/problems/contains-duplicate-ii

# Time Complexity: O(n), where n = length of nums
# Space Complexity: O(n), for storing the indices in a hash map

def containsNearbyDuplicate(nums, k):
    """
    Approach:
        - Use a dictionary `temp` to store the last seen index of each number.
        - Iterate through the list with index `i` and value `num`.
        - If `num` was seen before and the difference between current index and last seen index is ≤ k, return True.
        - Otherwise, update the index of `num` in the dictionary.
        - Return False if no such pair is found.
    """
    temp = {}

    for i, num in enumerate(nums):
        if num in temp:
            if abs(i - temp[num]) <= k:
                return True  # Found duplicate within allowed range

        temp[num] = i  # Update the latest index of the number

    return False  # No valid duplicate found

def main():
    # Test - 1
    nums1 = [1, 2, 3, 1]
    k1 = 3
    print(f"output-1: {containsNearbyDuplicate(nums1, k1)}")

    # Test - 2
    nums2 = [1, 0, 1, 1]
    k2 = 1
    print(f"output-2: {containsNearbyDuplicate(nums2, k2)}")

    # Test - 3
    nums3 = [1, 2, 3, 1, 2, 3]
    k3 = 2
    print(f"output-3: {containsNearbyDuplicate(nums3, k3)}")

if __name__ == "__main__":
    main()
