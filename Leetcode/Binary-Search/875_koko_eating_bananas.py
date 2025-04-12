# Problem: https://leetcode.com/problems/koko-eating-bananas/
# Time Complexity: O(n * log m) – n = number of piles, m = max pile size
# Space Complexity: O(1) – constant space

import math

def minEatingSpeed(piles, h):
    """
    Approach:
        - Use binary search on the possible values of k (speed).
        - The lowest possible k is 1 (slowest), and the highest is max(piles) (fastest needed).
        - For each k, compute total hours Koko needs to eat all bananas using ceil(p / k) for each pile.
        - If total hours <= h, try a smaller k (move right pointer left).
        - Otherwise, try a larger k (move left pointer right).
        - The smallest k that satisfies the time constraint is the answer.
    """

    left, right = 1, max(piles)

    while left <= right:
        k = (left + right) // 2
        time_count = 0

        for p in piles:
            time_count += math.ceil(p / k)

        if time_count <= h:
            right = k - 1  # Try a smaller k
        else:
            left = k + 1  # Try a larger k

    return left  # Smallest valid k found


def main():
    # Test - 1
    piles1 = [3,6,7,11]
    h1 = 8
    print(f"output-1: {minEatingSpeed(piles1, h1)}")

    # Test - 2
    piles2 = [30,11,23,4,20]
    h2 = 5
    print(f"output-2: {minEatingSpeed(piles2, h2)}")

    # Test - 3
    piles3 = [30,11,23,4,20]
    h3 = 6
    print(f"output-3: {minEatingSpeed(piles3, h3)}")

if __name__ == "__main__":
    main()
