# Problem Link: Leetcode - Combination Sum II
# Time Complexity: O(2^n)         # each element can be picked or skipped
# Space Complexity: O(n)          # recursion stack + current subset storage

def combinationSum2(candidates, target):
    """
    Approach:
        - Sort the candidates array to group duplicates together.
        - Use backtracking to explore all combinations.
        - At each step:
            - Include the current candidate and move to the next index (cannot reuse the same element).
            - Skip the current candidate and move forward.
        - To avoid duplicates:
            - Skip subsequent elements if they are the same as the current one after a pop.

    # Tree structure:
                                 []
                        /                  \
                  [2]                       []
              /        \                 /      \
         [2,3]         [2,6]         [3]        [6]
         /   \           ...         /  \         ...
    [2,3,6] [2,3,7]             [3,6] [3,7]
        ...      ...               ...    ...
     (duplicates skipped due to sorting and while loop)
    """

    out = []
    subset = []
    candidates.sort()

    def backtrack(i, cur_sum):
        if cur_sum == target:
            out.append(subset.copy())
            return

        if i >= len(candidates) or cur_sum > target:
            return

        # Include candidates[i]
        subset.append(candidates[i])
        backtrack(i + 1, cur_sum + candidates[i])
        subset.pop()

        # Skip all duplicates of candidates[i]
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1

        # Exclude current candidates[i]
        backtrack(i + 1, cur_sum)

    backtrack(0, 0)

    return out

def main():
    # Test - 1
    candidates1 = [10,1,2,7,6,1,5]
    target1 = 8
    print(f"output-1: {combinationSum2(candidates1, target1)}")

    # Test - 2
    candidates2 = [2,5,2,1,2]
    target2 = 5
    print(f"output-2: {combinationSum2(candidates2, target2)}")

if __name__ == "__main__":
    main()
