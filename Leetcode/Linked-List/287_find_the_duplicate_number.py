# Problem: https://leetcode.com/problems/find-the-duplicate-number/
# Time Complexity: O(n)        # One pass to detect cycle, one to find entrance
# Space Complexity: O(1)       # Uses constant extra space

# Constraint: Do not modify input array

def findDuplicate(nums):
    """
    Approach:
        - Treat the array as a linked list where each index points to nums[i].
        - A duplicate number causes a cycle in this "linked list".
        - Use Floyd's Tortoise and Hare algorithm to detect the cycle and find its entrance.
        - The entrance to the cycle is the duplicate number.
    """
    slow = fast = nums[0]

    # Step 1: Detect intersection point in the cycle
    while True:
        slow = nums[slow]            # Move 1 step
        fast = nums[nums[fast]]      # Move 2 steps
        if slow == fast:
            break

    # Step 2: Find the entrance to the cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast

# Test Cases
def main():
    # Test - 1
    nums1 = [1, 3, 4, 2, 2]
    print("output-1:", findDuplicate(nums1))

    # Test - 2
    nums2 = [3, 1, 3, 4, 2]
    print("output-2:", findDuplicate(nums2))

    # Test - 3
    nums3 = [3, 3, 3, 3, 3]
    print("output-3:", findDuplicate(nums3))

if __name__ == "__main__":
    main()
