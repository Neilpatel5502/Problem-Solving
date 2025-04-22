# Problem Link: https://leetcode.com/problems/subsets-ii/
# Time Complexity: O(2^n)          # each element has 2 choices (include or not), but duplicates are skipped
# Space Complexity: O(n)           # recursion depth + current subset storage

def subsetsWithDup(nums):
    """
    Approach:
        - Sort the input array so that duplicates are adjacent.
        - Use backtracking to explore all subset combinations.
        - At each step:
            - Include the current number and recurse.
            - Exclude the current number and skip all duplicates to avoid duplicate subsets.
        - Add the subset to the output only when we reach the end of the array.
    # Tree structure for nums = [1,2,2]:
                                 []
                       /                    \
                    [1]                     []
                 /      \                 /     \
              [1,2]     [1]           [2]       []
              /   \                    |
        [1,2,2]  [1,2]              [2,2]

    (Duplicate [1,2] or [2,2] is skipped due to sorting and the while loop)
    """

    out = []              # Final list of unique subsets
    subset = []           # Current subset path
    nums.sort()           # Sort to group duplicates

    def backtrack(i):
        if i == len(nums):
            out.append(subset.copy())
            return

        # Include nums[i]
        subset.append(nums[i])
        backtrack(i + 1)

        # Exclude nums[i] (backtrack)
        subset.pop()

        # Skip duplicates
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        backtrack(i + 1)

    backtrack(0)

    return out

def main():
    # Test - 1
    nums1 = [1, 2, 2]
    print(f"output-1: {subsetsWithDup(nums1)}")

    # Test - 2
    nums2 = [0]
    print(f"output-2: {subsetsWithDup(nums2)}")

if __name__ == "__main__":
    main()
