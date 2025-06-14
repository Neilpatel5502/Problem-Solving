# Problem Link: https://leetcode.com/problems/group-anagrams

# Time Complexity: O(n * k log k) - where n is the number of strings and k is the maximum length of a string
# Space Complexity: O(n * k) - to store all strings in the output dictionary

def groupAnagrams(strs):
    """
    Approach:
        - Use a hash map (defaultdict) to group anagrams.
        - For each string in the input list, sort its characters to create a key.
        - Append the original string to the list corresponding to that sorted key.
        - At the end, return all grouped lists (values of the dictionary).
    """

    from collections import defaultdict

    output = defaultdict(list)  # Dictionary to group anagrams

    for s in strs:
        sorted_s = ''.join(sorted(s))  # Sort the string to use as key
        output[sorted_s].append(s)     # Group by sorted key

    return list(output.values())       # Return grouped anagrams as list of lists


def main():
    # Test - 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"output-1: {groupAnagrams(strs1)}")

    # Test - 2
    strs2 = [""]
    print(f"output-2: {groupAnagrams(strs2)}")

    # Test - 3
    strs3 = ["a"]
    print(f"output-3: {groupAnagrams(strs3)}")

if __name__ == "__main__":
    main()
