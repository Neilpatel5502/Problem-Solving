# Problem: https://leetcode.com/problems/balanced-binary-tree/
# Time Complexity: O(n) — where n is the number of nodes in the tree
# Space Complexity: O(h) — where h is the height of the tree due to recursion stack

from TreeNode import list_to_tree

def isBalanced(root):
    """
    Approach:
        - Use a DFS (post-order traversal) to check whether each subtree is balanced.
        - At each node, recursively check:
            1. If left and right subtrees are balanced.
            2. The height of left and right subtrees.
        - A node is balanced if:
            - Both left and right subtrees are balanced
            - The height difference between left and right is not more than 1
        - Return a tuple: [isBalanced, height] for each subtree.
    """
    def dfs(root):
        if not root:
            return [True, 0]  # Base case: balanced and height 0

        left = dfs(root.left)
        right = dfs(root.right)

        # A tree is balanced if left and right are balanced and height difference ≤ 1
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        # Height is max of left and right subtree heights plus 1 for current node
        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]


def main():
    # Test - 1: Balanced binary tree
    root1 = list_to_tree([3, 9, 20, None, None, 15, 7])
    print(f"output-1: {isBalanced(root1)}")

    # Test - 2: Unbalanced binary tree
    root2 = list_to_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    print(f"output-2: {isBalanced(root2)}")

    # Test - 3: Empty tree (balanced)
    root3 = list_to_tree([])
    print(f"output-3: {isBalanced(root3)}")
if __name__ == "__main__":
    main()
