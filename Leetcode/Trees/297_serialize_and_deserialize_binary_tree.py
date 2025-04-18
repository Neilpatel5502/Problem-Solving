# Problem: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Time Complexity:
#   - serialize: O(n) — where n is the number of nodes in the tree
#   - deserialize: O(n)
# Space Complexity: O(n) — for the output string and recursion stack

from TreeNode import TreeNode, list_to_tree, tree_to_list

class Codec:
    def serialize(self, root):
        """
        Approach:
            - Use pre-order DFS to serialize the tree into a comma-separated string.
            - Represent None nodes with a special marker (e.g., 'N').
            - This preserves both structure and values.
        """
        out = []

        def dfs(node):
            if not node:
                out.append("N")  # Null marker
                return
            out.append(str(node.val))  # Append node value
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(out)

    def deserialize(self, data):
        """
        Approach:
            - Use DFS to read values from the serialized string.
            - Create nodes recursively following the order in the string.
            - 'N' represents a None node.
        """
        values = data.split(",")
        self.i = 0  # Pointer to current index in values

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


def main():
    codec = Codec()

    # Test - 1
    root1 = list_to_tree([1, 2, 3, None, None, 4, 5])
    data1 = codec.serialize(root1)
    result1 = codec.deserialize(data1)
    print(f"output-1: {tree_to_list(result1)}")

    # Test - 2
    root2 = list_to_tree([])
    data2 = codec.serialize(root2)
    result2 = codec.deserialize(data2)
    print(f"output-2: {tree_to_list(result2)}")

if __name__ == "__main__":
    main()
