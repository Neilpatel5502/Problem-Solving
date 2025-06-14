# Problem: https://leetcode.com/problems/happy-number

# Time Complexity: O(log n), due to the digits shrinking over iterations
# Space Complexity: O(log n), to store visited numbers

def isHappy(n):
    """
    Approach:
        - A number is happy if repeatedly replacing it with the sum of the squares
          of its digits eventually results in 1.
        - Use a set to track visited numbers to detect cycles.
        - Use a precomputed dictionary of digit squares for faster lookup.
    """
    square = {
        '0': 0, '1': 1, '2': 4, '3': 9, '4': 16,
        '5': 25, '6': 36, '7': 49, '8': 64, '9': 81
    }
    visited = set()

    while n != 1 and n not in visited:
        visited.add(n)        # Add current number to visited set
        number = str(n)       # Convert to string to access digits
        s = 0

        for ch in number:
            s += square[ch]   # Add square of each digit

        n = s                 # Update number with new sum

    return n == 1             # Return True if happy (reaches 1)

def main():
    # Test - 1
    n1 = 19
    print(f"output-1: {isHappy(n1)}")

    # Test - 2
    n2 = 2
    print(f"output-2: {isHappy(n2)}")

if __name__ == "__main__":
    main()
