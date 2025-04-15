# Problem: https://leetcode.com/problems/subtree-of-another-tree/
# Time Complexity: O(m * n) — where m = number of nodes in root, n = number of nodes in subRoot
# Space Complexity: O(h) — where h is the height of the root tree due to recursion stack

from TreeNode import list_to_tree

def isSubtree(root, subRoot):
    """
    Approach:
        - Traverse the main tree `root` node by node.
        - At each node, check if the subtree rooted at that node is the same as `subRoot` using isSameTree.
        - Use DFS to perform the traversal and check all subtrees.
        - If any match is found, return True. If none match, return False.
    """
    if not subRoot:
        return True  # An empty tree is always a subtree

    if not root:
        return False  # Non-empty subRoot can't be subtree of empty root

    if isSameTree(root, subRoot):
        return True

    # Recur on left and right subtree
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

# https://leetcode.com/problems/same-tree/
def isSameTree(p, q):
    """
    Helper Function:
        - Recursively checks if two binary trees are identical in structure and node values.
    """
    if p and q:
        return (
            p.val == q.val and
            isSameTree(p.left, q.left) and
            isSameTree(p.right, q.right)
        )
    return p is q


def main():
    # Test - 1: subRoot is a subtree of root
    root1 = list_to_tree([3, 4, 5, 1, 2])
    sub1 = list_to_tree([4, 1, 2])
    print(f"output-1: {isSubtree(root1, sub1)}")

    # Test - 2: subRoot is not a subtree (structure mismatch)
    root2 = list_to_tree([3, 4, 5, 1, 2, None, None, 0])
    sub2 = list_to_tree([4, 1, 2])
    print(f"output-2: {isSubtree(root2, sub2)}")

if __name__ == "__main__":
    main()
