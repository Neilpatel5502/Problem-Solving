# Problem: https://leetcode.com/problems/sum-root-to-leaf-numbers

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (due to recursion stack)

from TreeNode import list_to_tree

def sumNumbers(root):
    """
    Approach:
        - Use DFS to traverse from root to all leaf nodes.
        - For each path, build the number as a string by appending node values.
        - At a leaf node, convert the accumulated string to an integer and add it to the total sum.
        - Use a nonlocal variable `out` to store the cumulative result.
    """
    out = 0

    def dfs(node, path):
        nonlocal out

        # If it's a leaf node, finalize the number and add it
        if not node.left and not node.right:
            path += str(node.val)
            out += int(path)
            return

        # Recurse left and right with updated path
        if node.left:
            dfs(node.left, path + str(node.val))
        if node.right:
            dfs(node.right, path + str(node.val))

    dfs(root, "")

    return out


def main():
    # Test - 1:
    root1 = list_to_tree([1, 2, 3])
    print(f"output-1: {sumNumbers(root1)}")

    # Test - 2:
    root2 = list_to_tree([4, 9, 0, 5, 1])
    print(f"output-2: {sumNumbers(root2)}")

if __name__ == "__main__":
    main()
