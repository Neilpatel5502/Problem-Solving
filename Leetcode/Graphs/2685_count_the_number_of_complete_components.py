# Problem Link: https://leetcode.com/problems/count-the-number-of-complete-components

# Time Complexity: O(V + E)         V = Number of vertices, E = number of edges
# Space Complexity: O(V + E)

from collections import defaultdict

def countCompleteComponents(n, edges):
    """
    Approach:
        - Construct an adjacency list to represent the graph.
        - Use DFS to explore connected components.
        - For each connected component found:
        - Check if it's a complete graph by verifying that each node in the component
            has edges to all other nodes in that component.
        - Count and return the number of complete connected components.
    """

    # Normal DFS function to traverse through connected graph
    def dfs(node, out):
        if node in visit:
            return

        visit.add(node)
        out.append(node)

        for nei in adj[node]:
            dfs(nei, out)

        return out

    # Step 1: Build adjacency list representation of the graph
    adj = defaultdict(list)
    for v1, v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)

    out = 0
    visit = set()

    # Step 2: Find connected components using DFS
    for v in range(n):
        if v in visit:
            continue

        component = dfs(v, [])

        # Step 3: Check if the component forms a complete graph
        if all([len(component) - 1 == len(adj[v2]) for v2 in component]):
            out += 1

    return out


def main():
    # Test - 1
    n1 = 6
    edges1 = [[0,1],[0,2],[1,2],[3,4]]
    print(f"output-1: {countCompleteComponents(n1, edges1)}")

    # Test - 2
    n2 = 6
    edges2 = [[0,1],[0,2],[1,2],[3,4],[3,5]]
    print(f"output-2: {countCompleteComponents(n2, edges2)}")


if __name__ == "__main__":
    main()
