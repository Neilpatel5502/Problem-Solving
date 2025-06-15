# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (recursive stack)

from TreeNode import list_to_tree

def lowestCommonAncestor(root, p, q):
    """
    Approach:
        - Use postorder DFS traversal to search for nodes p and q in the tree.
        - If current node is None or equal to p or q, return it.
        - Recurse on left and right subtrees.
        - If both left and right recursive calls return non-null values, current node is the LCA.
        - If only one returns non-null, that means both p and q are located in one subtree.
    """

    # If it give any of the p or q return it.
    if not root or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root  # This is the LCA

    return left if left else right


def main():
    # Test - 1:
    root1 = list_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p1 = root1.left              # Node 5
    q1 = root1.right             # Node 1
    print(f"output-1: {lowestCommonAncestor(root1, p1, q1).val}")

    # Test - 2:
    root2 = list_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p2 = root2.left                         # Node 5
    q2 = root2.left.right.right             # Node 4
    print(f"output-2: {lowestCommonAncestor(root2, p2, q2).val}")

    # Test - 3:
    root3 = list_to_tree([1, 2])
    p3 = root3
    q3 = root3.left
    print(f"output-3: {lowestCommonAncestor(root3, p3, q3).val}")

if __name__ == "__main__":
    main()
