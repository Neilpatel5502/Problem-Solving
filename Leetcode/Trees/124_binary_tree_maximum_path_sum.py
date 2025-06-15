# Problem: https://leetcode.com/problems/binary-tree-maximum-path-sum

# Time Complexity: O(n) — where n is the number of nodes in the tree
# Space Complexity: O(h) — where h is the height of the tree due to recursion stack

from TreeNode import list_to_tree

def maxPathSum(root):
    """
    Approach:
        - Perform DFS traversal to calculate the maximum gain from each node.
        - At each node:
            - Compute the maximum path sum from the left child and right child.
            - If any path sum is negative, treat it as 0 (ignore that path).
            - Update the global maximum path sum (`out`) by considering the path through the current node and both its left and right subtrees.
            - Return the maximum gain to the parent node (only one side: either left or right).
    """
    out = root.val  # Initialize the maximum path sum with root's value

    def dfs(node):
        nonlocal out

        if not node:
            return 0  # Base case: no contribution from null nodes

        left_maximum = dfs(node.left)
        right_maximum = dfs(node.right)

        # If maximum is negative, take 0 (do not include that path)
        left_maximum = max(left_maximum, 0)
        right_maximum = max(right_maximum, 0)

        # Update the maximum path sum considering current node as root
        out = max(out, node.val + left_maximum + right_maximum)

        # Return max gain if we continue the path upwards (only one side can be chosen)
        return node.val + max(left_maximum, right_maximum)

    dfs(root)

    return out


def main():
    # Test - 1
    root1 = list_to_tree([1, 2, 3])
    print(f"output-1: {maxPathSum(root1)}")

    # Test - 2
    root2 = list_to_tree([-10, 9, 20, None, None, 15, 7])
    print(f"output-2: {maxPathSum(root2)}")

if __name__ == "__main__":
    main()
