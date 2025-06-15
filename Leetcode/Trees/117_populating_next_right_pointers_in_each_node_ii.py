# Problem: Populate Next Right Pointers in Each Node
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque
from TreeNode import list_to_tree, tree_to_list

def connect(root):
    """
    Approach:
        - Use level order traversal with a queue.
        - At each level, link each node to its right neighbor using `.next`.
        - Enqueue the left and right children of each node for next level traversal.
    """
    if not root:
        return root

    queue = deque([root])

    while queue:
        level = []

        # Traverse all nodes at the current level
        for _ in range(len(queue)):
            node = queue.popleft()

            if node:
                level.append(node)
                queue.append(node.left)
                queue.append(node.right)

        # Link all nodes in the level from left to right
        for i in range(len(level) - 1):
            level[i].next = level[i + 1]

    return root


def main():
    # Test - 1: Perfect binary tree
    root1 = list_to_tree([1, 2, 3, 4, 5, 6, 7])
    output1 = connect(root1)
    print(f"output-1: {tree_to_list(output1)}")

    # Test - 2: Empty tree
    root2 = list_to_tree([])
    output2 = connect(root2)
    print(f"output-2: {tree_to_list(output2)}")

if __name__ == "__main__":
    main()
