# Problem: https://leetcode.com/problems/reorder-list
# Time Complexity: O(n)         # n = number of nodes in the linked list
# Space Complexity: O(1)        # In-place modification without extra space

from ListNode import create_linked_list, print_linked_list

def reorderList(head):
    """
    Approach:
        - Step 1: Use Floyd's Tortoise and Hare algorithm to find the middle of the list.
        - Step 2: Reverse the second half of the list.
        - Step 3: Merge the two halves by alternating nodes from each.
        - The list is reordered in-place; no extra memory is used.
    """
    if not head or not head.next:
        return

    slow, fast = head, head.next

    # Step 1: Find the middle of the list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next     # Start of second half
    slow.next = None       # Split the list into two halves
    prev = None

    # Step 2: Reverse the second half
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # Step 3: Merge the two halves
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

# Test Cases
def main():
    # Test - 1
    head1 = create_linked_list([1, 2, 3, 4])
    reorderList(head1)
    print("output-1:", print_linked_list(head1))

    # Test - 2
    head2 = create_linked_list([1, 2, 3, 4, 5])
    reorderList(head2)
    print("output-2:", print_linked_list(head2))

if __name__ == "__main__":
    main()
