# Problem: https://leetcode.com/problems/binary-search-tree-iterator

# Time Complexity:
#   - `next()`: Amortized O(1) per call (O(h) worst-case for a single call)
#   - `hasNext()`: O(1)
# Space Complexity: O(h), where h is the height of the BST (stack stores leftmost path)

from TreeNode import list_to_tree

class BSTIterator:
    """
    Approach:
        - This iterator simulates an in-order traversal of the BST.
        - During initialization, push all left descendants of the root onto a stack.
        - `next()` pops the top node, pushes all left descendants of its right child.
        - `hasNext()` checks if any nodes remain in the stack.
    """

    def __init__(self, root):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        # Get next smallest value
        node = self.stack.pop()

        # If node has a right child, process its leftmost path
        cur = node.right
        while cur:
            self.stack.append(cur)
            cur = cur.left

        return node.val

    def hasNext(self):
        # Return True if there are still nodes left
        return len(self.stack) > 0


def main():
    # Test - 1: Balanced BST
    root1 = list_to_tree([7, 3, 15, None, None, 9, 20])
    it1 = BSTIterator(root1)
    print("output-1:", end=" ")
    while it1.hasNext():
        print(it1.next(), end=" ")
    print()

if __name__ == "__main__":
    main()
