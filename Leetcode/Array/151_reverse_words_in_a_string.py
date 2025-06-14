# Problem: https://leetcode.com/problems/reverse-words-in-a-string

# Time Complexity: O(n)
# Space Complexity: O(n)

def reverseWords(s):
    """
    Approach:
        - Traverse the string manually to extract words (non-space sequences).
        - Skip multiple spaces and accumulate words in a list `out`.
        - After collecting all words, reverse the list and join with a single space.
        - This ensures removal of extra spaces and proper reversal of word order.
    """
    out = []  # To store words

    i = 0
    while i < len(s):
        j = i
        if s[i] != " ":
            # Find the end of the current word
            while j < len(s) and s[j] != " ":
                j += 1

            out.append(s[i:j])  # Append the word
            j -= 1              # Reset j for i update

        i = j + 1  # Move to next character

    # Reverse the collected words and join with a space
    return " ".join(out[::-1])

def main():
    # Test - 1
    s1 = "the sky is blue"
    print(f"output-1: {reverseWords(s1)}")

    # Test - 2
    s2 = "  hello world  "
    print(f"output-2: {reverseWords(s2)}")

    # Test - 3
    s3 = "a good   example"
    print(f"output-3: {reverseWords(s3)}")

if __name__ == "__main__":
    main()
