# Problem: https://leetcode.com/problems/validate-binary-search-tree/
# Time Complexity: O(n) — where n is the number of nodes in the tree
# Space Complexity: O(h) — where h is the height of the tree due to recursion stack

from TreeNode import list_to_tree

def isValidBST(root):
    """
    Approach:
        - Use DFS to recursively validate that each node's value lies within a valid range.
        - Initially, the range is (-inf, inf).
        - For left child: update upper bound to parent node's value.
        - For right child: update lower bound to parent node's value.
        - If any node violates the rule, return False.
    """
    def dfs(node, min_value, max_value):
        if not node:
            return True  # Base case: empty nodes are valid

        # The current node's value must be within (min_value, max_value)
        if node.val <= min_value or node.val >= max_value:
            return False

        # Check left and right subtrees recursively
        return dfs(node.left, min_value, node.val) and dfs(node.right, node.val, max_value)

    return dfs(root, float("-inf"), float("inf"))


def main():
    # Test - 1: Valid BST
    root1 = list_to_tree([2, 1, 3])
    print(f"output-1: {isValidBST(root1)}")

    # Test - 2: Invalid BST
    root2 = list_to_tree([5, 1, 4, None, None, 3, 6])
    print(f"output-2: {isValidBST(root2)}")

if __name__ == "__main__":
    main()
