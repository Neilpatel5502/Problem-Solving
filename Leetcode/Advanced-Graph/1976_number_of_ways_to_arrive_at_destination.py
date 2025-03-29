# Problem Link: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination

# Time Complexity: O((V + E) log V)       V = Number of vertices, E = number of edges
# Space Complexity: O(V + E)

from collections import defaultdict
from heapq import heappop, heappush

def countPaths(n, roads):
    """
    Approach:
        - Construct the adjacency list for the given roads.
        - Use Dijkstra's algorithm to find the shortest time to reach each node.
        - Maintain an array to store the number of ways to reach each node using the shortest time.
        - Use a min-heap (priority queue) for efficient shortest path computation.
        - Return the number of ways to reach node (n-1) modulo 10^9 + 7.
    """

    # Construct the adjacency list
    adj = defaultdict(list)
    for u, v, w in roads:
        adj[u].append((w, v))
        adj[v].append((w, u))

    MOD = 10**9 + 7                 # Modulo for large numbers
    heap = [(0, 0)]                 # (cost, node)
    min_cost = [float('inf')] * n   # Stores shortest cost to reach each node
    path_count = [0] * n            # Stores number of ways to reach each node
    path_count[0] = 1               # There's only one way to start from node 0

    # Implement Dijkstra's algorithm
    while heap:
        cost, node = heappop(heap)

        # Explore neighbors
        for nei_cost, nei in adj[node]:

            # If a new shorter path is found, update min_cost and reset path_count
            if cost + nei_cost < min_cost[nei]:
                min_cost[nei] = cost + nei_cost
                path_count[nei] = path_count[node]      # Inherit ways from the current node
                heappush(heap, (cost + nei_cost, nei))

            # If another shortest path is found, add the number of ways
            elif cost + nei_cost == min_cost[nei]:
                # Count ways mod 10^9+7
                path_count[nei] = (path_count[nei] + path_count[node]) % MOD

    return path_count[n - 1]


def main():
    # Test - 1
    n1 = 7
    roads1 = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    print(f"output-1: {countPaths(n1, roads1)}")

    # Test - 2
    n2 = 2
    roads2 = [[1,0,10]]
    print(f"output-2: {countPaths(n2, roads2)}")


if __name__ == "__main__":
    main()
