# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Time Complexity: O(h + k) — where h is the height of the tree (for reaching the leftmost node) and k is the number of pops
# Space Complexity: O(h) — due to the stack storing nodes on the path

from TreeNode import list_to_tree

def kthSmallest(root, k):
    """
    Approach:
        - Perform an in-order traversal (L -> D -> R) of the BST.
        - In-order traversal of a BST yields nodes in sorted order.
        - Traverse until the kth node is popped from the stack and return its value.
    """
    stack = []
    cur = root

    while cur or stack:
        # Go to the leftmost node
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        k -= 1

        if k == 0:
            return cur.val  # Found kth smallest element

        cur = cur.right  # Move to right subtree

    return -1  # Should not reach here if k is valid


def main():
    # Test - 1
    root1 = list_to_tree([3, 1, 4, None, 2])
    k1 = 1
    print(f"output-1: {kthSmallest(root1, k1)}")

    # Test - 2
    root2 = list_to_tree([5, 3, 6, 2, 4, None, None, 1])
    k2 = 3
    print(f"output-2: {kthSmallest(root2, k2)}")

if __name__ == "__main__":
    main()
