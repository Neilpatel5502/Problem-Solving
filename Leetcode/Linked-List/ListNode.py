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
