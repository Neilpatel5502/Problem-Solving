# Problem Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number

# Time Complexity: O(4^n)         # n = length of digits, each digit can contribute up to 4 letters
# Space Complexity: O(n)          # recursion depth + string building

def letterCombinations(digits):
    """
    Approach:
        - Use backtracking to explore all possible character combinations digit by digit.
        - Maintain a map of digit -> characters (just like phone keypad).
        - At each level of recursion, iterate over characters mapped to the current digit.
        - Append character to current string and recurse to the next digit.
        - When the length of the current string equals the number of digits, add to the output.

    # Tree structure for digits = "23":
                     ""
             /        |        \
           "a"       "b"      "c"
         / | \     / | \    / | \
       ad ae af  bd be bf  cd ce cf
    """

    out = []     # List to store final combinations
    digit_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtrack(i, cur_str):
        # Base case: if current string is complete
        if len(cur_str) == len(digits):
            out.append(cur_str)
            return

        # Recursive case: try all letters mapped to digits[i]
        for ch in digit_map[digits[i]]:
            backtrack(i + 1, cur_str + ch)

    # Start backtracking if digits is not empty
    if digits:
        backtrack(0, "")

    return out

def main():
    # Test - 1
    digits1 = "23"
    print(f"output-1: {letterCombinations(digits1)}")

    # Test - 2
    digits2 = ""
    print(f"output-2: {letterCombinations(digits2)}")

    # Test - 3
    digits3 = "2"
    print(f"output-3: {letterCombinations(digits3)}")

if __name__ == "__main__":
    main()
