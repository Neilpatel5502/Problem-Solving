# Problem: https://leetcode.com/problems/generate-parentheses
# Time Complexity: O(2^2n) in the worst case, but only valid combinations are generated – actual time is Catalan number C(n) ~ O(4^n / sqrt(n))
# Space Complexity: O(n) for recursion stack and building each string

def generateParenthesis(n):
    """
    Approach:
        - Use backtracking to generate valid sequences.
        - Maintain counters for open and close brackets used so far.
        - Rules:
            - You can add '(' if openB < n.
            - You can add ')' if closeB < openB (to ensure balance).
        - When both counters reach n, add the current string to the result list.

                    .
                    |
                    |
                  ['(']
                |       |
              ['((']  ['()']
    """

    out = []   # To store final valid parentheses combinations
    stack = [] # Temporary stack to build current string

    def backtrack(openB, closeB):
        # If both open and close brackets are used up, it's a valid combo
        if openB == closeB == n:
            out.append("".join(stack))
            return

        # Add '(' if we still have open brackets left
        if openB < n:
            stack.append('(')
            backtrack(openB + 1, closeB)
            stack.pop()

        # Add ')' if it won't unbalance the expression
        if closeB < openB:
            stack.append(')')
            backtrack(openB, closeB + 1)
            stack.pop()

    backtrack(0, 0)
    return out


def main():
    # Test - 1
    n1 = 3
    print(f"output-1: {generateParenthesis(n1)}")

    # Test - 2
    n2 = 1
    print(f"output-2: {generateParenthesis(n2)}")

if __name__ == "__main__":
    main()
