# Problem: https://leetcode.com/problems/reverse-linked-list-ii

# Time Complexity: O(n), where n = number of nodes in the list
# Space Complexity: O(1), in-place reversal

from ListNode import ListNode, create_linked_list, print_linked_list

def reverseBetween(head, left, right):
    """
    Approach:
        - Use a dummy node to handle edge cases (like reversing from head).
        - Traverse to the node just before the `left` position.
        - Reverse the sublist in-place between `left` and `right` using head insertion method.
        - Return the updated list starting from dummy.next.
    """
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move `prev` to the node just before `left`
    for _ in range(left - 1):
        prev = prev.next

    # Standard reverse logic for the sublist
    reverse_prev = prev
    curr = prev.next
    prev = None

    # Reverse the sublist between left and right
    for _ in range(right - left + 1):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # Connect reversed sublist back
    # Reversed: 4 -> 3 -> 2 -> None , Remaining: 5
    # reverse_prev.next.next = Node 1.Node 2.next

    reverse_prev.next.next = curr     # tail of reversed part connects to remainder
    reverse_prev.next = prev          # node before left connects to new head of reversed part

    return dummy.next

def main():
    # Test - 1
    head1 = create_linked_list([1,2,3,4,5])
    left1, right1 = 2, 4
    result1 = reverseBetween(head1, left1, right1)
    print(f"output-1: {print_linked_list(result1)}")

    # Test - 2
    head2 = create_linked_list([5])
    left2, right2 = 1, 1
    result2 = reverseBetween(head2, left2, right2)
    print(f"output-2: {print_linked_list(result2)}")

if __name__ == "__main__":
    main()
