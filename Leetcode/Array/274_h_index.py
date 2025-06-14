# Problem: https://leetcode.com/problems/h-index

# Time Complexity: O(n log n)         # Due to sorting
# Space Complexity: O(1)              # Sorting in-place or constant extra space

def hIndex(citations):
    """
    Approach:
        - Sort the citations array in ascending order.
        - For each citation, check how many papers have citations >= current citation.
        - h-index is the maximum value h such that there are at least h papers with at least h citations each.
        - The trick is to check (n - i) vs citation[i]. If (n - i) >= citation[i], we can consider citation[i] as h.
        Otherwise, use (n - i) as h because it represents the number of papers that qualify, but citation[i] is too high.
    """
    n = len(citations)
    citations.sort()    # Sort citations in ascending order
    out = 0

    for i, num in enumerate(citations):
        if n - i >= num:
            # Enough papers with at least 'num' citations
            out = max(out, num)
        else:
            # Only (n - i) papers qualify, not enough to reach 'num'
            out = max(out, n - i)
            break

    return out


def main():
    # Test - 1
    citations1 = [3,0,6,1,5]
    print(f"output-1: {hIndex(citations1)}")

    # Test - 2
    citations2 = [1,3,1]
    print(f"output-2: {hIndex(citations2)}")

if __name__ == "__main__":
    main()
