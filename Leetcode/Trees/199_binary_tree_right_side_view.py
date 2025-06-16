# Problem: https://leetcode.com/problems/binary-tree-right-side-view

# Time Complexity: O(n) — where n is the number of nodes in the tree
# Space Complexity: O(n) — for the queue used in level-order traversal

from collections import deque
from TreeNode import list_to_tree

def rightSideView(root):
    """
    Approach:
        - Perform level-order traversal using a queue.
        - At each level, add the value of the rightmost node (i.e., the last node in that level's queue).
        - Continue until all levels are processed.
    """
    if not root:
        return []

    out = []
    queue = deque([root])  # Start BFS with root node

    while queue:
        out.append(queue[-1].val)  # Rightmost node at current level
        queue_len = len(queue)

        for _ in range(queue_len):
            node = queue.popleft()

            # Add children in left-to-right order
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return out


def main():
    # Test - 1
    root1 = list_to_tree([1, 2, 3, None, 5, None, 4])
    print(f"output-1: {rightSideView(root1)}")

    # Test - 2
    root2 = list_to_tree([1, 2, 3, 4, None, None, None, 5])
    print(f"output-2: {rightSideView(root2)}")

    # Test - 3
    root3 = list_to_tree([1, None, 3])
    print(f"output-3: {rightSideView(root3)}")

    # Test - 4
    root4 = list_to_tree([])
    print(f"output-4: {rightSideView(root4)}")

if __name__ == "__main__":
    main()
