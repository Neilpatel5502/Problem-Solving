# Problem: https://leetcode.com/problems/sort-list

# Time Complexity: O(n log n), where n is the number of nodes in the linked list
# Space Complexity: O(log n) due to recursion stack in divide step

from ListNode import ListNode, print_linked_list, create_linked_list

def sortList(head):
    """
    Approach:
        - Use Merge Sort for sorting a singly linked list.
        - Step 1: Use slow and fast pointers to find the midpoint and split the list.
        - Step 2: Recursively sort the left and right halves.
        - Step 3: Merge the sorted halves using a helper function.
    """
    if not head or not head.next:
        return head

    # Step 1: Split the list into two halves
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None  # Break the list

    # Step 2: Recursively sort each half
    left = sortList(head)
    right = sortList(mid)

    # Step 3: Merge sorted halves
    return merge(left, right)


def merge(l1, l2):
    """Helper function to merge two sorted linked lists"""
    dummy = ListNode(0)
    cur = dummy

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    cur.next = l1 or l2
    return dummy.next


def main():
    # Test - 1
    arr1 = [4, 2, 1, 3]
    head1 = create_linked_list(arr1)
    sorted_head1 = sortList(head1)
    print(f"output-1: {print_linked_list(sorted_head1)}")

    # Test - 2
    arr2 = [-1, 5, 3, 4, 0]
    head2 = create_linked_list(arr2)
    sorted_head2 = sortList(head2)
    print(f"output-2: {print_linked_list(sorted_head2)}")

    # Test - 3
    arr3 = []
    head3 = create_linked_list(arr3)
    sorted_head3 = sortList(head3)
    print(f"output-3: {print_linked_list(sorted_head3)}")

if __name__ == "__main__":
    main()
