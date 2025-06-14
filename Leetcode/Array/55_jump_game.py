# Problem: https://leetcode.com/problems/jump-game

# Time Complexity: O(n)              # Single pass from end to start
# Space Complexity: O(1)             # No extra space used

def canJump(nums):
    """
    Approach:
        - Start from the last index and work backwards.
        - Maintain a `goal` index we need to reach or surpass.
        - For each index `i` from right to left:
            - If i + nums[i] >= goal, then we can jump from i to the goal (or beyond).
            - In that case, update goal = i (we now need to reach i instead).
        - At the end, if goal == 0, then the start index can reach the end.
    """
    goal = len(nums) - 1  # Start with the last index as the goal

    # Traverse backwards through the list
    for i in range(len(nums) - 1, -1, -1):
        # Check if we can jump from i to current goal
        if i + nums[i] >= goal:
            goal = i  # Update goal to this new reachable position

    # If we have reached the beginning, return True
    return goal == 0


def main():
    # Test - 1
    nums1 = [2,3,1,1,4]
    print(f"output-1: {canJump(nums1)}")

    # Test - 2
    nums2 = [3,2,1,0,4]
    print(f"output-2: {canJump(nums2)}")

if __name__ == "__main__":
    main()
