# Problem Link: https://leetcode.com/problems/subsets/
# Time Complexity: O(2^n * n)       # 2^n subsets, and copying each subset of size up to n
# Space Complexity: O(2^n * n)      # storing all subsets

def subsets(nums):
    """
    Approach:
        - Use backtracking to generate all possible subsets.
        - At each index, make a decision:
            - Include the current element in the subset.
            - Do not include the current element in the subset.
        - Once the end of the list is reached, add the current subset to the output list.
        - This ensures that all possible subsets are covered without duplicates.

    # Tree structure:
                                 NULL
                       /                     \
                   [1]                        []
                /       \                  /       \
           [1,2]         [1]           [2]          []
          /     \       /    \        /    \       /    \
    [1,2,3]    [1,2] [1,3]   [1]   [2,3]   [2]   [3]     []
    """
    out = []      # List to store all subsets
    subset = []   # Current subset being built

    # Backtracking function to explore subsets starting from index i
    def backtrack(i):
        if i >= len(nums):
            # Add a copy of the current subset to output
            out.append(subset.copy())
            return

        # Include nums[i] in the current subset
        subset.append(nums[i])
        backtrack(i + 1)

        # Exclude nums[i] from the current subset
        subset.pop()
        backtrack(i + 1)

    # Start backtracking from index 0
    backtrack(0)

    return out

def main():
    # Test - 1
    nums1 = [1, 2, 3]
    print(f"output-1: {subsets(nums1)}")

    # Test - 2
    nums2 = [0]
    print(f"output-2: {subsets(nums2)}")

if __name__ == "__main__":
    main()
