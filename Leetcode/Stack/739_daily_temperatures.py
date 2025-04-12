# Problem: https://leetcode.com/problems/daily-temperatures/
# Time Complexity: O(n) – each index is pushed and popped at most once from the stack
# Space Complexity: O(n) – for the output list and the stack

def dailyTemperatures(temperatures):
    """
    Approach:
        - Use a monotonic decreasing stack to track temperatures and their indices.
        - Traverse the list:
            - For each temperature, check if it's warmer than the temperature on top of the stack.
            - If it is, pop from the stack and record the number of days waited in the result list.
            - Continue this until the stack is empty or current temp is not warmer.
        - Push current temperature and index onto the stack.
        - Initialize result list with 0s as default for days that never get warmer.
    """

    out = [0] * len(temperatures)  # Result array initialized with 0s
    stack = []  # Monotonic stack storing [temperature, index]

    for i, t in enumerate(temperatures):
        # Compare current temperature with top of the stack
        while stack and t > stack[-1][0]:
            stack_t, stack_i = stack.pop()
            out[stack_i] = i - stack_i  # Days waited for a warmer temperature
        # Push current day's temperature and index onto the stack
        stack.append((t, i))

    return out


def main():
    # Test - 1
    temps1 = [73,74,75,71,69,72,76,73]
    print(f"output-1: {dailyTemperatures(temps1)}")

    # Test - 2
    temps2 = [30,40,50,60]
    print(f"output-2: {dailyTemperatures(temps2)}")

    # Test - 3
    temps3 = [30,60,90]
    print(f"output-3: {dailyTemperatures(temps3)}")

if __name__ == "__main__":
    main()
