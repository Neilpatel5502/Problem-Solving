# Problem: https://leetcode.com/problems/average-of-levels-in-binary-tree

# Time Complexity: O(n)           # Each node is visited once
# Space Complexity: O(n)          # Space for queue in BFS traversal

from collections import deque
from TreeNode import list_to_tree

def averageOfLevels(root):
    """
    Approach:
        - Use Breadth-First Search (BFS) to traverse the binary tree level by level.
        - For each level, collect all node values into a list.
        - Calculate the average by dividing the sum of node values by the count.
        - Append each level's average to the output list.
    """
    out = []                            # Final output list of averages
    queue = deque([root])              # Queue for level-order traversal

    while queue:
        level = []                     # List to store values at the current level
        queue_len = len(queue)         # Number of nodes at this level

        for _ in range(queue_len):
            node = queue.popleft()

            if node:
                level.append(node.val) # Add current node's value
                queue.append(node.left)   # Add left child to queue
                queue.append(node.right)  # Add right child to queue

        if level:
            out.append(sum(level) / len(level))  # Compute average for current level

    return out


def main():
    # Test - 1
    root1 = list_to_tree([3,9,20,None,None,15,7])
    print(f"output-1: {averageOfLevels(root1)}")

    # Test - 2
    root2 = list_to_tree([3,9,20,15,7])
    print(f"output-2: {averageOfLevels(root2)}")

if __name__ == "__main__":
    main()
