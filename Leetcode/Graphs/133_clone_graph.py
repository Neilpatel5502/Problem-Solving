# Problem: https://leetcode.com/problems/clone-graph

# Time Complexity: O(n)           # Each node and its neighbors are visited once
# Space Complexity: O(n)          # Hash map and recursion stack for n nodes

from Node import Node, build_graph, graph_to_list

def cloneGraph(node):
    """
    Approach:
        - Use DFS to traverse the undirected graph starting from the given node.
        - Use a hash map `graph` to keep track of already copied nodes.
        - For each node, if it's already cloned, return it from the map to avoid re-processing.
        - Otherwise, create a copy, store it in the map, and recursively clone all neighbors.
        - Return the deep-cloned graph starting from the given node.
    """
    if not node:
        return node

    graph = {}  # Map original node -> cloned node

    def dfs(node):
        if node in graph:
            return graph[node]  # Return already cloned node

        copy_node = Node(node.val)     # Clone the node
        graph[node] = copy_node        # Store in map

        for nei in node.neighbors:
            copy_node.neighbors.append(dfs(nei))  # Recursively clone neighbors

        return copy_node

    return dfs(node)


def main():
    # Test - 1
    node1 = build_graph([[2,4],[1,3],[2,4],[1,3]])
    cloned1 = cloneGraph(node1)
    print(f"output-1: {graph_to_list(cloned1)}")

    # Test - 2
    node2 = build_graph([[]])
    cloned2 = cloneGraph(node2)
    print(f"output-2: {graph_to_list(cloned2)}")

    # Test - 3
    node3 = build_graph([])
    cloned3 = cloneGraph(node3)
    print(f"output-3: {graph_to_list(cloned3)}")

if __name__ == "__main__":
    main()
