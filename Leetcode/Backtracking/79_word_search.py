# Problem Link: https://leetcode.com/problems/word-search/
# Time Complexity: O(m * n * 4^l), where:
#   - m x n = board size
#   - l = length of the word
#   - At most 4 directions explored per letter
# Space Complexity: O(l) for the recursion stack (backtrack depth)

def exist(board, word):
    """
    Approach:
        - Use backtrack from each cell to try forming the word.
        - At each cell, check if current character matches word[k].
        - Mark the cell as visited by setting it to '/' and restore it during backtrack.
        - Explore in 4 directions: up, down, left, right.
        - If the entire word is matched (k == len(word)), return True.
        - If all paths fail, return False.
    """

    def backtrack(i, j, k):
        # Base case: if we've matched all characters
        if k == len(word):
            return True

        # Check if (i, j) is out of bounds or doesn't match current character or already visited
        if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) \
           or board[i][j] != word[k] or board[i][j] == '/':
            return False

        # Temporarily mark the current cell as visited
        temp, board[i][j] = board[i][j], '/'

        # Recursively check in all four directions
        out = (
            backtrack(i + 1, j, k + 1) or  # down
            backtrack(i - 1, j, k + 1) or  # up
            backtrack(i, j + 1, k + 1) or  # right
            backtrack(i, j - 1, k + 1)     # left
        )

        # Restore the original value (backtrack)
        board[i][j] = temp

        return out

    # Try to start backtrack from every cell in the grid
    for i in range(len(board)):
        for j in range(len(board[0])):
            # If we can construct the word starting from cell (i, j)
            if backtrack(i, j, 0):
                return True

    # If no valid path found
    return False

def main():
    # Test - 1
    board1 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word1 = "ABCCED"
    print(f"output-1: {exist(board1, word1)}")  # True

    # Test - 2
    board2 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word2 = "SEE"
    print(f"output-2: {exist(board2, word2)}")  # True

    # Test - 3
    board3 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word3 = "ABCB"
    print(f"output-3: {exist(board3, word3)}")  # False

if __name__ == "__main__":
    main()
