# Problem: https://leetcode.com/problems/integer-to-roman

# Time Complexity: O(1)       # Fixed number of symbols, maximum 13 iterations
# Space Complexity: O(1)

def intToRoman(num):
    """
    Approach:
        - Use a list of tuples mapping integer values to Roman numeral symbols in descending order.
        - Iterate through the list, subtracting the largest possible value from `num` and appending the corresponding symbol.
        - Repeat the process until `num` is reduced to 0.
        - This greedy approach ensures the correct Roman numeral is built from highest to lowest.
    """
    int_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    out = ""

    # Construct Roman numeral by subtracting highest possible values
    for val, symbol in int_to_roman:
        while num >= val:
            out += symbol
            num -= val

    return out

def main():
    # Test - 1
    num1 = 3749
    print(f"output-1: {intToRoman(num1)}")

    # Test - 2
    num2 = 58
    print(f"output-2: {intToRoman(num2)}")

    # Test - 3
    num3 = 1994
    print(f"output-3: {intToRoman(num3)}")

if __name__ == "__main__":
    main()
