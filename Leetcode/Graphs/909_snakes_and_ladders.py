# Problem: https://leetcode.com/problems/snakes-and-ladders

# Time Complexity: O(n^2)              # Each square is visited at most once
# Space Complexity: O(n^2)             # For visited set and BFS queue

from collections import deque

def snakesAndLadders(board):
    """
    Approach:
        - Reverse the board to simplify index calculations.
        - Use BFS to simulate dice rolls and explore reachable squares.
        - For each move, check if the square leads to a snake/ladder (non -1).
        - Track visited squares to avoid cycles.
        - Return the number of moves to reach the final square.
        - If unreachable, return -1.
    """

    length = len(board)
    board.reverse()  # Reverse the board to match the natural square numbering

    # Helper function to convert square number to board position
    def intToPos(square):
        r = (square - 1) // length
        c = (square - 1) % length

        if r % 2:  # Zigzag pattern: reverse column index on odd rows
            c = length - 1 - c

        return [r, c]

    queue = deque([[1, 0]])  # (square, moves)
    visited = set([1])

    while queue:
        square, moves = queue.popleft()

        # Try all dice rolls from current square
        for i in range(1, 7):
            nextSquare = square + i
            if nextSquare > length * length:
                continue

            r, c = intToPos(nextSquare)

            # Snake or ladder
            if board[r][c] != -1:
                nextSquare = board[r][c]

            if nextSquare == length * length:
                return moves + 1  # Reached last square

            if nextSquare not in visited:
                visited.add(nextSquare)
                queue.append([nextSquare, moves + 1])

    return -1  # Destination not reachable


def main():
    # Test - 1:
    board1 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]
    print(f"output-1: {snakesAndLadders(board1)}")

    # Test - 2:
    board2 = [
        [-1, -1],
        [-1, 3]
    ]
    print(f"output-2: {snakesAndLadders(board2)}")

if __name__ == "__main__":
    main()
