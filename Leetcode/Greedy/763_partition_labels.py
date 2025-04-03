# Problem Link: https://leetcode.com/problems/partition-labels

# Time Complexity: O(N), where N is the length of the string, since we traverse the string twice.
# Space Complexity: O(1), since we store only a fixed number of character indices (at most 26 for lowercase letters).

def partitionLabels(s):
    """
    Approach:
        - First, determine the last occurrence of each character in the string.
        - Iterate through the string while keeping track of the maximum last occurrence (`end`) of
        characters encountered so far.
        - If the current index matches `end`, it indicates a valid partition.
        - Store the partition size and continue processing the remaining string.
    """

    index_count = {}    # Stores the last occurrence index of each character
    output = []         # Stores the sizes of partitions

    # Record the last occurrence of each character in the string
    for i, ch in enumerate(s):
        index_count[ch] = i

    size = 0        # Current partition size
    end = 0         # Tracks the furthest last occurrence in the current partition

    # Iterate through the string to form partitions
    for i, ch in enumerate(s):
        size += 1
        end = max(end, index_count[ch])     # Update partition end boundary

        # If current index matches `end`, we found a partition
        if i == end:
            output.append(size)
            size = 0        # Reset partition size for the next partition

    return output


def main():
    # Test - 1
    s1 = "ababcbacadefegdehijhklij"
    print(f"output-1: {partitionLabels(s1)}")

    # Test - 2
    s2 = "eccbbbbdec"
    print(f"output-2: {partitionLabels(s2)}")

if __name__ == "__main__":
    main()
