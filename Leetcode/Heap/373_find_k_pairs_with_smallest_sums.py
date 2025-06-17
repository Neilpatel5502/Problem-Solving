# Problem: https://leetcode.com/problems/find-k-pairs-with-smallest-sums

# Time Complexity: O(k log k) in practice since we process up to k heap elements
# Space Complexity: O(k) for heap and visited set

import heapq

def kSmallestPairs(nums1, nums2, k):
    """
    Approach:
        - Use a min-heap to always expand the pair with the smallest sum.
        - Start with the smallest possible pair (nums1[0], nums2[0]).
        - At each step, pop the smallest pair from heap and add to result.
        - Push the next possible pairs (right and down in 2D matrix) into heap if not visited:
            (i+1, j) and (i, j+1)
        - Use a visited set to avoid pushing duplicate pairs into the heap.
    """
    out = []

    if not nums1 or not nums2:
        return out

    heap = []          # Min heap to track next minimum sum pair
    visited = set()    # Set to avoid revisiting the same (i, j)

    # Start with smallest pair (0,0)
    heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
    visited.add((0, 0))

    # Extract k smallest pairs
    while k and heap:
        _, i, j = heapq.heappop(heap)
        out.append([nums1[i], nums2[j]])
        k -= 1

        # Push next pair in row (i+1, j)
        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            visited.add((i + 1, j))

        # Push next pair in column (i, j+1)
        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            visited.add((i, j + 1))

    return out


def main():
    # Test - 1
    nums1_1 = [1, 7, 11]
    nums2_1 = [2, 4, 6]
    k1 = 3
    print(f"output-1: {kSmallestPairs(nums1_1, nums2_1, k1)}")

    # Test - 2
    nums1_2 = [1, 1, 2]
    nums2_2 = [1, 2, 3]
    k2 = 2
    print(f"output-2: {kSmallestPairs(nums1_2, nums2_2, k2)}")

if __name__ == "__main__":
    main()
