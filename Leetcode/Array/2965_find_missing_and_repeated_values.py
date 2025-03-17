# Problem Link: https://leetcode.com/problems/find-missing-and-repeated-values

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

def findMissingAndRepeatedValues(grid):
    """
    Approach:
        - In this problem we can simply take a counter map and count the values
        of number appears in grid and check which number has exactly 2 count and 0 count.
    """

    n = len(grid)
    count = {i:0 for i in range(1, (n**2) + 1)}
    out = [0, 0]

    # Loop through grid and increment count for each cell number
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            count[grid[row][col]] += 1

    # Loop through count map and check for count 2 and 0.
    for i, c in count.items():
        if c == 2:
            out[0] = i
        if c == 0:
            out[1] = i

    return out


def main():
    # Test - 1
    grid1 = [[1,3],[2,2]]
    print(f"output-1: {findMissingAndRepeatedValues(grid1)}")

    # Test - 2
    grid2 = [[9,1,7],[8,9,2],[3,4,6]]
    print(f"output-2: {findMissingAndRepeatedValues(grid2)}")

if __name__ == "__main__":
    main()
