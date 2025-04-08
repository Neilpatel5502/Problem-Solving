# Problem: https://leetcode.com/problems/top-k-frequent-elements/
# Time Complexity: O(n log n) - due to sorting the frequency map
# Space Complexity: O(n) - to store the frequency map and result list

def topKFrequent(nums, k):
    """
    Approach:
        - Use a hash map to count the frequency of each number in `nums`.
        - Sort the items in the frequency map by their frequency in descending order.
        - Extract the keys (numbers) from the sorted items.
        - Return the first `k` keys as the result.
    """

    count = {}  # Dictionary to count frequency of elements

    # Count frequencies
    for n in nums:
        count[n] = count.get(n, 0) + 1

    # Sort the dictionary by frequency in descending order
    sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

    out = list(sorted_count.keys())  # Extract sorted keys

    return out[:k]  # Return top k frequent elements


def main():
    # Test - 1
    nums1 = [1,1,1,2,2,3]
    k1 = 2
    print(f"output-1: {topKFrequent(nums1, k1)}")

    # Test - 2
    nums2 = [1]
    k2 = 1
    print(f"output-2: {topKFrequent(nums2, k2)}")

if __name__ == "__main__":
    main()
