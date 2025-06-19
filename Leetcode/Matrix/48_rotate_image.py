# Problem: https://leetcode.com/problems/rotate-image

# Time Complexity: O(n^2), where n is the number of rows/columns
# Space Complexity: O(1), in-place transformation

def rotate(matrix):
    """
    Approach:
        - The rotation can be done in two steps:
            1. Transpose the matrix: swap elements across the main diagonal
               This converts rows into columns.
            2. Reverse each row: this aligns the elements as if rotated 90 degrees clockwise
        - Both steps are performed in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix — convert rows to columns
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row — simulate 90° clockwise rotation
    for row in matrix:
        row.reverse()


def main():
    # Test - 1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate(matrix1)
    print(f"output-1: {matrix1}")

    # Test - 2
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    rotate(matrix2)
    print(f"output-2: {matrix2}")

if __name__ == "__main__":
    main()
