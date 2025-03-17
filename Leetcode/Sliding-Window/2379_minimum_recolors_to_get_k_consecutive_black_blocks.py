# Problem Link: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks

# Time Complexity: O(n)
# Space Complexity: O(1)    Counts dict has only 2 values.

def minimumRecolors(blocks, k):
    """
    Approach:
        - Use a sliding window of size `k` to count the number of white ('W') and black ('B') blocks in the window.
        - Initially, count the 'W' and 'B' blocks in the first `k` characters.
        - Slide the window one character at a time, updating the counts dynamically.
        - Keep track of the minimum number of white blocks ('W') that need to be recolored to get `k` consecutive black ('B') blocks.
    """
    # Dictionary to store counts of 'W' (white) and 'B' (black) in the current window
    counts = {'W': 0, 'B': 0}

    # Count occurrences of 'W' and 'B' in the first window of size `k`
    for i in range(k):
        counts[blocks[i]] += 1

    # Initialize left (l) and right (r) pointers for the sliding window
    l = 0
    r = k - 1

    # If the length of the string is exactly `k`, return the number of 'W' directly
    if len(blocks) == k:
        return counts['W']

    out = float('inf')

    # Slide the window across the string
    while r < len(blocks):
        # Update the minimum number of white blocks ('W') that need to be recolored
        out = min(out, counts['W'])

        # Move the left pointer out of the window, decrement its count
        counts[blocks[l]] -= 1
        l += 1

        # Move the right pointer to expand the window
        r += 1
        if r < len(blocks):
            counts[blocks[r]] += 1

    return out


def main():
    # Test - 1
    blocks1 = "WBBWWBBWBW"
    k1 = 7
    print(f"output-1: {minimumRecolors(blocks1, k1)}")

    # Test - 2
    blocks2 = "WBWBBBW"
    k2 = 2
    print(f"output-2: {minimumRecolors(blocks2, k2)}")

if __name__ == "__main__":
    main()
