# Problem: https://leetcode.com/problems/sqrtx

# Time Complexity: O(log x) – binary search reduces the range each time
# Space Complexity: O(1)

def mySqrt(x):
    """
    Approach:
        - Use binary search to find the integer square root of `x`.
        - The answer lies between 1 and x for x ≥ 1.
        - For each mid, check if mid^2 == x. If yes, return mid.
        - If mid^2 < x, search right half; else search left half.
        - If exact square is not found, return `right`, which is the floor of sqrt(x).
    """
    if x < 2:
        return x  # Edge case: sqrt(0) = 0, sqrt(1) = 1

    left, right = 1, x

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == x:
            return mid                      # Exact square root found
        elif mid * mid < x:
            left = mid + 1                  # Search right half
        else:
            right = mid - 1                 # Search left half

    return right  # Floor of sqrt(x) if no exact square found


def main():
    # Test - 1
    x1 = 4
    print(f"output-1: {mySqrt(x1)}")

    # Test - 2
    x2 = 8
    print(f"output-2: {mySqrt(x2)}")

if __name__ == "__main__":
    main()
