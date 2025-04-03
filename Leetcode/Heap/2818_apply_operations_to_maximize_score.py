# Problem Link: https://leetcode.com/problems/apply-operations-to-maximize-score

# Time Complexity: O(N log N), where N is the length of nums, due to heap operations and prime factorization.
# Space Complexity: O(N)

from math import sqrt
from heapq import heapify, heappop

def maximumScore(nums, k):
    """
    Approach:
        - Compute the prime score for each element in nums (number of distinct prime factors).
        - Use a monotonic stack to determine left and right boundaries for each element where it remains the maximum prime score.
        - Use a max heap to process elements with the highest prime score first.
        - For each element, determine the number of valid subarrays it appears in and apply the operation optimally.
        - Multiply the score with selected numbers while ensuring k operations are performed.
    """

    N = len(nums)
    MOD = 10**9 + 7     # Modulo value for large numbers
    out = 1

    # Compute prime scores (number of distinct prime factors) for each number in nums
    prime_scores = []
    for n in nums:
        score = 0
        for f in range(2, int(sqrt(n)) + 1):
            if n % f == 0:
                score += 1
                while n % f == 0:
                    n = n // f      # Remove all occurrences of this factor

        # If there's a prime factor left, count it
        if n >= 2:
            score += 1

        prime_scores.append(score)

    # Determine left and right boundaries for elements
    left_bound = [-1] * N
    right_bound = [N] * N


    stack = []
    for i, s in enumerate(prime_scores):
        # Maintain a decreasing stack based on prime scores
        while stack and prime_scores[stack[-1]] < s:
            index = stack.pop()
            right_bound[index] = i      # Set right boundary for popped element
        if stack:
            left_bound[i] = stack[-1]   # Set left boundary
        stack.append(i)

    # Use a max heap to process elements in decreasing order of value
    heap = [(-n, i) for i, n in enumerate(nums)]    # Store negative values for max heap
    heapify(heap)

    # Process k operations
    while k > 0:
        n, index = heappop(heap)    # Get max value element
        n = -n
        score = prime_scores[index]

        # Compute the number of subarrays where this number is the highest prime score
        left_cnt = index - left_bound[index]
        right_cnt = right_bound[index] - index
        count = left_cnt * right_cnt

        operations = min(count, k)                      # Perform as many operations as allowed
        out = (out * pow(n, operations, MOD)) % MOD     # Update score with modulo
        k -= operations

    return out


def main():
    # Test - 1
    nums1 = [8,3,9,3,8]
    k1 = 2
    print(f"output-1: {maximumScore(nums1, k1)}")

    # Test - 2
    nums2 = [19,12,14,6,10,18]
    k2 = 3
    print(f"output-2: {maximumScore(nums2, k2)}")

if __name__ == "__main__":
    main()
