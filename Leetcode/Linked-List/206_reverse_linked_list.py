# Problem: https://leetcode.com/problems/reverse-linked-list
# Time Complexity: O(n)       # n is the number of nodes in the linked list
# Space Complexity: O(1)      # In-place reversal using constant space

from ListNode import create_linked_list, print_linked_list

def reverseList(head):
    """
    Approach:
        - Initialize two pointers: `prev` as None and `cur` as the head of the list.
        - Iterate through the list, and for each node:
            - Store the next node.
            - Reverse the current node's pointer to point to `prev`.
            - Move `prev` and `cur` one step forward.
        - After the loop, `prev` will point to the new head of the reversed list.
        - Return `prev`.
    """
    prev = None         # Pointer to the previous node (initially None)
    cur = head          # Pointer to the current node starting at head

    # Iterate through the list
    while cur:
        temp = cur.next     # Store the next node
        cur.next = prev     # Reverse the link
        prev = cur          # Move prev to current
        cur = temp          # Move to the next node

    return prev             # New head of the reversed list

# Test Cases
def main():

    # Test - 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = reverseList(head1)
    print("output-1:", print_linked_list(reversed1))

    # Test - 2
    head2 = create_linked_list([1, 2])
    reversed2 = reverseList(head2)
    print("output-2:", print_linked_list(reversed2))

    # Test - 3
    head3 = create_linked_list([])
    reversed3 = reverseList(head3)
    print("output-3:", print_linked_list(reversed3))

if __name__ == "__main__":
    main()
