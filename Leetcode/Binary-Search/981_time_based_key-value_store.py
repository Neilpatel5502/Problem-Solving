# Problem: https://leetcode.com/problems/time-based-key-value-store/
# Time Complexity:
#   - set: O(1) — appending to list
#   - get: O(log n) — binary search over timestamps
# Space Complexity: O(n) — stores all values and timestamps for each key

class TimeMap:
    """
    Approach:
        - Use a dictionary to map each key to a list of [value, timestamp] pairs.
        - For get(key, timestamp):
            - Use binary search to find the largest timestamp <= given timestamp.
            - Return the corresponding value, or "" if no such timestamp exists.
    """

    def __init__(self):
        self.hashmap = {}  # Key -> List of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Initialize list for key if not present
        if key not in self.hashmap:
            self.hashmap[key] = []

        # Append [value, timestamp] to the list
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Get list of [value, timestamp] for the key
        out, values = "", self.hashmap.get(key, [])

        # Binary search to find rightmost timestamp <= given timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                out = values[mid][0]  # Possible candidate
                l = mid + 1           # Search further right
            else:
                r = mid - 1           # Search left

        return out


def main():
    # Test - 1
    obj = None
    output = []

    operations = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    inputs = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

    for op, args in zip(operations, inputs):
        if op == "TimeMap":
            obj = TimeMap()
            output.append(None)
        elif op == "set":
            obj.set(*args)
            output.append(None)
        elif op == "get":
            result = obj.get(*args)
            output.append(result)

    print("Output-1:", output)

if __name__ == "__main__":
    main()
