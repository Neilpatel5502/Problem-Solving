# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import defaultdict
from ListNode import ListNode, create_linked_list, print_linked_list

def deleteDuplicates(head):
    """
    Approach:
        - First pass: Count the frequency of each value in the list.
        - Second pass: Build a new list with only the values that appeared once.
    """
    if not head or not head.next:
        return head

    # First pass: Count all node values
    counter = defaultdict(int)
    cur = head
    while cur:
        counter[cur.val] += 1
        cur = cur.next

    # Second pass: Build a new list with only unique values
    dummy = ListNode(0)
    new = dummy
    cur = head

    while cur:
        if counter[cur.val] == 1:
            new.next = ListNode(cur.val)
            new = new.next
        cur = cur.next

    return dummy.next

def main():
    # Test - 1
    head1 = create_linked_list([1,2,3,3,4,4,5])
    result1 = deleteDuplicates(head1)
    print(f"output-1: {print_linked_list(result1)}")

    # Test - 2
    head2 = create_linked_list([1,1,1,2,3])
    result2 = deleteDuplicates(head2)
    print(f"output-2: {print_linked_list(result2)}")

if __name__ == "__main__":
    main()
