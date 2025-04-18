# Problem: https://leetcode.com/problems/diameter-of-binary-tree/
# Time Complexity: O(n) — where n is the number of nodes in the tree
# Space Complexity: O(h) — where h is the height of the tree due to recursion stack

from TreeNode import list_to_tree

def diameterOfBinaryTree(root):
    """
    Approach:
        - Perform DFS traversal on each node to calculate the depth of its left and right subtrees.
        - At each node, update the global diameter as the sum of left and right depths.
        - Return the maximum diameter found during traversal.
    """
    out = 0  # To keep track of the maximum diameter

    def dfs(root):
        nonlocal out

        if root is None:
            return 0  # Base case: null node contributes 0 to the depth

        left = dfs(root.left)    # Recursively find left subtree depth
        right = dfs(root.right)  # Recursively find right subtree depth

        out = max(out, left + right)  # Update diameter at this node

        return 1 + max(left, right)   # Return depth of current subtree

    dfs(root)
    return out


def main():
    # Test - 1
    root1 = list_to_tree([1, 2, 3, 4, 5])
    print(f"output-1:", diameterOfBinaryTree(root1))

    # Test - 2
    root2 = list_to_tree([1, 2])
    print(f"output-2:", diameterOfBinaryTree(root2))

if __name__ == "__main__":
    main()
