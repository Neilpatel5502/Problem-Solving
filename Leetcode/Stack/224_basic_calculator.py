# Problem: https://leetcode.com/problems/basic-calculator

# Time Complexity: O(n), where n = length of the input string
# Space Complexity: O(n), for the stack

def calculate(s):
    """
    Approach:
        - Use a stack to manage results and signs for sub-expressions inside parentheses.
        - Use `out` to keep the ongoing result, `num` to build multi-digit numbers,
          and `sign` to track whether the current number is positive or negative.
        - When encountering '(', push the current result and sign to the stack and reset them.
        - When encountering ')', finalize the expression inside the parentheses using the stack.
        - At the end, apply any remaining number to the result.
    """
    stack = []
    num = 0       # To store the current number
    sign = 1      # 1 for '+', -1 for '-'
    out = 0       # Cumulative result

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)  # Build multi-digit numbers

        elif ch == "+":
            out += sign * num  # Add previous number with its sign
            num = 0
            sign = 1           # Update sign for next number

        elif ch == "-":
            out += sign * num
            num = 0
            sign = -1

        elif ch == "(":
            # Save the current result and sign before '('
            stack.append(out)
            stack.append(sign)
            out, sign = 0, 1   # Reset for inner expression

        elif ch == ")":
            out += sign * num  # Finalize value inside parentheses
            num = 0
            out *= stack.pop()  # Apply sign before '('
            out += stack.pop()  # Add value before '('

    return out + sign * num  # Add last number (if any)

def main():
    # Test - 1
    expr1 = "1 + 1"
    print(f"output-1: {calculate(expr1)}")

    # Test - 2
    expr2 = " 2-1 + 2 "
    print(f"output-2: {calculate(expr2)}")

    # Test - 3
    expr3 = "(1+(4+5+2)-3)+(6+8)"
    print(f"output-3: {calculate(expr3)}")

if __name__ == "__main__":
    main()
