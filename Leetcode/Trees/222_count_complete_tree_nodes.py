# Problem: Count Complete Tree Nodes
# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (stack depth)

from TreeNode import list_to_tree

def countNodes(root):
    """
    Approach:
        - Use iterative DFS (with a stack) to traverse the entire tree.
        - Increment a counter for each visited node.
        - Push left and right children (if any) to the stack for further traversal.
    """
    if root is None:
        return 0

    count = 0
    stack = [root]

    while stack:
        node = stack.pop()
        count += 1  # Count current node

        # Add left and right children to stack if they exist
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return count


def main():
    # Test - 1:
    root1 = list_to_tree([1, 2, 3, 4, 5, 6])
    print(f"output-1: {countNodes(root1)}")

    # Test - 2:
    root2 = list_to_tree([])
    print(f"output-2: {countNodes(root2)}")

    # Test - 3:
    root3 = list_to_tree([1])
    print(f"output-3: {countNodes(root3)}")

if __name__ == "__main__":
    main()
