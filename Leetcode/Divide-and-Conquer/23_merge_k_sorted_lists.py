# Problem: https://leetcode.com/problems/merge-k-sorted-lists

# Time Complexity: O(N log k), where N is total number of nodes, and k is number of lists
# Space Complexity: O(1) (ignoring the output list), or O(log k) stack space if recursion is used

from ListNode import ListNode, create_linked_list, print_linked_list

def mergeKLists(lists):
    """
    Approach:
        - Use a bottom-up pairwise merging strategy (similar to merge sort).
        - Repeatedly merge pairs of lists until only one remains.
        - For merging two lists, use the standard two-pointer technique.
    """
    if not lists:
        return None

    # Merge in pairs until one list remains
    while len(lists) > 1:
        merged_lists = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            merged_lists.append(mergeList(l1, l2))

        lists = merged_lists

    return lists[0]

# https://leetcode.com/problems/merge-two-sorted-lists/
def mergeList(list1, list2):
    dummy = ListNode()
    node = dummy

    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next

    node.next = list1 or list2
    return dummy.next

# Test Cases
def main():
    # Test - 1
    l1 = create_linked_list([1, 4, 5])
    l2 = create_linked_list([1, 3, 4])
    l3 = create_linked_list([2, 6])
    lists1 = [l1, l2, l3]
    merged1 = mergeKLists(lists1)
    print("output-1:", print_linked_list(merged1))

    # Test - 2
    lists2 = []
    merged2 = mergeKLists(lists2)
    print("output-2:", print_linked_list(merged2))

    # Test - 3
    l1 = create_linked_list([])
    lists3 = [l1]
    merged3 = mergeKLists(lists3)
    print("output-3:", print_linked_list(merged3))

if __name__ == "__main__":
    main()
