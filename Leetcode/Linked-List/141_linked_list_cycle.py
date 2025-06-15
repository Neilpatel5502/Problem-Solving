# Problem: https://leetcode.com/problems/linked-list-cycle

# Time Complexity: O(n)       # n = number of nodes in the list
# Space Complexity: O(1)      # Uses constant space with two pointers

from ListNode import create_linked_list

def hasCycle(head):
    """
    Approach:
        - Use Floyd's Cycle Detection Algorithm (Tortoise and Hare).
        - Initialize two pointers, slow and fast, both starting at head.
        - Move slow one step at a time and fast two steps.
        - If there is a cycle, slow and fast will eventually meet.
        - If fast reaches the end (null), there is no cycle.
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next         # Move one step
        fast = fast.next.next    # Move two steps

        if slow == fast:         # Pointers meet: cycle detected
            return True

    return False                 # Reached end of list: no cycle

# Test Cases
def main():
    # Test - 1: Cycle exists
    head1 = create_linked_list([3, 2, 0, -4], 1)
    print("output-1:", hasCycle(head1))

    # Test - 2: Cycle exists
    head2 = create_linked_list([1, 2], 0)
    print("output-2:", hasCycle(head2))

    # Test - 3: No cycle
    head3 = create_linked_list([1], -1)
    print("output-3:", hasCycle(head3))

if __name__ == "__main__":
    main()
