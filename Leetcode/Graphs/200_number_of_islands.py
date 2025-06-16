# Problem: https://leetcode.com/problems/number-of-islands

# Time Complexity: O(m * n)           # Each cell is visited once
# Space Complexity: O(m * n)          # Recursion stack in worst case

def numIslands(grid):
    """
    Approach:
        - Use Depth-First Search (DFS) to traverse each island.
        - Iterate over every cell in the grid.
        - When a land cell ('1') is found, initiate a DFS to mark all connected land as visited.
        - Convert visited land cells to '0' to avoid revisiting.
        - Increment the island count for each DFS call triggered from an unvisited land cell.
    """
    m, n = len(grid), len(grid[0])
    out = 0                           # Count of islands

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
            return                    # Return if out of bounds or water

        grid[r][c] = "0"              # Mark current land cell as visited

        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r, c + 1)
        dfs(r - 1, c)
        dfs(r, c - 1)

    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":     # Found unvisited land
                dfs(r, c)             # Visit entire island
                out += 1              # Increment island count

    return out


def main():
    # Test - 1
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(f"output-1: {numIslands([row[:] for row in grid1])}")

    # Test - 2
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"output-2: {numIslands([row[:] for row in grid2])}")

if __name__ == "__main__":
    main()
