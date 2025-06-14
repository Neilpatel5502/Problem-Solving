# Problem: https://leetcode.com/problems/candy

# Time Complexity: O(n)
# Space Complexity: O(n)

def candy(ratings):
    """
    Approach:
        - Each child must have at least one candy.
        - Children with a higher rating than their immediate neighbors must get more candies.
        - Step 1: Traverse left to right to ensure the right child gets more if rated higher than the left.
        - Step 2: Traverse right to left to ensure the left child gets more if rated higher than the right.
        - Track candies in an array `out`, initialized to 1 (minimum one candy per child).
        - The final result is the sum of candies in `out`.
    """
    n = len(ratings)
    out = [1] * n  # Every child gets at least one candy

    # Traverse from left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            out[i] = out[i - 1] + 1

    # Traverse from right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            out[i] = max(out[i], out[i + 1] + 1)

    return sum(out)

def main():
    # Test - 1
    ratings1 = [1, 0, 2]
    print(f"output-1: {candy(ratings1)}")

    # Test - 2
    ratings2 = [1, 2, 2]
    print(f"output-2: {candy(ratings2)}")

if __name__ == "__main__":
    main()
