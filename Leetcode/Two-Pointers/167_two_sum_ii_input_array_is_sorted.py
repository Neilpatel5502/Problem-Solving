# Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Time Complexity: O(n) – one pass through the array
# Space Complexity: O(1) – constant extra space used (two pointers)

def twoSum(numbers, target):
    """
    Approach:
        - Use two pointers starting at the beginning (L) and end (R) of the array.
        - Since the array is sorted:
            - If the sum is greater than the target, move the right pointer left.
            - If the sum is less than the target, move the left pointer right.
            - If the sum equals the target, return the 1-based indices [L+1, R+1].
    """

    # Initialize two pointers
    L, R = 0, len(numbers) - 1

    while L < R:
        # Compute sum of elements at current pointers
        current_sum = numbers[L] + numbers[R]

        # Sum too large, move right pointer left to reduce sum
        if current_sum > target:
            R -= 1

        # Sum too small, move left pointer right to increase sum
        elif current_sum < target:
            L += 1

        # Found the two numbers, return 1-based indices
        else:
            return [L + 1, R + 1]


def main():
    # Test - 1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    print(f"output-1: {twoSum(numbers1, target1)}")

    # Test - 2
    numbers2 = [2, 3, 4]
    target2 = 6
    print(f"output-2: {twoSum(numbers2, target2)}")

    # Test - 3
    numbers3 = [-1, 0]
    target3 = -1
    print(f"output-3: {twoSum(numbers3, target3)}")

if __name__ == "__main__":
    main()
