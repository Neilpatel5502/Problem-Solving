# Problem: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Time Complexity: O(n^2) — due to list slicing and searching index at each recursive call
# Space Complexity: O(n) — due to recursion stack and storing tree nodes

from TreeNode import TreeNode, tree_to_list

def buildTree(inorder, postorder):
    """
    Approach:
        - The first element of preorder traversal is always the root of the current subtree.
        - Find the root's index in inorder traversal to separate left and right subtrees.
        - Recursively build left and right subtrees using the partitioned preorder and inorder arrays.
        - Return the constructed root node.
    """
    if not postorder or not inorder:
        return None  # Base case: no tree to build

    # Root is the first element in preorder
    root = TreeNode(postorder[-1])
    mid = inorder.index(postorder[-1])  # Find root index in inorder

    # Recursively build left and right subtrees
    root.left = buildTree(inorder[:mid], postorder[:mid])
    root.right = buildTree(inorder[mid+1:], postorder[mid:len(postorder) - 1])

    return root


def main():
    # Test - 1
    inorder1 = [9, 3, 15, 20, 7]
    postorder1 = [9, 15, 7, 20, 3]
    root1 = buildTree(inorder1, postorder1)
    print(f"output-1: {tree_to_list(root1)}")

    # Test - 2
    inorder2 = [-1]
    postorder2 = [-1]
    root2 = buildTree(inorder2, postorder2)
    print(f"output-2: {tree_to_list(root2)}")

if __name__ == "__main__":
    main()
