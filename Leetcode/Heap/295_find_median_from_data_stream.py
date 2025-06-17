# Problem: https://leetcode.com/problems/find-median-from-data-stream

# Time Complexity: O(log n) for addNum, O(1) for findMedian
# Space Complexity: O(n) for storing all elements in two heaps

import heapq

class MedianFinder:
    """
    Approach:
        - Maintain two heaps:
            1. low_heap (Max-heap using negative values): holds the smaller half of numbers.
            2. high_heap (Min-heap): holds the larger half of numbers.
        - Insertion maintains the invariant: max(low_heap) <= min(high_heap)
        - Ensure the heaps remain balanced in size. If odd count, low_heap has one extra.
        - Median:
            - If total count is odd, median is top of low_heap.
            - If even, it's the average of tops of both heaps.
    """

    def __init__(self):
        self.low_heap = []      # Max-heap simulated with negative values
        self.high_heap = []     # Min-heap for larger half

    def addNum(self, num):
        # Step 1: Push to max-heap (as negative to simulate max-heap)
        heapq.heappush(self.low_heap, -num)

        # Step 2: Move the largest from low_heap to high_heap to maintain order property
        heapq.heappush(self.high_heap, -self.low_heap[0])
        heapq.heappop(self.low_heap)

        # Step 3: Balance the heaps such that low_heap can have at most 1 more element
        if len(self.low_heap) < len(self.high_heap):
            heapq.heappush(self.low_heap, -self.high_heap[0])
            heapq.heappop(self.high_heap)

    def findMedian(self):
        # If odd total, median is top of low_heap
        if len(self.low_heap) > len(self.high_heap):
            return -self.low_heap[0]

        # If even total, median is average of tops of both heaps
        return (-self.low_heap[0] + self.high_heap[0]) / 2


def main():
    mf = MedianFinder()

    # Test - 1
    out1 = [
        None,
        mf.addNum(1),
        mf.addNum(2),
        mf.findMedian(),
        mf.addNum(3),
        mf.findMedian(),
    ]
    print(f"output-1: {out1}")

if __name__ == "__main__":
    main()
