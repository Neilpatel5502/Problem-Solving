# Problem Link: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three

# Time Complexity: O(log n)
# Space Complexity: O(1)

def checkPowersOfThree(n):
    """
    Approach:
        - Divide n by three util it becomes 0. Here we only want reminder 0 or 1.
        because 0 is divisable by 3 means 3^1 and 1 = 3^0, but we cannot represnt 2
        for any 3 power.
    """

    # Loop until n becomes 0.
    while n!=0:
        rem = n%3   # Calculate reminder by dividing n by 3.

        if rem==2:          # If rem is 2 return False.
            return False

        n = n//3    # Update n with n divide by 3.

    # All things works out return True.
    return True


def main():
    # Test - 1
    n1 = 12
    print(f"output-1: {checkPowersOfThree(n1)}")

    # Test - 2
    n2 = 91
    print(f"output-2: {checkPowersOfThree(n2)}")

    # Test - 3
    n3 = 21
    print(f"output-3: {checkPowersOfThree(n3)}")


if __name__ == "__main__":
    main()
