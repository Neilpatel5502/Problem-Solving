# Problem Link: https://leetcode.com/problems/permutations/
# Time Complexity: O(n * n!)     # n! permutations, each of length n
# Space Complexity: O(n)         # space for current permutation and visited tracking

def permute(nums):
    """
    Approach:
        - Use backtracking to explore all permutations.
        - Maintain a boolean array `isPicked` to track which elements are already used in the current permutation.
        - At each level of recursion, pick an unused number and mark it as used.
        - When the current permutation length equals nums length, add it to the output.
        - Backtrack by unmarking and popping the last used number.

    # Tree structure for nums = [1,2,3,4]:

            1           ~           2          ~          3          ~         4
            |                       |                     |                    |
    2       3       4   ~   1       3      4   ~   1      2      4   ~   1     2      3
    |       |       |       |       |      |       |      |      |       |     |      |
   3 4     2 4     2 3  ~  3 4     1 4    1 3  ~  4 2    1 4    1 2  ~  3 2   3 1    2 1
   | |     | |     | |     | |     | |    | |     | |    | |    | |     | |   | |    | |
   4 3     4 2     3 2  ~  4 3     4 1    3 1  ~  4 2    4 1    2 1  ~  3 2   3 1    2
    """

    out = []                    # List to store final permutations
    permutations = []           # Current permutation path
    isPicked = [False] * len(nums)  # Boolean tracker for elements used

    def backtrack(isPicked):
        if len(permutations) == len(nums):
            out.append(permutations.copy())
            return

        for i in range(len(nums)):
            if not isPicked[i]:
                # Include nums[i]
                permutations.append(nums[i])
                isPicked[i] = True

                # Recurse
                backtrack(isPicked)

                # Backtrack
                permutations.pop()
                isPicked[i] = False

    backtrack(isPicked)

    return out

def main():
    # Test - 1
    nums1 = [1, 2, 3]
    print(f"output-1: {permute(nums1)}")

    # Test - 2
    nums2 = [0, 1]
    print(f"output-2: {permute(nums2)}")

    # Test - 3
    nums3 = [1]
    print(f"output-3: {permute(nums3)}")

if __name__ == "__main__":
    main()
