# Problem: https://leetcode.com/problems/isomorphic-strings

# Time Complexity: O(n), where n = length of the input strings
# Space Complexity: O(n), for storing mappings and visited characters

def isIsomorphic(s, t):
    """
    Approach:
        - Use a dictionary `temp` to map characters from `s` to `t`.
        - Use a set `visited` to track characters in `t` that are already mapped.
        - For each character pair (ch1, ch2) in s and t:
            - If ch1 is not mapped yet:
                - Check if ch2 is already visited (mapped by another ch1); if yes, return False.
                - Otherwise, add the mapping and mark ch2 as visited.
            - If ch1 is already mapped, check if it maps correctly to ch2; if not, return False.
        - If all mappings are consistent, return True.
    """
    temp = {}
    visited = set()     # To track ch from "t" already aplied in dict

    for ch1, ch2 in zip(s, t):
        # If ch1 not in temp then add it in temp if ch2 not visited.
        # if ch2 is in visited then it should be False.
        if ch1 not in temp:
            if ch2 in visited:
                return False
            temp[ch1] = ch2
            visited.add(ch2)
        else:
            if ch2 != temp[ch1]:
                return False

    return True

def main():
    # Test - 1
    s1 = "egg"
    t1 = "add"
    print(f"output-1: {isIsomorphic(s1, t1)}")

    # Test - 2
    s2 = "foo"
    t2 = "bar"
    print(f"output-2: {isIsomorphic(s2, t2)}")

    # Test - 3
    s3 = "paper"
    t3 = "title"
    print(f"output-3: {isIsomorphic(s3, t3)}")

if __name__ == "__main__":
    main()
