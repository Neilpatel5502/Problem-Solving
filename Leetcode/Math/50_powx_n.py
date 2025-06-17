# Problem: https://leetcode.com/problems/powx-n

# Time Complexity: O(log n) – due to recursive divide-and-conquer
# Space Complexity: O(log n) – recursion stack depth

def myPow(x, n):
    """
    Approach:
        - Use recursive fast exponentiation (divide-and-conquer).
        - For each call, recursively compute x^(n // 2), then square the result.
        - If n is even: x^n = (x^(n//2))^2
        - If n is odd:  x^n = x * (x^(n//2))^2
        - Handle negative exponents by inverting the result (1 / x^|n|).
        - Base cases:
            - If x == 0 → return 0
            - If n == 0 → return 1 (any number to power 0 is 1)
    """
    def helper(x, n):
        if x == 0:
            return 0        # 0 to any power is 0
        if n == 0:
            return 1        # Any number to power 0 is 1

        out = helper(x, n // 2)
        out = out * out     # Square the result

        return x * out if n % 2 else out  # If odd, multiply once more by x

    out = helper(x, abs(n))

    return out if n >= 0 else 1 / out  # Handle negative exponent


def main():
    # Test - 1
    x1, n1 = 2.0, 10
    print(f"output-1: {myPow(x1, n1)}")

    # Test - 2
    x2, n2 = 2.1, 3
    print(f"output-2: {myPow(x2, n2)}")

    # Test - 3
    x3, n3 = 2.0, -2
    print(f"output-3: {myPow(x3, n3)}")

if __name__ == "__main__":
    main()
