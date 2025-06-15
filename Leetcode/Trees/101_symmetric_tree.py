# Problem: https://leetcode.com/problems/symmetric-tree

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (due to recursive call stack)

from TreeNode import list_to_tree

def isSymmetric(root):
    """
    Approach:
        - A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
        - Use a helper DFS function `dfs(p, q)` that compares nodes from both subtrees:
            * Check if both nodes are null → symmetric at this branch.
            * If one is null and the other is not → not symmetric.
            * Recursively compare outer pairs (p.left vs q.right) and inner pairs (p.right vs q.left).
        - Begin DFS with root.left and root.right.
    """
    # Edge case: if both left and right are None, it's symmetric
    if not root.left and not root.right:
        return True

    # Helper function to check mirror symmetry
    def dfs(p, q):
        if not p and not q:
            return True  # Both nodes are null
        if not p or not q:
            return False  # One node is null
        if p.val != q.val:
            return False  # Node values differ

        # Compare outer and inner pairs recursively
        return dfs(p.left, q.right) and dfs(p.right, q.left)

    # Start DFS comparison from left and right child of root
    return dfs(root.left, root.right)


def main():
    # Test 1
    root1 = list_to_tree([1, 2, 2, 3, 4, 4, 3])
    print(f"output-1: {isSymmetric(root1)}")

    # Test 2: Not symmetric
    root2 = list_to_tree([1, 2, 2, None, 3, None, 3])
    print(f"output-2: {isSymmetric(root2)}")

if __name__ == "__main__":
    main()
