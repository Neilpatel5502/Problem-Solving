# Problem Link: https://leetcode.com/problems/closest-prime-numbers-in-range

# Time Complexity: O(n log n)   where n is right.
# Space Complexity: O(n)        because of primes_list.

def helper(right_limit):
    """
    Approach:
        - Create a boolean array `primes` where primes[i] is True if `i` is prime.
        - Mark 0 and 1 as False since they are not prime.
        - Iterate from 2 to sqrt(right_limit) and mark multiples as non-prime.
        - Return the boolean prime list where True indicates a prime number.
    """
    primes = [True] * (right_limit + 1)     # Assume all numbers are prime initially
    primes[0] = primes[1] = False

    for i in range(2, int(right_limit**0.5) + 1):
        # If i is prime, mark its multiples as non-prime
        if primes[i]:
            for mul in range(i*i, right_limit + 1, i):
                primes[mul] = False

    return primes


def closestPrimes(left, right):
    """
    Approach:
        - Generate prime numbers up to `right` using the helper function.
        - Filter out primes within the given range [left, right].
        - If there are fewer than 2 primes, return [-1, -1].
        - Iterate through the list of primes and find the pair with the smallest difference.
    """
    primes_list = helper(right)    # Get the boolean list of prime numbers

    # Extract prime numbers within the given range [left, right]
    primes = [
        num for num in range(left, right + 1) if primes_list[num]
    ]

    # If fewer than 2 primes exist, return [-1, -1] as no valid pair can be found
    if len(primes) < 2:
        return [-1, -1]

    # Initialize variables to track the closest prime pair
    diff = float('inf')
    output = [0, 0]

    # Iterate through the list of primes to find the closest pair
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] < diff:    # Check if the difference is the smallest so far
            output[0] = primes[i]
            output[1] = primes[i + 1]
            diff = primes[i + 1] - primes[i]    # Update the minimum difference

    return output


def main():
    # Test - 1
    left1 = 10
    right1 = 19
    print(f"output-1: {closestPrimes(left1, right1)}")

    # Test - 2
    left2 = 4
    right2 = 6
    print(f"output-2: {closestPrimes(left2, right2)}")


if __name__ == "__main__":
    main()
