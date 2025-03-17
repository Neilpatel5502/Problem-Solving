# Problem Link: https://leetcode.com/problems/divide-array-into-equal-pairs

# Time Complexity: O(n)
# Space Complexity: O(n)    Because of Counter Map.

from collections import defaultdict

def divideArray(nums):
    """
    Approach:
        - We are having 2 * n integers and need to divide them in n pairs, so We have to check
        count of each numbers in nums list are even or not.
    """
    # Couter dict to count occurences of numbers.
    counter = defaultdict(int)

    for n in nums:
        counter[n] += 1

    # Check that any value of number is odd, if odd return False otherwise Return True.
    for c in counter.values():
        if c % 2 != 0:
            return False

    return True

def main():
    # Test - 1
    nums1 = [3,2,3,2,2,2]
    print(f"output-1: {divideArray(nums1)}")

    # Test - 2
    nums2 = [1,2,3,4]
    print(f"output-2: {divideArray(nums2)}")

if __name__ == "__main__":
    main()
