# Problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Time Complexity: O(n) — where n is the number of nodes in the tree
# Space Complexity: O(h) — where h is the height of the tree due to recursion stack

from TreeNode import list_to_tree

def goodNodes(root):
    """
    Approach:
        - Perform DFS traversal from the root, keeping track of the maximum value seen so far along the path.
        - A node is considered 'good' if its value is greater than or equal to the maximum value encountered before it.
        - Recursively count good nodes in the left and right subtrees, updating the max value.
        - Return the total number of good nodes.
    """
    def dfs(node, max_value):
        if not node:
            return 0  # Base case: no node contributes 0

        out = 1 if node.val >= max_value else 0  # Check if current node is good

        # Update the max_value for children
        max_value = max(max_value, node.val)

        # Continue DFS on left and right children
        out += dfs(node.left, max_value)
        out += dfs(node.right, max_value)

        return out

    return dfs(root, root.val)


def main():
    # Test - 1
    root1 = list_to_tree([3, 1, 4, 3, None, 1, 5])
    print(f"output-1: {goodNodes(root1)}")

    # Test - 2
    root2 = list_to_tree([3, 3, None, 4, 2])
    print(f"output-2: {goodNodes(root2)}")

    # Test - 3
    root3 = list_to_tree([1])
    print(f"output-3: {goodNodes(root3)}")

if __name__ == "__main__":
    main()
