# Problem: https://leetcode.com/problems/invert-binary-tree/
# Time Complexity: O(n) — where n is the number of nodes in the tree, as each node is visited once.
# Space Complexity: O(n) — for the stack in the worst case (completely unbalanced tree).

from TreeNode import list_to_tree, tree_to_list

def invertTree(root):
    """
    Approach:
        - Use an iterative approach with a stack (Depth First Search).
        - For every node visited, swap its left and right children.
        - Push the non-null children onto the stack to process them in future iterations.
        - Once all nodes are processed and their children swapped, return the root of the inverted tree.
    """

    if root is None:
        return None

    stack = [root]  # Initialize stack with root node

    while stack:
        node = stack.pop()  # Pop the top node

        # Swap the left and right children of the current node
        node.right, node.left = node.left, node.right

        # Push right child to stack if it exists
        if node.right:
            stack.append(node.right)

        # Push left child to stack if it exists
        if node.left:
            stack.append(node.left)

    return root


def main():
    # Test - 1
    root1 = list_to_tree([4, 2, 7, 1, 3, 6, 9])
    inverted1 = invertTree(root1)
    print(f"output-1: {tree_to_list(inverted1)}")

    # Test - 2
    root2 = list_to_tree([2, 1, 3])
    inverted2 = invertTree(root2)
    print(f"output-2: {tree_to_list(inverted2)}")

    # Test - 3
    root3 = list_to_tree([])
    inverted3 = invertTree(root3)
    print(f"output-3: {tree_to_list(inverted3)}")

if __name__ == "__main__":
    main()
