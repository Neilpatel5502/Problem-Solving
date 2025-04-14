class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next

    return res

# Helper to create linked list with a cycle at position `pos`
def create_linked_list(values, pos):
    dummy = ListNode(0)
    curr = dummy
    cycle_node = None

    for idx, val in enumerate(values):
        node = ListNode(val)
        if idx == pos:
            cycle_node = node
        curr.next = node
        curr = curr.next

    if pos != -1:
        curr.next = cycle_node

    return dummy.next
