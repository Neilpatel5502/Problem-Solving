# Problem link: https://leetcode.com/problems/count-days-without-meetings

# Time Complexity: O(n log n)        popping all meetings takes O(n log n)
# Space Complexity: O(n)

from heapq import heapify, heappop, heappush

def countDays(days, meetings):
    """
    Approach:
        - Use a min-heap to process meetings in ascending order of start days.
        - Track the latest end day of meetings to avoid double-counting overlapping days.
        - Subtract the number of busy days from the total available days to get free days.
    """
    # Convert the meetings list into a min-heap (sorted by start day)
    heapify(meetings)
    out = days
    latest_end_day = 0          # Keeps track of the latest meeting end day

    # Process all meetings in order
    while meetings:
        start, end = heappop(meetings)
        busy_days = end - start + 1             # Total days occupied by this meeting

        # Avoid overlapping meetings
        if latest_end_day >= end:
            continue
        elif latest_end_day >= start:
            busy_days = end - latest_end_day    # Adjust busy days if overlapping partially

        latest_end_day = end
        out -= busy_days                        # Subtract busy days from available days

    return out


def main():
    # Test - 1
    days1 = 10
    meetings1 = [[5,7],[1,3],[9,10]]
    print(f"output-1: {countDays(days1, meetings1)}")

    # Test - 2
    days2 = 5
    meetings2 = [[2,4],[1,3]]
    print(f"output-2: {countDays(days2, meetings2)}")

    # Test - 3
    days3 = 6
    meetings3 = [[1,6]]
    print(f"output-2: {countDays(days3, meetings3)}")

if __name__ == "__main__":
    main()
