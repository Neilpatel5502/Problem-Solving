# Problem: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Time Complexity: O(n), where n is the number of elements in the array
# Space Complexity: O(log n) due to recursion stack depth in balanced tree

from TreeNode import TreeNode, tree_to_list

def sortedArrayToBST(nums):
    """
    Approach:
        - Use Divide and Conquer to convert the sorted array into a height-balanced BST.
        - Select the middle element as the root to ensure balance.
        - Recursively apply the same logic to the left and right subarrays to build left and right subtrees.
        - Base case: if start > end, return None (no node).
    """

    def dfs(start, end):
        if start > end:
            return None

        # Middle element as root
        mid = (start + end) // 2
        root = TreeNode(nums[mid])

        # Recursively build left and right subtrees
        root.left = dfs(start, mid - 1)
        root.right = dfs(mid + 1, end)

        return root

    return dfs(0, len(nums) - 1)


def main():
    # Test - 1
    nums1 = [-10, -3, 0, 5, 9]
    root1 = sortedArrayToBST(nums1)
    print(f"output-1: {tree_to_list(root1)}")

    # Test - 2
    nums2 = [1, 3]
    root2 = sortedArrayToBST(nums2)
    print(f"output-2: {tree_to_list(root2)}")

if __name__ == "__main__":
    main()
