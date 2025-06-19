# Problem: https://leetcode.com/problems/set-matrix-zeroes

# Time Complexity: O(m * n), where m = rows and n = columns
# Space Complexity: O(k), where k = number of zero cells stored in the `zeros` list

def setZeroes(matrix):
    """
    Approach:
        - First pass: identify all cells with 0 and store their coordinates.
        - Second pass: for each zero location, set entire row and column to 0.
        - This solution uses additional space to track zero locations (not optimal).
        - In-place optimization is possible using first row and column as markers.
    """
    zeros = []                          # Store coordinates of cells with 0
    n, m = len(matrix), len(matrix[0])  # n = number of rows, m = number of columns

    # First pass: collect all positions with value 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zeros.append((i, j))

    # Second pass: set row i and column j to 0 for each zero found
    for i, j in zeros:
        for dj in range(m):
            matrix[i][dj] = 0           # Set entire row to 0

        for di in range(n):
            matrix[di][j] = 0           # Set entire column to 0


def main():
    # Test - 1
    matrix1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    setZeroes(matrix1)
    print(f"output-1: {matrix1}")

    # Test - 2
    matrix2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    setZeroes(matrix2)
    print(f"output-2: {matrix2}")

if __name__ == "__main__":
    main()
