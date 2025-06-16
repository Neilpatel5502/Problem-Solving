# Problem: https://leetcode.com/problems/validate-binary-search-tree

# Time Complexity: O(n)           # Each node is visited once in in-order traversal
# Space Complexity: O(n)          # Stack and output list can grow up to n nodes

from TreeNode import list_to_tree

def isValidBST(root):
    """
    Approach:
        - Use iterative in-order traversal to traverse the tree.
        - In a valid BST, in-order traversal should yield strictly increasing values.
        - Maintain a list `out` to store visited node values.
        - If the current node's value is less than or equal to the last stored value, return False.
        - If traversal completes without issue, the tree is a valid BST.
    """
    stack = []                   # Stack for iterative in-order traversal
    out = []                     # List to hold visited values for validation
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)    # Traverse left subtree
            cur = cur.left

        cur = stack.pop()        # Visit node
        if out and cur.val <= out[-1]:
            return False         # Not strictly increasing → not a valid BST

        out.append(cur.val)
        cur = cur.right          # Traverse right subtree

    return True


def main():
    # Test - 1
    root1 = list_to_tree([2, 1, 3])
    print(f"output-1: {isValidBST(root1)}")

    # Test - 2
    root2 = list_to_tree([5, 1, 4, None, None, 3, 6])
    print(f"output-2: {isValidBST(root2)}")

    # Test - 3
    root3 = list_to_tree([2, 2, 2])
    print(f"output-2: {isValidBST(root3)}")

if __name__ == "__main__":
    main()
