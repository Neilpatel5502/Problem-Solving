# Problem: https://leetcode.com/problems/container-with-most-water

# Time Complexity: O(n) – where n is the number of lines
# Space Complexity: O(1) – uses constant extra space

def maxArea(height):
    """
    Approach:
        - Use two pointers at the start and end of the array.
        - At each step, calculate the area formed by the lines at the two pointers.
        - The height of the container is the minimum of the two heights.
        - The width is the difference between the indices.
        - Move the pointer with the shorter height inward to potentially find a taller line.
        - Repeat until the pointers meet, tracking the maximum area found.
    """

    l, r = 0, len(height) - 1  # Initialize two pointers
    out = 0  # Variable to keep track of the maximum area found

    while l < r:
        # Calculate current area
        area = min(height[l], height[r]) * (r - l)
        # Update max area if current area is greater
        out = max(out, area)

        # Move the pointer at the shorter line inward
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1

    return out


def main():
    # Test - 1
    height1 = [1,8,6,2,5,4,8,3,7]
    print(f"output-1: {maxArea(height1)}")

    # Test - 2
    height2 = [1,1]
    print(f"output-2: {maxArea(height2)}")

if __name__ == "__main__":
    main()
