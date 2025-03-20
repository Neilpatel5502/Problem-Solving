# Problem Link: https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph

# Time Complexity: O(V + E + Q)     V = vertices, E = edges, Q = queries
# Space Complexity: O(V + Q)        V for component_cost dict and Q for output


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))    # Initialize parent array where each node is its own parent
        self.size = [1] * n             # Size array to track the size of each set (for union by size optimization)

    def find(self, x):
        # Path compression: Makes future queries faster by pointing nodes directly to root
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find the roots of x and y
        x = self.find(x)
        y = self.find(y)

        # Union by size: Attach smaller tree under larger tree
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]

def minimumCost(n, edges, query):
    """
    Approach:
    1. Use Union-Find (Disjoint Set Union) to group connected components of the graph.
    2. Compute the bitwise AND of all edge weights within each connected component.
    3. For each query (src, dst), check if they belong to the same component:
        - If they do, return the precomputed bitwise AND value.
        - If not, return -1.
    """

    # Step 1: Connect all nodes in the same component using Union-Find
    uf = UnionFind(n)
    for u, v, w in edges:
        uf.union(u, v)

    # Step 2: Compute bitwise AND of all edge weights for each connected component
    component_cost = {}
    for u, v, w in edges:
        root = uf.find(u)
        if root not in component_cost:
            component_cost[root] = w
        else:
            component_cost[root] &= w   # Perform bitwise AND with existing weight

    # Step 3: Process each query
    out = []
    for src, dst in query:
        r1, r2 = uf.find(src), uf.find(dst)
        if r1 != r2:
            out.append(-1)              # If they are in different components, no valid path exists
        else:
            out.append(component_cost[r1])

    return out


def main():
    # Test - 1
    n1 = 5
    edges1 = [[0,1,7],[1,3,7],[1,2,1]]
    query1 = [[0,3],[3,4]]
    print(f"output-1: {minimumCost(n1, edges1, query1)}")

    # Test - 2
    n2 = 3
    edges2 = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
    query2 = [[1,2]]
    print(f"output-2: {minimumCost(n2, edges2, query2)}")


if __name__ == "__main__":
    main()
