# Problem: https://leetcode.com/problems/longest-common-prefix

# Time Complexity: O(n * m), where n = number of strings and m = length of the shortest string
# Space Complexity: O(m) for storing the common prefix

def longestCommonPrefix(strs):
    """
    Approach:
        - Initialize the common prefix with the first string.
        - Iterate through the remaining strings in the list.
        - For each string, compare characters with the current `common` prefix up to the minimum length.
        - Update the common prefix based on matching characters.
        - If at any point the common prefix becomes empty, return "".
    """
    common = strs[0]  # Start with the first string as the initial prefix

    for s in strs[1:]:
        temp = ""
        for i in range(min(len(s), len(common))):
            if s[i] == common[i]:
                temp += s[i]  # Add matching characters
            else:
                break         # Break on first mismatch

        if temp != "":
            common = temp    # Update prefix with current match
        else:
            return ""        # No common prefix

    return common

def main():
    # Test - 1
    strs1 = ["flower", "flow", "flight"]
    print(f"output-1: {longestCommonPrefix(strs1)}")

    # Test - 2
    strs2 = ["dog", "racecar", "car"]
    print(f"output-2: {longestCommonPrefix(strs2)}")

if __name__ == "__main__":
    main()
