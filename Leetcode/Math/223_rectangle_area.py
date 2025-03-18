# Problem Link: https://leetcode.com/problems/rectangle-area/

# Time Complexity: O(1)
# Space Complexity: O(1)

def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    """
    Approach:
        - Calculate the area of both rectangles separately.
        - Determine the overlapping area between the two rectangles.
        - Subtract the overlapping area from the sum of both rectangle areas.
    """

    # Calculate the area of the first rectangle.
    # The width is (ax2 - ax1) and the height is (ay2 - ay1).
    rect1 = (ax2 - ax1) * (ay2 - ay1)

    # Calculate the area of the second rectangle.
    # The width is (bx2 - bx1) and the height is (by2 - by1).
    rect2 = (bx2 - bx1) * (by2 - by1)

    # Determine the width of the overlapping region.
    # The overlap occurs between max(ax1, bx1) and min(ax2, bx2).
    overlap_x = max(min(ax2, bx2) - max(ax1, bx1), 0)

    # Determine the height of the overlapping region.
    # The overlap occurs between max(ay1, by1) and min(ay2, by2).
    overlap_y = max(min(by2, ay2) - max(by1, ay1), 0)

    overlap = overlap_x * overlap_y

    return rect1 + rect2 - overlap


def main():
    # Test - 1
    ax1_1 = -3
    ay1_1 = 0
    ax2_1 = 3
    ay2_1 = 4
    bx1_1 = 0
    by1_1 = -1
    bx2_1 = 9
    by2_1 = 2

    print(f"output-1: {computeArea(ax1_1, ay1_1, ax2_1, ay2_1, bx1_1, by1_1, bx2_1, by2_1)}")

    # Test - 2
    ax1_2 = -2
    ay1_2 = -2
    ax2_2 = 2
    ay2_2 = 2
    bx1_2 = -2
    by1_2 = -2
    bx2_2 = 2
    by2_2 = 2

    print(f"output-2: {computeArea(ax1_2, ay1_2, ax2_2, ay2_2, bx1_2, by1_2, bx2_2, by2_2)}")


if __name__ == "__main__":
    main()
