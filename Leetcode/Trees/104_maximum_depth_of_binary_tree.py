# Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree

# Time Complexity: O(n) — where n is the number of nodes, as each node is visited once.
# Space Complexity: O(n) — for the stack used in depth-first traversal (worst case in unbalanced tree).

from TreeNode import list_to_tree

def maxDepth(root):
    """
    Approach:
        - Use an iterative DFS with a stack to track nodes and their corresponding depths.
        - Initialize the stack with the root node and depth 1.
        - As we pop each node, update the maximum depth encountered so far.
        - Push the left and right children of the node onto the stack with an incremented depth.
        - Finally, return the maximum depth found.
    """
    if root is None:
        return 0

    stack = [(root, 1)]  # Stack holds tuples of (node, current_depth)
    out = 0              # Variable to keep track of max depth

    while stack:
        node, depth = stack.pop()

        # Update the maximum depth encountered
        out = max(out, depth)

        # Push left child with incremented depth
        if node.left:
            stack.append((node.left, depth + 1))

        # Push right child with incremented depth
        if node.right:
            stack.append((node.right, depth + 1))

    return out


def main():
    # Test - 1
    root1 = list_to_tree([3, 9, 20, None, None, 15, 7])
    print(f"output-1: {maxDepth(root1)}")

    # Test - 2
    root2 = list_to_tree([1, None, 2])
    print(f"output-2: {maxDepth(root2)}")

if __name__ == "__main__":
    main()
