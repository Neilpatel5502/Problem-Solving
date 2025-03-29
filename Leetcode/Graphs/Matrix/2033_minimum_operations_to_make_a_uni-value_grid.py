# Problem Link: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid

# Time Complexity: O(m*n log(m*n))      m = number of rows and n = number of cols
# Space Complexity: O(m * n)

def minOperations(grid, x):
    """
    Approach:
        - Check if all elements have the same remainder when divided by x. If not, return -1.
        - Flatten the grid into a sorted list and find the median.
        - The median minimizes the total operations required to make all elements equal.
        - Calculate the number of operations needed to convert each element to the median.
    """

    # Check if it's possible to make all elements the same
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] % x != grid[0][0] % x:
                return -1       # Not possible to make the grid uni-value

    # Flatten the grid into a sorted list
    nums = sorted([n for row in grid for n in row])
    median = nums[len(nums) // 2]       # Find the median value

    # Calculate the minimum operations needed
    out = 0
    for n in nums:
        out += abs((n - median) // x)   # Number of steps needed to reach the median

    return out


def main():
    # Test - 1
    grid1 = [[2,4],[6,8]]
    x1 = 2
    print(f"output-1: {minOperations(grid1, x1)}")

    # Test - 2
    grid2 = [[1,5],[2,3]]
    x2 = 1
    print(f"output-2: {minOperations(grid2, x2)}")

    # Test - 3
    grid3 = [[1,2],[3,4]]
    x3 = 2
    print(f"output-2: {minOperations(grid3, x3)}")

if __name__ == "__main__":
    main()
