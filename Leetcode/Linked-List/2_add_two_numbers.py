# Problem: https://leetcode.com/problems/add-two-numbers

# Time Complexity: O(max(m, n))   # m = length of l1, n = length of l2
# Space Complexity: O(max(m, n))  # Result list size is proportional to the longer input

from ListNode import ListNode, create_linked_list, print_linked_list

def addTwoNumbers(l1, l2):
    """
    Approach:
        - Traverse both lists while adding corresponding digits and carry.
        - If one list is shorter, treat its value as 0.
        - Maintain a dummy node to simplify the result list construction.
        - At the end, if there's a carry left, append it as a new node.
    """
    dummy = ListNode()    # Dummy node to hold result list
    cur = dummy           # Pointer to build the result
    carry = 0             # Carry from previous sum

    while l1 or l2:
        v1 = l1.val if l1 else 0  # Value from l1, or 0 if None
        v2 = l2.val if l2 else 0  # Value from l2, or 0 if None

        value = v1 + v2 + carry   # Add values and carry
        carry = value // 10       # Update carry
        value = value % 10        # Get digit to store

        cur.next = ListNode(value)  # Create new node
        cur = cur.next

        # Move to next nodes if available
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry:
        cur.next = ListNode(1)  # Append leftover carry as node

    return dummy.next

# Test Cases
def main():
    # Test - 1
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result1 = addTwoNumbers(l1, l2)
    print("output-1:", print_linked_list(result1))

    # Test - 2
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result2 = addTwoNumbers(l1, l2)
    print("output-2:", print_linked_list(result2))

    # Test - 3
    l1 = create_linked_list([9,9,9,9,9,9,9])
    l2 = create_linked_list([9,9,9,9])
    result3 = addTwoNumbers(l1, l2)
    print("output-3:", print_linked_list(result3))

if __name__ == "__main__":
    main()
