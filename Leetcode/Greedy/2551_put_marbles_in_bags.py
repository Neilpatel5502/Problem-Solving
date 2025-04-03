# Problem Link: https://leetcode.com/problems/put-marbles-in-bags

# Time Complexity: O(n log n)
# Space Complexity: O(n)

def putMarbles(weights, k):
    """
    Approach:
        - Compute the possible bag costs by summing adjacent elements in weights.
        - Sort these computed costs to easily extract the minimum and maximum sums.
        - To get the maximum score, pick the largest (k-1) values.
        - To get the minimum score, pick the smallest (k-1) values.
        - The difference between these two sums gives the final result.
    """

    # Compute pairwise sums of adjacent elements
    n = len(weights) - 1
    weights = [weights[i] + weights[i + 1] for i in range(n)]

    # Sort the pairwise sums
    weights.sort()

    res = 0

    # Calculate the difference between the sum of the largest (k-1) and smallest (k-1) values
    for i in range(k - 1):
        res += weights[-1 - i] - weights[i]     # Max values minus min values

    return res


def main():
    # Test - 1
    weights1 = [1,3,5,1]
    k1 = 2
    print(f"output-1: {putMarbles(weights1, k1)}")

    # Test - 2
    weights2 = [1,3]
    k2 = 2
    print(f"output-2: {putMarbles(weights2, k2)}")

if __name__ == "__main__":
    main()
