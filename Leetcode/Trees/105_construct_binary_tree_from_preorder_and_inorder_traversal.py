# Problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Time Complexity: O(n^2) — due to list slicing and searching index at each recursive call
# Space Complexity: O(n) — due to recursion stack and storing tree nodes

from TreeNode import TreeNode, tree_to_list

def buildTree(preorder, inorder):
    """
    Approach:
        - The first element of preorder traversal is always the root of the current subtree.
        - Find the root's index in inorder traversal to separate left and right subtrees.
        - Recursively build left and right subtrees using the partitioned preorder and inorder arrays.
        - Return the constructed root node.
    """
    if not preorder or not inorder:
        return None  # Base case: no tree to build

    # Root is the first element in preorder
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])  # Find root index in inorder

    # Recursively build left and right subtrees
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])

    return root


def main():
    # Test - 1
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    root1 = buildTree(preorder1, inorder1)
    print(f"output-1: {tree_to_list(root1)}")

    # Test - 2
    preorder2 = [-1]
    inorder2 = [-1]
    root2 = buildTree(preorder2, inorder2)
    print(f"output-2: {tree_to_list(root2)}")

if __name__ == "__main__":
    main()
