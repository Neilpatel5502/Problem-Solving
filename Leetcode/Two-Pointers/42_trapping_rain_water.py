# Problem: https://leetcode.com/problems/trapping-rain-water/
# Time Complexity: O(n) – single pass through the array using two pointers
# Space Complexity: O(1) – constant extra space used

def trap(height):
    """
    Approach:
        - Use two pointers (`l` and `r`) starting from both ends of the height array.
        - Keep track of the maximum height seen so far from the left (`leftMax`) and from the right (`rightMax`).
        - At each step:
            - Move the pointer pointing to the smaller max height.
            - For that pointer, update the max height and calculate trapped water as `maxHeight - height[i]`.
        - Continue until the two pointers meet.
    """

    if not height:
        return 0  # No bars, no water

    l, r = 0, len(height) - 1  # Initialize two pointers
    leftMax, rightMax = height[l], height[r]  # Track max height seen from both ends
    out = 0  # Accumulator for total trapped water

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])  # Update left max
            out += leftMax - height[l]  # Water trapped at index l
        else:
            r -= 1
            rightMax = max(rightMax, height[r])  # Update right max
            out += rightMax - height[r]  # Water trapped at index r

    return out


def main():
    # Test - 1
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"output-1: {trap(height1)}")

    # Test - 2
    height2 = [4,2,0,3,2,5]
    print(f"output-2: {trap(height2)}")

if __name__ == "__main__":
    main()
