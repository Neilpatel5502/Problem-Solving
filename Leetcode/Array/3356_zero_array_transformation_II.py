# Problem Link: https://leetcode.com/problems/zero-array-transformation-ii

# Time Complexity: O(n + m) -> n is len of nums and m is len queries.
# Space Complexity: O(n) -> We are using temp.

def minZeroArray(nums, queries):
    """
    Approach:
        - This function tries to reduce all elements in `nums` to zero using a set of queries.
        - Each query `[left, right, value]` increases the elements in `temp` from index `left` to `right` by `value`.
        - The function implements a difference array technique (`temp` array) to efficiently apply range updates.
    Steps:
        1. Initialize `temp` to track the cumulative effect of applied queries.
        2. Iterate through `nums` and check if the current element can be reduced to zero using the accumulated effect.
        3. If more reduction is needed, apply a new query from `queries` and update the `temp` array.
        4. If queries run out before reducing `nums` to zero, return `-1`.
        5. Otherwise, return the number of queries used.
    """
    n = len(nums)
    temp = [0] * (n + 1)    # Difference array for efficient range updates
    k = 0                   # Number of queries used
    count = 0               # Accumulated sum from temp array

    for i in range(n):
        # Ensure nums[i] is reduced to zero
        while count + temp[i] < nums[i]:
            # If no more queries are available, return -1
            if len(queries) == k:
                return -1

            # Get the current query
            left, right, value = queries[k]

            # Increment the query count
            k += 1

            # If right pointer is out of bound nothing to check.
            if right < i:
                continue

            # Increment value at current index basically i if i less than left then left.
            temp[max(left, i)] += value

            # Reduce the right + 1 to restrict calculation in range. In the next queries we
            # have to plus the negative values and then we can get updated count of k. if
            # accumulated sum less than any value in next quries, otherwise loop will not run further.
            temp[right + 1] -= value

        count += temp[i]    # Update the accumulated effect

    return k

def main():
    # Test - 1
    nums1 = [2,0,2]
    queries1 = [[0,2,1],[0,2,1],[1,1,3]]
    print(f"output-1: {minZeroArray(nums1, queries1)}")

    # Test - 2
    nums2 = [4,3,2,1]
    queries2 = [[1,3,2],[0,2,1]]
    print(f"output-2: {minZeroArray(nums2, queries2)}")

    # Test - 3
    nums3 = [0]
    queries3 = [[0,0,2],[0,0,4],[0,0,4],[0,0,3],[0,0,5]]
    print(f"output-3: {minZeroArray(nums3, queries3)}")

if __name__ == "__main__":
    main()
