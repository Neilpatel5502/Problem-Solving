# Problem: https://leetcode.com/problems/largest-rectangle-in-histogram
# Time Complexity: O(n) – each bar is pushed and popped at most once
# Space Complexity: O(n) – for the stack

def largestRectangleArea(heights):
    """
    Approach:
        - Use a monotonic increasing stack to keep track of the bar indices and their heights.
        - For each bar:
            - If it is shorter than the bar on top of the stack, pop from the stack and calculate the area.
            - The width is determined by the difference between the current index and the index of the popped bar.
            - Always track the furthest index back where a shorter bar was last seen to preserve correct width.
        - After the main loop, process any remaining bars in the stack.
    """

    max_area = 0
    stack = []  # Stack stores (index, height)

    for i, h in enumerate(heights):
        start = i
        # Pop while current height is less than the stack top
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index  # Extend the start to where the popped bar began
        stack.append((start, h))  # Push the current bar with the earliest start

    # Process remaining bars in the stack
    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))

    return max_area


def main():
    # Test - 1
    heights1 = [2,1,5,6,2,3]
    print(f"output-1: {largestRectangleArea(heights1)}")

    # Test - 2
    heights2 = [2,4]
    print(f"output-2: {largestRectangleArea(heights2)}")

if __name__ == "__main__":
    main()
