# Problem Link: https://leetcode.com/problems/count-total-number-of-colored-cells

# Time Complexity: O(n)
# Space Complexity: O(1)

def coloredCells(n):
    """
    Approach:
        - If n is 1 then output is 1, now for subsequent n values it is simple
        math to (n - 1)'s output + 4 * n.
    """

    if n == 1:
        return 1

    # Set prev val is 1 intially.
    prev = 1

    # Loop through 1 to n and calculate output for each i till n.
    for i in range(1, n):
        prev = prev + 4 * i

    return prev


def main():
    # Test - 1
    n1 = 1
    print(f"output-1: {coloredCells(n1)}")

    # Test - 2
    n2 = 2
    print(f"output-2: {coloredCells(n2)}")

    # Test - 3
    n3 = 3
    print(f"output-3: {coloredCells(n3)}")


if __name__ == "__main__":
    main()
