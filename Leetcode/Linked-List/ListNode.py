class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values, pos=None):
    """
    Method overloading simulation:
    - If `pos` is None, creates a normal linked list.
    - If `pos` is an integer, creates a linked list with a cycle at that position.
    """
    dummy = ListNode(0)
    curr = dummy
    cycle_node = None

    for idx, val in enumerate(values):
        node = ListNode(val)
        if pos is not None and idx == pos:
            cycle_node = node
        curr.next = node
        curr = curr.next

    if pos is not None and pos != -1:
        curr.next = cycle_node

    return dummy.next

def print_linked_list(head):
    """Print the linked list. Stops if a cycle is detected."""
    res = []
    visited = set()
    while head and head not in visited:
        res.append(head.val)
        visited.add(head)
        head = head.next
    return res



# Definition for a Node with random pointer
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random

# Helper: Build linked list with random pointers
def create_random_linked_list(arr):
    if not arr:
        return None
    nodes = [Node(val) for val, _ in arr]
    for i, (_, rand_idx) in enumerate(arr):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]

# Helper: Print linked list with random pointers
def print_random_linked_list(head):
    res = []
    node_to_index = {}
    index = 0
    curr = head

    # First pass: assign indices to nodes
    while curr:
        node_to_index[curr] = index
        curr = curr.next
        index += 1

    # Second pass: build output list with [val, random_index]
    curr = head
    while curr:
        rand_idx = node_to_index[curr.random] if curr.random else None
        res.append([curr.val, rand_idx])
        curr = curr.next

    return res
