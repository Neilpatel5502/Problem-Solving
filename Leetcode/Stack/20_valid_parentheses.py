# Problem: https://leetcode.com/problems/valid-parentheses/
# Time Complexity: O(n) – where n is the length of the string
# Space Complexity: O(n) – for the stack in the worst case

def isValid(s):
    """
    Approach:
        - Use a stack to keep track of opening brackets.
        - Use a hashmap to map each closing bracket to its corresponding opening bracket.
        - Traverse the string:
            - If the character is a closing bracket, check if it matches the top of the stack.
              If it does, pop from the stack; otherwise, return False.
            - If it's an opening bracket, push it to the stack.
        - After processing all characters, if the stack is empty, the string is valid.
    """

    para = {')': "(", ']': "[", '}': "{"}  # Mapping of closing to opening brackets
    stack = []  # Stack to keep track of unmatched opening brackets

    for i in s:
        if i in para:
            # If the stack is not empty and top matches, pop it
            if stack and para[i] == stack[-1]:
                stack.pop()
            else:
                return False  # Mismatch or empty stack when expecting match
        else:
            stack.append(i)  # Push opening brackets to the stack

    return True if not stack else False  # Valid if stack is empty


def main():
    # Test - 1
    s1 = "()"
    print(f"output-1: {isValid(s1)}")

    # Test - 2
    s2 = "()[]{}"
    print(f"output-2: {isValid(s2)}")

    # Test - 3
    s3 = "(]"
    print(f"output-3: {isValid(s3)}")

    # Test - 4
    s4 = "([])"
    print(f"output-4: {isValid(s4)}")

if __name__ == "__main__":
    main()
