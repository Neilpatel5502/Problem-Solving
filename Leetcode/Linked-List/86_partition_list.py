# Problem: https://leetcode.com/problems/partition-list

# Time Complexity: O(n)
# Space Complexity: O(n) – due to creation of new nodes

from ListNode import ListNode, create_linked_list, print_linked_list

def partition(head, x):
    """
    Approach:
        - Create two dummy heads for two lists:
            1. One for nodes with values < x (left list).
            2. One for nodes with values >= x (right list).
        - Traverse the original list and append nodes to appropriate list.
        - Connect left list to right list at the end.
        - Return head of the new merged list.
    """
    if not head or not head.next:
        return head

    dummy_l = ListNode(0)  # Dummy head for left list
    left = dummy_l
    dummy_r = ListNode(0)  # Dummy head for right list
    right = dummy_r
    cur = head

    while cur:
        if cur.val < x:
            left.next = ListNode(cur.val)  # Add to left list
            left = left.next
        else:
            right.next = ListNode(cur.val)  # Add to right list
            right = right.next
        cur = cur.next

    left.next = dummy_r.next  # Merge right list after left
    return dummy_l.next       # Return head of merged list


def main():
    # Test - 1
    head1 = create_linked_list([1, 4, 3, 2, 5, 2])
    x1 = 3
    result1 = partition(head1, x1)
    print(f"output-1: {print_linked_list(result1)}")

    # Test - 2
    head2 = create_linked_list([2, 1])
    x2 = 2
    result2 = partition(head2, x2)
    print(f"output-2: {print_linked_list(result2)}")

if __name__ == "__main__":
    main()
