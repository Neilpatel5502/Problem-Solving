# Problem: https://leetcode.com/problems/evaluate-division

# Time Complexity: O(N + Q) * avg_neighbors     # N = number of equations, Q = number of queries
# Space Complexity: O(N)                        # For graph storage

from collections import defaultdict, deque

def calcEquation(equations, values, queries):
    """
    Approach:
        - Build a bidirectional graph where each equation A / B = k represents:
            A → B with weight k
            B → A with weight 1/k
        - For each query X / Y, use BFS to find a path from X to Y.
        - Accumulate the product of edge weights along the path.
        - If no path exists, return -1.
    """
    graph = defaultdict(list)

    # Step 1: Build the graph from equations
    for i in range(len(equations)):
        A, B = equations[i]
        graph[A].append([B, values[i]])         # A -> B with weight values[i]
        graph[B].append([A, 1 / values[i]])     # B -> A with weight 1/values[i]

    # Step 2: BFS to find path from src to target
    def bfs(src, target):
        if src not in graph or target not in graph:
            return -1.0

        queue = deque([[src, 1.0]])             # queue holds [current_node, cumulative_product]
        visited = set([src])

        while queue:
            node, weight = queue.popleft()

            if node == target:
                return weight

            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append([neighbor, weight * w])

        return -1.0

    # Step 3: Evaluate each query
    return [bfs(q[0], q[1]) for q in queries]


def main():
    # Test - 1
    equations1 = [["a", "b"], ["b", "c"]]
    values1 = [2.0, 3.0]
    queries1 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(f"output-1: {calcEquation(equations1, values1, queries1)}")

    # Test - 2
    equations2 = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values2 = [1.5, 2.5, 5.0]
    queries2 = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    print(f"output-2: {calcEquation(equations2, values2, queries2)}")

    # Test - 3
    equations3 = [["a", "b"]]
    values3 = [0.5]
    queries3 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    print(f"output-3: {calcEquation(equations3, values3, queries3)}")

if __name__ == "__main__":
    main()
