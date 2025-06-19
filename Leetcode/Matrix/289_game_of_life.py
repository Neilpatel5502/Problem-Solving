# Problem: https://leetcode.com/problems/game-of-life

# Time Complexity: O(m * n), where m is number of rows and n is number of columns
# Space Complexity: O(m * n), due to the use of a copy grid

def gameOfLife(board):
    """
    Approach:
        - Create a copy of the board to preserve original state while updating the actual board.
        - For each cell, count live neighbors by checking all 8 directions.
        - Apply the Game of Life rules:
            Rule 1: Any live cell with fewer than two live neighbors dies (underpopulation).
            Rule 2: Any live cell with two or three live neighbors lives on.
            Rule 3: Any live cell with more than three live neighbors dies (overpopulation).
            Rule 4: Any dead cell with exactly three live neighbors becomes a live cell (reproduction).
        - Update the original board in-place based on the rules.
    """

    m, n = len(board), len(board[0])

    # Make a deep copy of the original board
    copy = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            copy[i][j] = board[i][j]

    # Helper function to count live neighbors for cell (r, c)
    def live_neighbors(r, c):
        count = 0
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                # Skip out-of-bounds and self cell
                if i < 0 or j < 0 or i >= m or j >= n or (i == r and j == c):
                    continue

                count += copy[i][j]
        return count

    # Update board based on live neighbors
    for i in range(m):
        for j in range(n):
            live = live_neighbors(i, j)

            if copy[i][j] == 1:
                if live < 2 or live > 3:
                    board[i][j] = 0  # Dies
            else:
                if live == 3:
                    board[i][j] = 1  # Becomes alive


def main():
    # Test - 1
    board1 = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    gameOfLife(board1)
    print(f"output-1: {board1}")

    # Test - 2
    board2 = [
        [1, 1],
        [1, 0]
    ]
    gameOfLife(board2)
    print(f"output-2: {board2}")


if __name__ == "__main__":
    main()
