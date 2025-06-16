# Problem: https://leetcode.com/problems/surrounded-regions

# Time Complexity: O(m * n)           # Each cell is visited at most once
# Space Complexity: O(m * n)          # DFS recursion stack in worst case

def solve(board):
    """
    Approach:
        - The goal is to capture all regions surrounded by 'X'.
        - Any 'O' connected to the border is *not* surrounded and must be preserved.
        - Step 1: Run DFS from all border 'O' cells and mark them temporarily as 'B'.
        - Step 2: Convert all remaining 'O's to 'X' since they are surrounded.
        - Step 3: Convert all 'B's back to 'O' as they were not surrounded.
        - This modifies the board in-place as required.
    """
    m, n = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != "O":
            return

        board[r][c] = "B"  # Mark as "O" conntected to border

        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r, c + 1)
        dfs(r - 1, c)
        dfs(r, c - 1)

    # Step 1: Start DFS from border cells
    for r in range(m):
        for c in range(n):
            if (r in [0, m - 1] or c in [0, n - 1]) and board[r][c] == "O":
                dfs(r, c)

    # Step 2: Convert surrounded 'O' to 'X'
    for r in range(m):
        for c in range(n):
            if board[r][c] == "O":
                board[r][c] = "X"

    # Step 3: Convert temporary 'B' back to 'O'
    for r in range(m):
        for c in range(n):
            if board[r][c] == "B":
                board[r][c] = "O"


def main():
    # Test - 1
    board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    solve(board1)
    print("output-1:", board1)

    # Test - 2
    board2 = [["X"]]
    solve(board2)
    print("output-2:", board2)

    # Test - 3
    board3 = [
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"]
    ]
    solve(board3)
    print("output-3:", board3)

if __name__ == "__main__":
    main()
