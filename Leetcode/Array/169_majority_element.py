# Problem: https://leetcode.com/problems/majority-element/

# Time Complexity: O(n)              # Single pass through the list
# Space Complexity: O(1)             # Constant space used

def majorityElement(nums):
    """
    Approach:
        - Use the Boyer-Moore Voting Algorithm.
        - The idea is to cancel out different elements and keep track of the most frequent one.
        - Maintain two variables:
            - `majority_num`: current candidate for majority
            - `count`: number of votes for current candidate
        - If count becomes 0, select current number as new candidate.
        - If current number equals candidate, increment count; else decrement count.
        - Since the problem guarantees a majority element exists, the final candidate will be the answer.
    """
    majority_num = None  # Current candidate for majority element
    count = 0            # Vote count for current candidate

    for num in nums:
        if count == 0:
            majority_num = num  # Set new candidate

        if num == majority_num:
            count += 1          # Vote for candidate
        else:
            count -= 1          # Vote against candidate

    return majority_num


def main():
    # Test - 1
    nums1 = [3,2,3]
    print(f"output-1: {majorityElement(nums1)}")

    # Test - 2
    nums2 = [2,2,1,1,1,2,2]
    print(f"output-2: {majorityElement(nums2)}")

if __name__ == "__main__":
    main()
