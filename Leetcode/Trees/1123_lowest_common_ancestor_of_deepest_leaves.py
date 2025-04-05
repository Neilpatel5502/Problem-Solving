# Problem Link: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# Time Complexity: O(n * d)     n = number of nodes, d = number of leaf nodes at deepest level
# Space Complexity: O(n)


from collections import deque
from TreeNode import list_to_tree, tree_to_list

def lcaDeepestLeaves(root):
    """
    Approach:
        - Perform a level-order traversal (BFS) of the tree to find all the nodes at the deepest level (leaf nodes).
        - If there's only one deepest leaf, return it directly as the LCA.
        - Otherwise, compute the Lowest Common Ancestor (LCA) for the deepest leaf nodes pairwise.
            - Start with the last two leaves and compute their LCA.
            - Then use this result with the next leaf to compute the new LCA, and so on.
            - At the end, the final node will be the LCA of all deepest leaves.
    """
    # Do trversal in level order and for the last level find LCA pairwise
    def find_leaves(root):
        nodes = []              # Will hold lists of nodes at each level
        queue = deque([root])   # Start BFS with the root

        while queue:
            queue_len = len(queue)
            level = []          # List to hold nodes of current level

            for i in range(queue_len):
                node = queue.popleft()

                if node:
                    level.append(node)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                nodes.append(level) # Add current level nodes to the result

        # Last element list of the level order traversal are the leaf nodes.
        return nodes[-1]

    # Function to compute Lower Common Ancestor of any two nodes in the Tree.
    def find_lca(root, p, q):
        if not root or root == p or root == q:
            return root

        # Recursion call on left subtree and right subtree consecutively.
        left = find_lca(root.left, p, q)
        right = find_lca(root.right, p, q)

        # If both gives result means cur node is the LCA
        if left and right:
            return root

        # Otherwise return left if left gives the value and vice versa.
        return left if left else right

    # Find leaves of the given tree.
    leaves = find_leaves(root)

    # If only one element in the leaf of last depth then LCA is node itself.
    if len(leaves) < 2:
        return leaves[0]

    # Pairwise compute LCA for the deepest leaves.
    q = leaves[-1]
    for i in range(len(leaves) - 2, -1, -1):
        p = leaves[i]
        q = find_lca(root, p, q)

    # Final result is the LCA of all deepest leaves
    return q

def main():
    # Test - 1
    list1 = [3,5,1,6,2,0,8,None,None,7,4]
    root1 = list_to_tree(list1)
    output1 = lcaDeepestLeaves(root1)
    print(f"output-1: {tree_to_list(output1)}")

    # Test - 2
    list2 = [1]
    root2 = list_to_tree(list2)
    output2 = lcaDeepestLeaves(root2)
    print(f"output-2: {tree_to_list(output2)}")

    # Test - 3
    list3 = [0,1,3,None,2]
    root3 = list_to_tree(list3)
    output3 = lcaDeepestLeaves(root3)
    print(f"output-3: {tree_to_list(output3)}")

if __name__ == "__main__":
    main()
