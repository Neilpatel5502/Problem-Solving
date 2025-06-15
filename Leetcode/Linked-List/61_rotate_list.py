# Problem: https://leetcode.com/problems/rotate-list

# Time Complexity: O(n)
# Space Complexity: O(1)

from ListNode import create_linked_list, print_linked_list

def rotateRight(head, k):
    """
    Approach:
        - First, calculate the length of the list.
        - Use modulo to avoid unnecessary full rotations.
        - Find the new tail at (length - k - 1) and the new head at (length - k).
        - Break the list at the new tail and reattach the end to the original head.
    """
    if not head or not head.next:
        return head

    # Step 1: Find the length of the list
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next

    # Step 2: Handle full rotations
    k = k % length
    if k == 0:
        return head

    # Step 3: Traverse to the node before the new head
    counter = 0
    prev = head
    cur = head.next
    while counter < (length - k - 1):
        counter += 1
        prev = prev.next
        cur = cur.next

    # Step 4: Break and rotate
    prev.next = None         # Break the link
    new_head = cur           # New head starts here

    while cur.next:
        cur = cur.next       # Move to the last node

    cur.next = head          # Attach original head at the end

    return new_head

def main():
    # Test - 1
    head1 = create_linked_list([1,2,3,4,5])
    result1 = rotateRight(head1, 2)
    print(f"output-1: {print_linked_list(result1)}")

    # Test - 2
    head2 = create_linked_list([0,1,2])
    result2 = rotateRight(head2, 4)
    print(f"output-2: {print_linked_list(result2)}")

if __name__ == "__main__":
    main()
