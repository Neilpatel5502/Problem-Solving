# Problem: https://leetcode.com/problems/two-sum/
# Time Complexity: O(n) - where n is the length of the input list `nums`
# Space Complexity: O(n) - for storing elements in the hash map

def twoSum(nums, target):
    """
    Approach:
        - Use a hash map `temp` to store numbers and their indices.
        - Iterate over the array using index `i` and number `n`.
        - For each number, compute its complement (`diff = target - n`).
        - If the complement exists in the hash map, return the stored index and current index.
        - Otherwise, add the current number and index to the hash map.
    """

    temp = {}  # Dictionary to store value: index

    for i, n in enumerate(nums):
        diff = target - n  # Calculate the complement

        if diff in temp:
            return [temp[diff], i]  # Found the pair

        temp[n] = i  # Store the index of the current number


def main():
    # Test - 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"output-1: {twoSum(nums1, target1)}")

    # Test - 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"output-2: {twoSum(nums2, target2)}")

    # Test - 3
    nums3 = [3, 3]
    target3 = 6
    print(f"output-3: {twoSum(nums3, target3)}")

if __name__ == "__main__":
    main()
