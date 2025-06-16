from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def build_graph(adj_list):
    if not adj_list:
        return None

    nodes = {}

    # Create all nodes
    for i in range(1, len(adj_list) + 1):
        nodes[i] = Node(i)

    # Connect neighbors
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]

    return nodes[1]  # Return the node with value 1 as the entry point

def graph_to_list(node):
    if not node:
        return []

    adj = {}
    visited = set()
    queue = deque([node])

    while queue:
        curr = queue.popleft()
        if curr.val in visited:
            continue
        visited.add(curr.val)
        adj[curr.val] = [neighbor.val for neighbor in curr.neighbors]
        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                queue.append(neighbor)

    # Convert to adjacency list ordered by node value
    res = []
    for i in range(1, max(adj.keys()) + 1):
        res.append(adj.get(i, []))
    return res
