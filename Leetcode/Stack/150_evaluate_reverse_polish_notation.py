# Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation
# Time Complexity: O(n) – where n is the number of tokens
# Space Complexity: O(n) – for storing operands on the stack

def evalRPN(tokens):
    """
    Approach:
        - Use a stack to store intermediate results.
        - Iterate over each token in the input:
            - If the token is an operator (+, -, *, /):
                - Pop the top two elements from the stack.
                - Apply the operator with correct operand order.
                - Push the result back onto the stack.
            - If the token is a number, convert to int and push to stack.
        - After processing all tokens, the result will be the only element in the stack.
    """

    stack = []

    for i in tokens:
        if i == "+":
            stack.append(stack.pop() + stack.pop())  # Add top two numbers
        elif i == "*":
            stack.append(stack.pop() * stack.pop())  # Multiply top two numbers
        elif i == "/":
            exp2 = stack.pop()
            exp1 = stack.pop()
            stack.append(int(exp1 / exp2))  # Truncate division toward zero
        elif i == "-":
            exp2 = stack.pop()
            exp1 = stack.pop()
            stack.append(exp1 - exp2)  # Subtract in correct order
        else:
            stack.append(int(i))  # Push number onto the stack

    return stack[0]


def main():
    # Test - 1
    tokens1 = ["2", "1", "+", "3", "*"]
    print(f"output-1: {evalRPN(tokens1)}")

    # Test - 2
    tokens2 = ["4", "13", "5", "/", "+"]
    print(f"output-2: {evalRPN(tokens2)}")

    # Test - 3
    tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(f"output-3: {evalRPN(tokens3)}")

if __name__ == "__main__":
    main()
