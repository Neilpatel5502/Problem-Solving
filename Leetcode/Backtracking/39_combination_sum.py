# Problem Link: https://leetcode.com/problems/combination-sum/
# Time Complexity: O(2^t) where t = target (approximate)
# Space Complexity: O(t) for recursion stack and building combinations

def combinationSum(candidates, target):
    """
    Approach:
        - Use backtracking to explore all possible combinations.
        - At each step:
            - Include the current candidate and stay at the same index (because a number can be reused unlimited times).
            - Or move to the next index without including the current number.
        - If the running total equals the target, add a copy of the current combination to the output list.
        - If the running total exceeds the target or all candidates are exhausted, backtrack.

    # Tree structure:
                                 []
                       /                       \
                    [2]                        []
               /           \               /             \
            [2,2]          [2,3]          [3]             []
           /     \         /    \        /    \           /   \
      [2,2,2]  [2,2,3] [2,3,3] [2,3,6]  [3,3] [3,6]      [6]   []
       /     \            /   \
    [2,2,2,2] [2,2,2,3]  ...
    """

    out = []             # List to store final valid combinations
    combinations = []    # Current combination being built

    def backtrack(i, total):
        if total == target:
            # If sum equals target, add a copy of combination
            out.append(combinations.copy())
            return

        if total > target or i >= len(candidates):
            # Exceeded the target or no candidates left
            return

        # Choose the current candidate
        combinations.append(candidates[i])
        backtrack(i, total + candidates[i])

        # Backtrack, remove the last chosen number
        combinations.pop()
        backtrack(i + 1, total)

    # Start backtracking from index 0 with total 0
    backtrack(0, 0)

    return out

def main():
    # Test - 1
    candidates1 = [2,3,6,7]
    target1 = 7
    print(f"output-1: {combinationSum(candidates1, target1)}")

    # Test - 2
    candidates2 = [2,3,5]
    target2 = 8
    print(f"output-2: {combinationSum(candidates2, target2)}")

    # Test - 3
    candidates3 = [2]
    target3 = 1
    print(f"output-3: {combinationSum(candidates3, target3)}")

if __name__ == "__main__":
    main()
