# Problem: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

# Time Complexity: O(n log n), due to sorting
# Space Complexity: O(1)

def findMinArrowShots(points):
    """
    Approach:
        - Each balloon is represented by an interval [start, end].
        - To burst the maximum number of balloons with one arrow, we sort intervals by their end points.
        - Greedily shoot an arrow at the end of the first balloon.
        - If the next balloon starts after the current arrow's end, we need another arrow.
        - Otherwise, it's already burst by the current arrow.
    """

    points.sort(key=lambda x: x[1])  # Sort by end coordinate
    out = 1                          # At least one arrow is needed
    end = points[0][1]               # Initial arrow position

    for i in range(1, len(points)):
        if points[i][0] > end:
            out += 1                # New arrow needed
            end = points[i][1]      # Update arrow position to new balloon's end

    return out

def main():
    # Test - 1
    points1 = [[10,16],[2,8],[1,6],[7,12]]
    print(f"output-1: {findMinArrowShots(points1)}")

    # Test - 2
    points2 = [[1,2],[3,4],[5,6],[7,8]]
    print(f"output-2: {findMinArrowShots(points2)}")

    # Test - 3
    points3 = [[1,2],[2,3],[3,4],[4,5]]
    print(f"output-3: {findMinArrowShots(points3)}")

if __name__ == "__main__":
    main()
