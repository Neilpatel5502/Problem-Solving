# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Time Complexity: O(n) — where n is the number of nodes in the tree
# Space Complexity: O(n) — for the queue used in BFS traversal

from collections import deque
from TreeNode import list_to_tree

def levelOrder(root):
    """
    Approach:
        - Use Breadth-First Search (BFS) with a queue to traverse the tree level by level.
        - At each level, process all nodes currently in the queue.
        - For each node, add its value to the current level list, and enqueue its children.
        - Append the level list to the result after each level is processed.
    """
    out = []
    queue = deque([root])  # Initialize queue with root node

    while queue:
        queue_len = len(queue)
        level = []  # List to store current level nodes

        for _ in range(queue_len):
            node = queue.popleft()

            if node:
                level.append(node.val)  # Add node value to current level
                queue.append(node.left)  # Add left child to queue
                queue.append(node.right)  # Add right child to queue

        if level:
            out.append(level)  # Append non-empty level to output

    return out


def main():
    # Test - 1
    root1 = list_to_tree([3, 9, 20, None, None, 15, 7])
    print(f"output-1: {levelOrder(root1)}")

    # Test - 2
    root2 = list_to_tree([1])
    print(f"output-2: {levelOrder(root2)}")

    # Test - 3
    root3 = list_to_tree([])
    print(f"output-3: {levelOrder(root3)}")

if __name__ == "__main__":
    main()
