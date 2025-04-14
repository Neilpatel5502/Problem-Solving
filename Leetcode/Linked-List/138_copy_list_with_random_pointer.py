# Problem: https://leetcode.com/problems/copy-list-with-random-pointer/
# Time Complexity: O(n)       # Traverse the list twice: once to copy nodes, once to set pointers
# Space Complexity: O(n)      # Dictionary to store original-to-copy node mapping

from ListNode import Node, create_random_linked_list, print_random_linked_list

def copyRandomList(head):
    """
    Approach:
        - Use a hash map to keep a mapping between original nodes and their copies.
        - First pass: Create a new node for each original node and store in the map.
        - Second pass: Use the map to assign the next and random pointers for the copied nodes.
        - Return the copied head node.
    """
    nodeMap = {None: None}  # Handles cases where a pointer is None

    # First pass: Create a copy of each node and store it in the map
    cur = head
    while cur:
        copy = Node(cur.val)     # Create new node with same value
        nodeMap[cur] = copy      # Map original node to its copy
        cur = cur.next

    # Second pass: Assign next and random pointers using the map
    cur = head
    while cur:
        copy = nodeMap[cur]
        copy.next = nodeMap[cur.next]
        copy.random = nodeMap[cur.random]
        cur = cur.next

    return nodeMap[head]

# Test Cases
def main():

    # Test - 1
    arr1 = [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]
    head1 = create_random_linked_list(arr1)
    copied1 = copyRandomList(head1)
    print("output-1:", print_random_linked_list(copied1))

    # Test - 2
    arr2 = [(1, 1), (2, 1)]
    head2 = create_random_linked_list(arr2)
    copied2 = copyRandomList(head2)
    print("output-2:", print_random_linked_list(copied2))

    # Test - 3
    arr3 = [(3, None), (3, 0), (3, None)]
    head3 = create_random_linked_list(arr3)
    copied3 = copyRandomList(head3)
    print("output-3:", print_random_linked_list(copied3))

if __name__ == "__main__":
    main()
