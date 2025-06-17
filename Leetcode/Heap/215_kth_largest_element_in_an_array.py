# Problem: https://leetcode.com/problems/kth-largest-element-in-an-array

# Time Complexity: O(n log n) in worst-case due to heap operations (each push/pop is log n, done n times)
# Space Complexity: O(n) due to heap storing all elements

import heapq

def findKthLargest(nums, k):
    """
    Approach:
        - Use a max-heap to efficiently retrieve the k-th largest element.
        - Since Python's heapq implements a min-heap, insert negative values to simulate a max-heap.
        - Push all elements as negative values into the heap.
        - Pop k-1 elements from the heap (which removes the largest k-1 values).
        - The next element popped is the k-th largest (in negative form), so return its negation.
    """
    heap = []  # Max-heap simulated with negative values

    # Insert all elements as negative to simulate max-heap
    for n in nums:
        heapq.heappush(heap, -n)

    # Pop the largest k-1 elements
    for _ in range(k - 1):
        heapq.heappop(heap)

    # The next popped element is the k-th largest
    return -heapq.heappop(heap)


def main():
    # Test - 1
    nums1 = [3,2,1,5,6,4]
    k1 = 2
    print(f"output-1: {findKthLargest(nums1, k1)}")

    # Test - 2
    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    print(f"output-2: {findKthLargest(nums2, k2)}")

if __name__ == "__main__":
    main()
