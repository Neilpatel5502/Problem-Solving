# Problem Link: https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections

# Time complexity: O(n log n)
# Space complexity: O(n)

def checkValidCuts(n, rectangles):
    """
    Approach:
        - Extract x and y coordinate ranges for each rectangle.
        - Sort the intervals by their starting coordinates.
        - Define a function to count distinct sections in a sorted list of intervals.
            - Iterate through intervals, tracking the previous end coordinate.
            - If a new interval starts after the previous end, it forms a new section.
        - Check if either horizontal (x) or vertical (y) cuts create at least 3 sections.
        - Return True if at least 3 sections are found, otherwise return False.
    """

    # Extract x and y coordinate ranges from rectangles
    x = [(r[0], r[2]) for r in rectangles]
    y = [(r[1], r[3]) for r in rectangles]

    # Sort intervals by their starting coordinates
    x.sort()
    y.sort()

    # Function to count distinct sections formed by non-overlapping intervals
    def check(intervals):
        count = 0
        prev_end = -1

        for start, end in intervals:
            if prev_end <= start:
                count += 1

            prev_end = max(end, prev_end)
        return count

    return max(check(x),check(y)) >= 3


def main():
    # Test - 1
    n1 = 5
    rectangles1 = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
    print(f"output-1: {checkValidCuts(n1, rectangles1)}")

    # Test - 2
    n2 = 4
    rectangles2 = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
    print(f"output-2: {checkValidCuts(n2, rectangles2)}")

    # Test - 3
    n3 = 4
    rectangles3 = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
    print(f"output-2: {checkValidCuts(n3, rectangles3)}")

if __name__ == "__main__":
    main()
