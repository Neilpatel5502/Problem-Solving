# Problem: https://leetcode.com/problems/combinations

# Time Complexity: O(C(n, k))       # Total number of combinations is n choose k
# Space Complexity: O(k)            # Depth of recursion stack and temporary combination list

def combine(n, k):
    """
    Approach:
        - Use backtracking to generate all possible combinations of size k from numbers 1 to n.
        - Start from 1 and go up to n, adding numbers to the current combination.
        - Once the combination has k elements, add it to the output list.
        - Use recursion to explore further and backtrack to try other possibilities.


        # Tree structure for n = 4 and k = 2:
                      .
             /        |        \
            1         2         3
         / | \       / \        |
        2  3  4     3   4       4
    """
    out = []  # To store all valid combinations

    def backtrack(start, comb):
        # Base case: if combination is of size k, store a copy
        if len(comb) == k:
            out.append(comb.copy())
            return

        # Try adding numbers from 'start' to 'n'
        for i in range(start, n + 1):
            comb.append(i)          # Choose i
            backtrack(i + 1, comb)  # Recurse with next start
            comb.pop()              # Backtrack

    backtrack(1, [])  # Start backtracking with first number

    return out


def main():
    # Test - 1
    n1, k1 = 4, 2
    print(f"output-1: {combine(n1, k1)}")

    # Test - 2
    n2, k2 = 1, 1
    print(f"output-2: {combine(n2, k2)}")

if __name__ == "__main__":
    main()
