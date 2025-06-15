# Problem: https://leetcode.com/problems/merge-two-sorted-lists

# Time Complexity: O(n + m)       # n = length of list1, m = length of list2
# Space Complexity: O(1)          # In-place merging using constant space

from ListNode import ListNode, create_linked_list, print_linked_list

def mergeTwoLists(list1, list2):
    """
    Approach:
        - Create a dummy node to serve as the start of the merged list.
        - Use a pointer `node` to build the list by comparing current nodes of list1 and list2.
        - Append the smaller node to `node.next` and advance the respective list.
        - After the loop, if one list is not exhausted, append it to the merged list.
        - Return `dummy.next` which points to the head of the merged list.
    """
    dummy = ListNode()   # Dummy node to simplify edge cases
    node = dummy         # Pointer to build the merged list

    # Traverse both lists and pick the smaller value
    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next

    # Append the remaining nodes of the non-empty list
    node.next = list1 or list2

    return dummy.next

# Test Cases
def main():
    # Test - 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged1 = mergeTwoLists(list1, list2)
    print("output-1:", print_linked_list(merged1))

    # Test - 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged2 = mergeTwoLists(list1, list2)
    print("output-2:", print_linked_list(merged2))

    # Test - 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged3 = mergeTwoLists(list1, list2)
    print("output-3:", print_linked_list(merged3))

if __name__ == "__main__":
    main()
