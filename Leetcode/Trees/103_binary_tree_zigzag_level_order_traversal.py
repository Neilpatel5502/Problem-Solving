# Problem: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Time Complexity: O(n)           # Each node is visited once
# Space Complexity: O(n)          # Space for queue and output list

from collections import deque
from TreeNode import list_to_tree

def zigzagLevelOrder(root):
    """
    Approach:
        - Use Breadth-First Search (BFS) to traverse the tree level by level.
        - Keep a counter to track the current level's parity (even or odd).
        - Append the values of each level to the result list.
        - If the level is odd, reverse the level values before appending.
        - Continue this alternation to achieve zigzag order.
    """
    out = []                            # Final output list
    queue = deque([root])              # Queue for level-order traversal
    count = 0                          # To alternate the direction

    while queue:
        queue_len = len(queue)         # Number of nodes at this level
        level = []                     # List to store current level values

        for _ in range(queue_len):
            node = queue.popleft()
            if node:
                level.append(node.val)     # Add current node's value
                queue.append(node.left)    # Add left child
                queue.append(node.right)   # Add right child

        if level:
            if count % 2 == 0:
                out.append(level)          # Append normally on even levels
            else:
                out.append(level[::-1])    # Reverse on odd levels

        count += 1                         # Increment level counter

    return out


def main():
    # Test - 1
    root1 = list_to_tree([3,9,20,None,None,15,7])
    print(f"output-1: {zigzagLevelOrder(root1)}")

    # Test - 2
    root2 = list_to_tree([1])
    print(f"output-2: {zigzagLevelOrder(root2)}")

    # Test - 3
    root3 = list_to_tree([])
    print(f"output-3: {zigzagLevelOrder(root3)}")

if __name__ == "__main__":
    main()
