# Problem: https://leetcode.com/problems/path-sum

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (due to recursive call stack)

from TreeNode import list_to_tree

def hasPathSum(root, targetSum):
    """
    Approach:
        - Use DFS to traverse the tree from root to leaves.
        - At each node, keep track of the cumulative path sum.
        - When a leaf node is reached, check if the cumulative sum equals the targetSum.
        - Return True immediately if a valid path is found; otherwise check both subtrees.
    """
    if not root:
        return False

    def dfs(node, path):
        # Base case: if node is a leaf, check sum
        if not node.left and not node.right:
            return path + node.val == targetSum

        # Recursively check left and right subtrees
        left = dfs(node.left, path + node.val) if node.left else False
        right = dfs(node.right, path + node.val) if node.right else False

        return left or right

    return dfs(root, 0)


def main():
    # Test - 1: Valid path exists (5→4→11→2 sums to 22)
    root1 = list_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2])
    print(f"output-1: {hasPathSum(root1, 22)}")

    # Test - 2: No valid path exists
    root2 = list_to_tree([1, 2, 3])
    print(f"output-2: {hasPathSum(root2, 5)}")

    # Test - 3: Empty tree
    root3 = list_to_tree([])
    print(f"output-3: {hasPathSum(root3, 0)}")

if __name__ == "__main__":
    main()
