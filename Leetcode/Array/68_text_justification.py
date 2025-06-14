# Problem: https://leetcode.com/problems/text-justification

# Time Complexity: O(n * k), where n = number of words, k = average word length
# Space Complexity: O(n * k), for storing the justified lines

def fullJustify(words, maxWidth):
    """
    Approach:
        - Iterate through the list of words while accumulating them into lines such that each line does
        not exceed maxWidth.
        - Once a line is full, calculate how many spaces are needed to fully justify it.
        - Distribute the spaces as evenly as possible, placing extra spaces from left to right.
        - For the last line, or lines with only one word, left-justify the line by adding all extra spaces
        at the end.
    """
    out = []
    line = []    # List of Words in the current line.
    length = 0   # length of the current line without spaces.
    i = 0

    while i < len(words):
        # len(line) indicate space count.
        if length + len(line) + len(words[i]) > maxWidth:
            extra_space = maxWidth - length  # Total spaces to distribute

            # Calculate spaces needed to add and remainder of the spaces.
            spaces = extra_space // max(1, len(line) - 1)
            remainder = extra_space % max(1, len(line) - 1)     # minimum word in line should be 1

            # Add spaces to the end of the words in line[:-1] (except last word)
            for j in range(max(1, len(line) - 1)):
                line[j] += " " * spaces

                # Parrallely add remainder spaces as well.
                if remainder:
                    line[j] += " "
                    remainder -= 1

            out.append("".join(line))  # Append justified line

            # Reset for next line
            line = []
            length = 0
            continue

        # Add word to current line
        line.append(words[i])
        length += len(words[i])
        i += 1

    # Handle last line - left justified
    last_line = " ".join(line)
    trail_space = maxWidth - len(last_line)
    last_line += " " * trail_space
    out.append(last_line)

    return out

def main():
    # Test - 1
    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth1 = 16
    print("output-1:")
    for line in fullJustify(words1, maxWidth1):
        print(f"'{line}'")

    # Test - 2
    words2 = ["What","must","be","acknowledgment","shall","be"]
    maxWidth2 = 16
    print("output-2:")
    for line in fullJustify(words2, maxWidth2):
        print(f"'{line}'")

    # Test - 3
    words3 = ["Science","is","what","we","understand","well","enough","to","explain",
              "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth3 = 20
    print("output-3:")
    for line in fullJustify(words3, maxWidth3):
        print(f"'{line}'")

if __name__ == "__main__":
    main()
