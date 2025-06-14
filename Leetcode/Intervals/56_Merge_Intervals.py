# Problem https://leetcode.com/problems/merge-intervals

# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for storing merged intervals

def merge(intervals):
    """
    Approach:
        - First sort the intervals based on their start time.
        - Iterate through the sorted list and merge overlapping intervals.
        - If the current interval overlaps with the previous one, merge them by updating the end.
        - Otherwise, add it as a new interval to the output.
    """
    out = []

    if len(intervals) < 2:
        return intervals  # No need to merge if there's only one or zero intervals

    intervals.sort()  # Sort intervals by start time
    i = 0

    while i < len(intervals):
        start = intervals[i][0]  # Start of the current merged interval
        end = intervals[i][1]    # End of the current merged interval

        # Merge overlapping intervals
        while i + 1 < len(intervals) and end >= intervals[i + 1][0]:
            i += 1
            end = max(end, intervals[i][1])  # Extend end if overlapping

        out.append([start, end])  # Add merged interval
        i += 1

    return out

def main():
    # Test - 1
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(f"output-1: {merge(intervals1)}")

    # Test - 2
    intervals2 = [[1,4],[4,5]]
    print(f"output-2: {merge(intervals2)}")

if __name__ == "__main__":
    main()
