# Problem Link: https://leetcode.com/problems/sum-of-all-subset-xor-totals

# Time Complexity: O(2^n * n)       2^n subsets for a list of length n
# Space Complexity: O(2^n * n)

def subsetXORSum(nums):
    """
    Approach:
        - Generate all possible subsets of the input list `nums` using backtracking.
        - For each non-empty subset, compute the XOR of all elements in the subset.
        - Sum the XOR values of all subsets to get the final answer.
    """
    all_subsets = []    # List to store all subsets
    subset = []         # Current subset being constructed

    # Backtracking function to generate all subsets starting from index i
    def backtrack(i):
        if i >= len(nums):
            # Add a copy of the current subset to the list of all subsets
            all_subsets.append(subset.copy())
            return

        # Include nums[i] in the current subset
        subset.append(nums[i])
        backtrack(i + 1)

        # Exclude nums[i] from the current subset (backtrack)
        subset.pop()
        backtrack(i + 1)

    # Helper function to compute XOR of elements in a given subset
    def list_xor(subset):
        xor = subset[0]
        for num in subset[1:]:
            xor ^= num  # XOR current value with the next number in subset

        return xor

    # Generate all subsets
    backtrack(0)

    # Compute XOR for each non-empty subset and add to answer
    answer = 0
    for sub in all_subsets:
        if len(sub) != 0:
            answer += list_xor(sub)

    return answer


def main():
    # Test - 1
    nums1 = [1,3]
    print(f"output-1: {subsetXORSum(nums1)}")

    # Test - 2
    nums2 = [5,1,6]
    print(f"output-2: {subsetXORSum(nums2)}")

    # Test - 3
    nums3 = [3,4,5,6,7,8]
    print(f"output-3: {subsetXORSum(nums3)}")

if __name__ == "__main__":
    main()
