# Problem: https://leetcode.com/problems/ipo

# Time Complexity: O(n log n), where n is the number of projects (each project goes through heap operations)
# Space Complexity: O(n) for storing heaps

import heapq

def findMaximizedCapital(k, w, profits, capital):
    """
    Approach:
        - Maintain two heaps:
            1. minCapital: Min-heap based on required capital to unlock projects.
            2. maxProfit: Max-heap to choose the most profitable project that is currently affordable.
        - Iterate up to k times (number of projects allowed to choose):
            - While there are affordable projects in minCapital (capital requirement <= current capital `w`),
              move them to maxProfit heap.
            - If no projects are affordable, break early.
            - Otherwise, pick the most profitable project from maxProfit and increase capital `w`.
        - Return the final capital after selecting up to k projects.
    """
    maxProfit = []  # Max heap to store affordable projects by profit
    minCapital = [(c, p) for c, p in zip(capital, profits)]  # Min heap sorted by capital required
    heapq.heapify(minCapital)

    for _ in range(k):
        # Move all affordable projects into the maxProfit heap
        while minCapital and minCapital[0][0] <= w:
            c, p = heapq.heappop(minCapital)
            heapq.heappush(maxProfit, -p)

        # No projects can be undertaken with current capital
        if not maxProfit:
            break

        # Pick the project with the highest profit
        w += -heapq.heappop(maxProfit)

    return w


def main():
    # Test - 1
    k1 = 2
    w1 = 0
    profits1 = [1, 2, 3]
    capital1 = [0, 1, 1]
    print(f"output-1: {findMaximizedCapital(k1, w1, profits1, capital1)}")

    # Test - 2
    k2 = 3
    w2 = 0
    profits2 = [1, 2, 3]
    capital2 = [0, 1, 2]
    print(f"output-2: {findMaximizedCapital(k2, w2, profits2, capital2)}")

if __name__ == "__main__":
    main()
