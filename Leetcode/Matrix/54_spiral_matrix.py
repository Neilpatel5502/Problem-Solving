# Problem: https://leetcode.com/problems/spiral-matrix

# Time Complexity: O(m * n), where m is number of rows and n is number of columns
# Space Complexity: O(1) additional space (excluding output list)

def spiralOrder(matrix):
    """
    Approach:
        - Traverse the matrix in a spiral order using direction control.
        - Start from the top-left corner and move right.
        - When reaching a boundary or a visited cell, change direction:
            right → down → left → up (repeat).
        - Mark visited cells with a placeholder (e.g., ".") to avoid revisiting.
        - Collect the elements in a result list as we move.
    """
    rows, cols = len(matrix), len(matrix[0])
    x, y = 0, 0              # Current cell position
    dx, dy = 0, 1            # Initial direction: move right
    out = []

    for _ in range(rows * cols):
        out.append(matrix[x][y])
        matrix[x][y] = "."  # Mark cell as visited

        # Check if next move is out of bounds or already visited
        if (
            not (0 <= x + dx < rows) or
            not (0 <= y + dy < cols) or
            matrix[x + dx][y + dy] == "."
        ):
            # Change direction: right -> down -> left -> up -> right ...
            dx, dy = dy, -dx

            # Right  (dx, dy = 0, 1)  -> Down  (1, 0)
            # Down   (dx, dy = 1, 0)  -> Left  (0, -1)
            # Left   (dx, dy = 0, -1) -> Up    (-1, 0)
            # Up     (dx, dy = -1, 0) -> Right (0, 1)

        # Move to the next cell
        x += dx
        y += dy

    return out


def main():
    # Test - 1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"output-1: {spiralOrder(matrix1)}")

    # Test - 2
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    print(f"output-2: {spiralOrder(matrix2)}")

if __name__ == "__main__":
    main()
