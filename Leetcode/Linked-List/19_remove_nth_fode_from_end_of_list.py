# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Time Complexity: O(n)       # Single pass through the list to remove the node
# Space Complexity: O(1)      # Uses constant space with two pointers

from ListNode import ListNode, create_linked_list, print_linked_list

def removeNthFromEnd(head, n):
    """
    Approach:
        - Use two pointers (left and right).
        - Move the right pointer `n` steps ahead.
        - Move both pointers together until right reaches the end.
        - The left pointer will then be just before the target node.
        - Modify `left.next` to remove the nth node from the end.
        - Use a dummy node to simplify edge cases like removing the head.
    """
    dummy = ListNode(0, head)  # Dummy node before the head
    left = dummy
    right = head

    # Move right n steps ahead
    while n > 0 and right:
        right = right.next
        n -= 1

    # Move both pointers until right reaches the end
    while right:
        left = left.next
        right = right.next

    # Remove the nth node from end
    left.next = left.next.next

    return dummy.next

# Test Cases
def main():
    # Test - 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = removeNthFromEnd(head1, 2)
    print("output-1:", print_linked_list(result1))

    # Test - 2
    head2 = create_linked_list([1])
    result2 = removeNthFromEnd(head2, 1)
    print("output-2:", print_linked_list(result2))

    # Test - 3
    head3 = create_linked_list([1, 2])
    result3 = removeNthFromEnd(head3, 1)
    print("output-3:", print_linked_list(result3))

if __name__ == "__main__":
    main()
