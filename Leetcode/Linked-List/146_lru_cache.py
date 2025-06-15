# Problem: https://leetcode.com/problems/lru-cache

# Time Complexity: O(1) average for both get and put
# Space Complexity: O(capacity) for storing cache entries

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
    """
    Approach:
        - Use a doubly linked list to track the order of usage (most recently used near the tail).
        - Use a hashmap to store key -> node mappings for O(1) access.
        - On 'get': move the accessed node to the end (most recently used).
        - On 'put': insert a new node and evict the least recently used (from the front) if capacity exceeded.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps key to node

        # Dummy nodes to avoid edge-case handling
        self.left = Node(0, 0)  # Least Recently Used (front)
        self.right = Node(0, 0) # Most Recently Used (back)

        self.left.next, self.right.prev = self.right, self.left

    # Helper to insert node at the end (before self.right)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    # Helper to remove a node from anywhere in the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])        # Remove from current position
            self.insert(self.cache[key])        # Re-insert at end (most recent)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])        # Remove old entry

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])            # Insert as most recently used

        if len(self.cache) > self.capacity:
            lru = self.left.next                # Node next to left dummy is LRU
            self.remove(lru)
            del self.cache[lru.key]

# Test Cases
def main():
    # Test - 1
    obj = None
    output = []

    ops = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    for op, arg in zip(ops, args):
        if op == "LRUCache":
            obj = LRUCache(*arg)
            output.append(None)
        elif op == "put":
            obj.put(*arg)
            output.append(None)
        elif op == "get":
            result = obj.get(*arg)
            output.append(result)

    print("Output-1:", output)
if __name__ == "__main__":
    main()
