# Problem: https://leetcode.com/problems/zigzag-conversion

# Time Complexity: O(n), where n is the length of the input string
# Space Complexity: O(n), used for storing characters in rows

def convert(s, numRows):
    """
    Approach:
        - Simulate writing characters in a zigzag pattern row-by-row.
        - Use a list of lists (one for each row) to store characters.
        - Move down the rows (incrementing) and then up (decrementing) repeatedly.
        - Once all characters are placed, concatenate the rows to form the result.
        - Handle the special case where numRows == 1 (no zigzag).
    """
    if numRows == 1:
        return s

    out = [[] for _ in range(numRows)]  # Initialize rows
    inc = True      # Flag for moving down
    dec = False     # Flag for moving up
    idx = 0         # Current row index

    for ch in s:
        if inc:
            out[idx].append(ch)
            idx += 1

            # Switch direction to up when reaching the last row
            if idx == numRows:
                inc = False
                dec = True
                idx -= 1
                continue

        if dec:
            idx -= 1
            out[idx].append(ch)

            # Switch direction to down when reaching the first row
            if idx == 0:
                dec = False
                inc = True
                idx += 1

    # Join all characters row by row
    ans = ""
    for row in out:
        ans += "".join(row)

    return ans

def main():
    # Test - 1
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    print(f"output-1: {convert(s1, numRows1)}")

    # Test - 2
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    print(f"output-2: {convert(s2, numRows2)}")

    # Test - 3
    s3 = "A"
    numRows3 = 1
    print(f"output-3: {convert(s3, numRows3)}")

if __name__ == "__main__":
    main()
