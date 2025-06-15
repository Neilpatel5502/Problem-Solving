# Problem: https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(n), for the explicit stack used in DFS

from TreeNode import list_to_tree, tree_to_list

def flatten(root):
    """
    Approach:
        - Use a stack to perform pre-order traversal (node → left → right).
        - At each step, connect the current node's right pointer to the next node in the preorder traversal.
        - Set left pointer of each node to None to create a linked-list-like structure.
        - Stack ensures we explore left subtree before right, preserving preorder structure.
    """
    if not root:
        return

    stack = [root]  # Start with the root node

    while stack:
        node = stack.pop()

        # Push right and left children to stack (right first so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        # Update current node's right pointer to next node in stack (preorder)
        if stack:
            node.right = stack[-1]

        node.left = None  # Set left to None to form linked list


def main():
    # Test - 1:
    root1 = list_to_tree([1, 2, 5, 3, 4, None, 6])
    flatten(root1)
    print(f"output-1: {tree_to_list(root1)}")

    # Test - 2:
    root2 = list_to_tree([])
    flatten(root2)
    print(f"output-2: {tree_to_list(root2)}")

    # Test - 3:
    root3 = list_to_tree([0])
    flatten(root3)
    print(f"output-3: {tree_to_list(root3)}")

if __name__ == "__main__":
    main()
