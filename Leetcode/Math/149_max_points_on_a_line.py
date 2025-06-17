# Problem: https://leetcode.com/problems/max-points-on-a-line

# Time Complexity: O(n^2) — we compare each pair of points
# Space Complexity: O(n^2) — in worst case, we store slopes for all pairs

from collections import defaultdict

def maxPoints(points):
    """
    Approach:
        - Iterate over all pairs of points and calculate the slope between them.
        - Use a hash map to count how many times a particular slope (with reference to a base point) occurs.
        - For each point as a base, track the slope it forms with every other point.
        - The maximum count of same slopes for a base point + 1 (the base point itself) is the answer.
    """
    if len(points) <= 2:
        return len(points)  # Any 2 or fewer points are trivially collinear

    out = 1  # At least 1 point always exists

    for i in range(len(points) - 1):
        slope_count = defaultdict(int)  # Reset for each base point
        for j in range(i + 1, len(points)):
            # Calculate the differences in y and x coordinates
            diff_y = points[j][1] - points[i][1]
            diff_x = points[j][0] - points[i][0]

            # Handle vertical lines (infinite slope)
            if diff_x == 0:
                slope = 'inf'
            else:
                slope = diff_y / diff_x  # Compute slope between point i and j

            # Use base point i and its slope to build a unique key
            slope_count[slope] += 1

        # Get the maximum count of points on the same line through i
        max_for_i = max(slope_count.values(), default=0)
        out = max(out, max_for_i + 1)  # +1 to include the base point itself

    return out


def main():
    # Test - 1
    points1 = [[1,1],[2,2],[3,3]]
    print(f"output-1: {maxPoints(points1)}")

    # Test - 2
    points2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(f"output-2: {maxPoints(points2)}")

if __name__ == "__main__":
    main()
