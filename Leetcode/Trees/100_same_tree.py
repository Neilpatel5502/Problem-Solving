# Problem: https://leetcode.com/problems/same-tree

# Time Complexity: O(n) — where n is the number of nodes in the smaller of the two trees
# Space Complexity: O(h) — where h is the height of the tree due to recursion stack

from TreeNode import list_to_tree

def isSameTree(p, q):
    """
    Approach:
        - Recursively compare both trees node by node.
        - At each step:
            1. If both nodes are not None, check their values and recurse on left and right subtrees.
            2. If either node is None, check if both are None (valid), else return False.
        - Return True only if all corresponding nodes in both trees match in structure and value.
    """
    if p and q:
        # Compare values and check left & right subtree
        return (
            p.val == q.val and
            isSameTree(p.left, q.left) and
            isSameTree(p.right, q.right)
        )
    return p is q  # Both must be None to be considered same


def main():
    # Test - 1: Identical trees
    tree1 = list_to_tree([1, 2, 3])
    tree2 = list_to_tree([1, 2, 3])
    print(f"output-1: {isSameTree(tree1, tree2)}")

    # Test - 2: Different structure
    tree3 = list_to_tree([1, 2])
    tree4 = list_to_tree([1, None, 2])
    print(f"output-2: {isSameTree(tree3, tree4)}")

    # Test - 3: Different values
    tree5 = list_to_tree([1, 2, 1])
    tree6 = list_to_tree([1, 1, 2])
    print(f"output-3: {isSameTree(tree5, tree6)}")

if __name__ == "__main__":
    main()
