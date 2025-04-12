# Problem: https://leetcode.com/problems/min-stack/
# Time Complexity: O(1) – for all operations: push, pop, top, and getMin
# Space Complexity: O(n) – where n is the number of elements in the stack

class MinStack:
    """
    Approach:
        - Use two stacks:
            - `stack` stores all values normally.
            - `min_stack` keeps track of the minimum value at each level of the stack.
        - On push:
            - Push value to `stack`.
            - Push the minimum of (val, current min) to `min_stack`.
        - On pop:
            - Pop from both `stack` and `min_stack`.
        - On top:
            - Return the top of `stack`.
        - On getMin:
            - Return the top of `min_stack`.
    """

    def __init__(self):
        self.stack = []      # Main stack to store values
        self.min_stack = []  # Auxiliary stack to track minimum values

    def push(self, val) -> None:
        self.stack.append(val)  # Push the value to main stack
        # Push the new minimum to min_stack
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()       # Remove top from main stack
        self.min_stack.pop()   # Remove top from min stack as well

    def top(self):
        return self.stack[-1]  # Return top element of the stack

    def getMin(self):
        return self.min_stack[-1]  # Return current minimum element


def main():
    # Test - 1
    operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    inputs = [[], [-2], [0], [-3], [], [], [], []]
    output = []

    min_stack = None

    for op, val in zip(operations, inputs):
        if op == "MinStack":
            min_stack = MinStack()
            output.append(None)
        elif op == "push":
            min_stack.push(val[0])
            output.append(None)
        elif op == "pop":
            min_stack.pop()
            output.append(None)
        elif op == "top":
            output.append(min_stack.top())
        elif op == "getMin":
            output.append(min_stack.getMin())

    print(f"Output-1: {output}")

if __name__ == "__main__":
    main()
