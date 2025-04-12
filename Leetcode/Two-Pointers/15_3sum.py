# Problem: https://leetcode.com/problems/3sum
# Time Complexity: O(n^2) – due to the nested loop with two-pointer approach
# Space Complexity: O(1) – excluding the space required for the output list

def threeSum(nums):
    """
    Approach:
        - Sort the input array to facilitate skipping duplicates and using two-pointer technique.
        - Iterate through the array:
            - For each number, apply the two-pointer approach on the subarray to the right of the current index.
            - Skip duplicate numbers to avoid duplicate triplets.
            - If the sum of the current number and the two pointers equals zero, store the triplet.
            - Move the left and right pointers accordingly and skip duplicates.
    """

    out = []
    nums.sort()  # Sort the array to apply two-pointer strategy and manage duplicates

    for idx, num in enumerate(nums):
        if num > 0:
            break  # No need to proceed if the smallest number is already > 0

        # Skip duplicate values to avoid repeated triplets
        if idx > 0 and num == nums[idx - 1]:
            continue

        # Two-pointer initialization
        l, r = idx + 1, len(nums) - 1

        while l < r:
            summation = num + nums[l] + nums[r]  # Compute the sum of the triplet

            if summation > 0:
                r -= 1  # Sum too large, move right pointer to decrease the sum
            elif summation < 0:
                l += 1  # Sum too small, move left pointer to increase the sum
            else:
                out.append([num, nums[l], nums[r]])  # Found a valid triplet
                l += 1
                r -= 1

                # Skip duplicates after finding a valid triplet
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

    return out


def main():
    # Test - 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"output-1: {threeSum(nums1)}")

    # Test - 2
    nums2 = [0, 1, 1]
    print(f"output-2: {threeSum(nums2)}")

    # Test - 3
    nums3 = [0, 0, 0]
    print(f"output-3: {threeSum(nums3)}")

if __name__ == "__main__":
    main()
