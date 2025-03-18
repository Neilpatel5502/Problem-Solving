# Problem Link: https://leetcode.com/problems/count-primes/

# Time Complexity: O(n log n)   init of prime takes n and log n to loop through root of n.
# Space Complexity: O(n)        because of primes list.

def countPrimes(n):
    """
    Approach:
        - Create a boolean array `primes` where primes[i] is True if `i` is prime.
        - return 0 if n < 3 because for n = 2 output should be 0 because 0 and 1 are not prime.
        - Iterate from 2 to sqrt(right_limit) and mark multiples of prime as non-prime.
        - Return the count of True indicates a count of prime numbers.
    """
    if n < 3:
        return 0

    primes = [True] * (n)           # Assume all numbers are prime initially
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        # If i is prime, mark its multiples as non-prime
        if primes[i]:
            for mul in range(i*i, n, i):
                primes[mul] = False

    return primes.count(True)


def main():
    # Test - 1
    n1 = 10
    print(f"output-1: {countPrimes(n1)}")

    # Test - 2
    n2 = 0
    print(f"output-2: {countPrimes(n2)}")

    # Test - 3
    n3 = 1
    print(f"output-3: {countPrimes(n3)}")


if __name__ == "__main__":
    main()
