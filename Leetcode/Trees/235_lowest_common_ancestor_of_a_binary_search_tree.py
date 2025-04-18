# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Time Complexity: O(h) — where h is the height of the BST
# Space Complexity: O(1) — since we're using iterative approach without recursion

from TreeNode import TreeNode, list_to_tree

def lowestCommonAncestor(root, p, q):
    """
    Approach:
        - Start from the root node and traverse the tree.
        - If both p and q are greater than the current node, the LCA must be in the right subtree.
        - If both are less, move to the left subtree.
        - Otherwise, current node is the split point and hence the LCA.
    """
    cur = root

    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right  # Move right if both are greater
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left  # Move left if both are smaller
        else:
            return cur  # Current node is LCA

    return None  # Just for completeness, this line should not be hit in valid BST


def main():
    # Helper function to find node reference by value
    def find_node(root, val):
        if not root:
            return None
        if root.val == val:
            return root
        return find_node(root.left, val) or find_node(root.right, val)

    # Test - 1
    root1 = list_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p1 = TreeNode(2)
    q1 = TreeNode(8)
    print(f"output-1:", lowestCommonAncestor(root1, p1, q1).val)

    # Test - 2
    root2 = list_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p2 = TreeNode(2)
    q2 = TreeNode(4)
    print(f"output-2:", lowestCommonAncestor(root2, p2, q2).val)

    # Test - 3
    root3 = list_to_tree([2, 1])
    p3 = TreeNode(2)
    q3 = TreeNode(1)
    print(f"output-3:", lowestCommonAncestor(root3, p3, q3).val)

if __name__ == "__main__":
    main()
