# Problem Link: https://leetcode.com/problems/maximum-candies-allocated-to-k-children

# Time Complexity: O(n log m) -> n is len of candies and m is sum(candies) // k.
# Space Complexity: O(1).

def maximumCandies(candies, k):
    """
    Approach:
        - Use binary search on possible values of candies can be given.

    Steps:
        1. If the total number of candies is less than k, it's impossible to give at least one candy per child, so return 0.
        2. Use binary search to determine the maximum candies each child can receive.
            - The search space is [1, sum(candies) // k], where:
            - `left = 1` (minimum possible candies per child).
            - `right = sum(candies) // k` (maximum possible candies per child).
        3. In each binary search iteration:
            - Check if we can distribute `mid` candies per child by counting how many children can be served.
            - If we can serve at least `k` children, it means we can try to increase the candy count (`left = mid + 1`).
            - Otherwise, reduce the possible amount (`right = mid - 1`).
        4. The final answer is stored in `out`, which tracks the largest valid value of `mid`.
    """
    if sum(candies) < k:
        return 0

    left = 1
    right = sum(candies) // k       # Maximum possible candies per child
    out = 0

    while left <= right:
        mid = (left + right) // 2
        count = 0                   # Count of children who can receive at least `mid` candies

        for c in candies:
            if c >= mid:
                count += c // mid

            if count >= k:
                break

        if count >= k:              # If we can distribute at least `mid` candies per child
            out = mid
            left = mid + 1          # Try for a larger amount per child
        else:
            right = mid - 1         # Reduce search space if we can't serve `k` children


    return out

def main():
    # Test - 1
    candies1 = [5,8,6]
    k1 = 3
    print(f"output-1: {maximumCandies(candies1, k1)}")

    # Test - 2
    candies2 = [2,5]
    k2 = 11
    print(f"output-2: {maximumCandies(candies2, k2)}")

    # Test - 3
    candies3 = [4,9,4,7,8,10,3,10,3,9]
    k3 = 9
    print(f"output-3: {maximumCandies(candies3, k3)}")

if __name__ == "__main__":
    main()
