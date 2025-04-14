# Problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Time Complexity: O(n), where n is the number of nodes in the list
# Space Complexity: O(1), in-place reversal without extra space

from ListNode import ListNode, create_linked_list, print_linked_list

def reverseKGroup(head, k):
    """
    Approach:
        - Use a dummy node to simplify reversal logic at the head.
        - For each group of k nodes:
            - Find the k-th node from the current group start.
            - Reverse all k nodes between current group and the next group.
            - Reconnect the reversed group back to the list.
        - If fewer than k nodes remain, leave them as is.
    """
    dummy = ListNode(0, head)
    prev_group = dummy

    while True:
        kth_node = getKthNode(prev_group, k)
        if not kth_node:
            break

        next_group = kth_node.next

        # Reverse k nodes
        prev, cur = kth_node.next, prev_group.next
        while cur != next_group:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # Connect reversed group to previous and next
        tmp = prev_group.next  # This is the tail after reversal
        prev_group.next = kth_node
        prev_group = tmp

    return dummy.next

def getKthNode(cur, k):
    while cur and k > 0:
        cur = cur.next
        k -= 1
    return cur

# Test Cases
def main():
    # Test - 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = reverseKGroup(head1, 2)
    print("output-1:", print_linked_list(result1))

    # Test - 2
    head2 = create_linked_list([1, 2, 3, 4, 5])
    result2 = reverseKGroup(head2, 3)
    print("output-2:", print_linked_list(result2))

if __name__ == "__main__":
    main()
