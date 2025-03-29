# Problem Link: https://leetcode.com/problems/maximum-number-of-points-from-grid-queries

# Time Complexity: O(m*n log(m * n) + q log q)      where m, n are grid dimensions and q is query length.
# Space Complexity: O(m * n)

from heapq import heappush, heappop

def maxPoints(grid, queries):
    """
    Approach:
        - Sort the queries in ascending order and keep track of their original indices.
        - Use a min-heap to explore the grid starting from the top-left cell.
        - Expand to neighboring cells when the current query value is greater than the cell value.
        - Keep track of visited cells to avoid redundant processing.
        - Store results based on the original order of queries.

    Time Complexity: O(m * n log(m * n) + k log k) where m, n are grid dimensions and k is query length.
    """

    rows, cols = len(grid), len(grid[0])

    # Pair queries with their original indices and sort them in ascending order
    q = [(num, idx) for idx, num in enumerate(queries)]
    q.sort()

    # Min-heap to store grid cells (value, row, col)
    heap = [(grid[0][0], 0, 0)]
    out = [0] * len(queries)
    visited = set([(0, 0)])             # Set to track visited cells
    count = 0                           # Counter for points collected

    # Process each query in sorted order
    for number, index in q:
        # Expand the grid while the top of the heap is less than the current query value
        while heap and heap[0][0] < number:
            value, r, c = heappop(heap)
            count += 1

            # Define 4 possible movement directions
            neighbors = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for nr, nc in neighbors:
                # Check if the new position is within grid bounds and not visited
                if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited):
                    heappush(heap, (grid[nr][nc], nr, nc))
                    visited.add((nr, nc))

        # Store the result for the current query in original index
        out[index] = count

    return out


def main():
    # Test - 1
    grid1 = [[1,2,3],[2,5,7],[3,5,1]]
    queries1 = [5,6,2]
    print(f"output-1: {maxPoints(grid1, queries1)}")

    # Test - 2
    grid2 = [[5,2,1],[1,1,2]]
    queries2 = [3]
    print(f"output-2: {maxPoints(grid2, queries2)}")


if __name__ == "__main__":
    main()
