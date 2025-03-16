# Problem Link: https://leetcode.com/problems/minimum-time-to-repair-cars

# Time Complexity: O(n log m) -> n is len of ranks and m is min(ranks) * cars^2.
# Space Complexity: O(1).

import math

def repairCars(ranks, cars):
    """
    Approach:
        - The solution uses binary search on the range of possible values (from 0 to min(ranks) * cars * cars).
        - A mechanic can repair at most `floor(T / r) ** 0.5` cars within a given time `T`.
    Steps:
        1. Set `left` as the minimum possible time and `right` as the where a single mechanic with the lowest rank
        repairs all `cars`, which takes `min(ranks) * cars^2` time.
        2. Perform binary search on this range to find the minimum possible time.
        3. Check how many cars can be repaired within `mid` time by summing `floor((mid // rank) ** 0.5)` for all mechanics.
        4. If the count is greater than or equal to `cars`, try reducing the time (`right = mid - 1`).
        5. Otherwise, increase the time (`left = mid + 1`).
    """

    left = 0
    right = min(ranks) * cars * cars

    while left <= right:
        mid = (left + right) // 2
        count = 0                   # Number of cars that can be repaired within `mid` time

        for rank in ranks:
            count += math.floor((mid // rank) ** 0.5)   # Number of cars this mechanic can repair

        if count >= cars:           # If we can repair at least `cars`, reduce time
            right = mid - 1
        else:                       # If not enough cars are repaired, increase time
            left = mid + 1

    return left

def main():
    # Test - 1
    ranks1 = [4,2,3,1]
    cars1 = 10
    print(f"output-1: {repairCars(ranks1, cars1)}")

    # Test - 2
    ranks2 = [5,1,8]
    cars2 = 6
    print(f"output-2: {repairCars(ranks2, cars2)}")

if __name__ == "__main__":
    main()
