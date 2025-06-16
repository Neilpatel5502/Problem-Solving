# Problem: https://leetcode.com/problems/minimum-absolute-difference-in-bst

# Time Complexity: O(n)           # In-order traversal of all n nodes
# Space Complexity: O(n)          # Storing node values in a list

from TreeNode import list_to_tree

def getMinimumDifference(root):
    """
    Approach:
        - Perform in-order traversal on the BST to get values in sorted order.
        - Store all node values during traversal into a list.
        - Then iterate through the list and compute the minimum difference
          between consecutive values.
        - Since it's a BST, the smallest difference will be between two adjacent values in sorted order.
    """
    node_lst = []                        # To store in-order values

    def inorder(node):
        if node:
            inorder(node.left)          # Visit left subtree
            node_lst.append(node.val)   # Visit current node
            inorder(node.right)         # Visit right subtree

    inorder(root)

    out = float('inf')
    for i in range(len(node_lst) - 1):
        out = min(out, abs(node_lst[i] - node_lst[i + 1]))  # Track minimum diff

    return out


def main():
    # Test - 1
    root1 = list_to_tree([4, 2, 6, 1, 3])
    print(f"output-1: {getMinimumDifference(root1)}")

    # Test - 2
    root2 = list_to_tree([1, 0, 48, None, None, 12, 49])
    print(f"output-2: {getMinimumDifference(root2)}")

if __name__ == "__main__":
    main()
