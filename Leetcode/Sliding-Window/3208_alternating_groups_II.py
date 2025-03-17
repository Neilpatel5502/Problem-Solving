# Problem Link: https://leetcode.com/problems/alternating-groups-ii

# Time Complexity: O(n)
# Space Complexity: O(1)

def numberOfAlternatingGroups(colors, k):
    """
    Approach:
        - Use a sliding window technique to check for alternating groups of size `k` in a circular array.
        - The key condition for a valid alternating group is that every adjacent tile in the window should have different colors.
        - Since the array represents a circle, index wrapping is handled using modulo (`% n`).
        - We maintain two pointers (`left` and `right`) to track a valid group of size `k`.
        - If the window maintains alternating colors, we count it as a valid group.
    """
    output = 0
    left = 0
    right = 0
    n = len(colors)

    # Expand the right pointer until we check all possible windows in the circular array
    while right < n + k - 1:
        # If the current tile and the previous tile have the same color, reset `left`
        if colors[right % n] == colors[(right - 1) % n]:
            left = right

        # If window size becomes larger than k it means we have solution
        if right - left + 1 >= k:
            output += 1

        right += 1

    return output

def main():
    # Test - 1
    colors1 = [0,1,0,1,0]
    k1 = 3
    print(f"output-1: {numberOfAlternatingGroups(colors1, k1)}")

    # Test - 2
    colors2 = [0,1,0,0,1,0,1]
    k2 = 6
    print(f"output-2: {numberOfAlternatingGroups(colors2, k2)}")

    # Test - 3
    colors3 = [1,1,0,1]
    k3 = 4
    print(f"output-2: {numberOfAlternatingGroups(colors3, k2)}")

if __name__ == "__main__":
    main()
