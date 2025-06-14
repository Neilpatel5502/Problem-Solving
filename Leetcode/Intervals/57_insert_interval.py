# Problem: https://leetcode.com/problems/insert-interval

# Time Complexity: O(n), where n = number of intervals
# Space Complexity: O(n) for the output list

def insert(intervals, newInterval):
    """
    Approach:
        - Iterate through the existing intervals and compare with newInterval:
            - If newInterval is before the current interval, insert it and return merged result.
            - If newInterval is after the current interval, keep adding intervals to output.
            - If overlapping, merge newInterval with current interval.
        - After the loop, append the (possibly merged) newInterval to output.
    """
    out = []

    for i in range(len(intervals)):
        # Case 1: newInterval comes before the current interval (no overlap)
        if newInterval[1] < intervals[i][0]:
            out.append(newInterval)
            return out + intervals[i:]  # Append the rest of intervals

        # Case 2: newInterval comes after the current interval (no overlap)
        elif newInterval[0] > intervals[i][1]:
            out.append(intervals[i])

        # Case 3: Overlapping intervals, update newInterval to merged interval
        else:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])
            ]

    # Append the final merged newInterval
    out.append(newInterval)

    return out

def main():
    # Test - 1
    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]
    print(f"output-1: {insert(intervals1, newInterval1)}")

    # Test - 2
    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]
    print(f"output-2: {insert(intervals2, newInterval2)}")

if __name__ == "__main__":
    main()
