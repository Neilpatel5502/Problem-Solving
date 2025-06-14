# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

# Time Complexity: O(n)              # Single pass through the list
# Space Complexity: O(1)             # Constant space used

def maxProfit(prices):
    """
    Approach:
        - Use two pointers: `left` (buy day) and `right` (sell day).
        - Initialize `left = 0` and `right = 1`.
        - If prices[right] > prices[left], compute the profit and update max_profit.
        - If prices[right] <= prices[left], update `left` to `right` since we found a cheaper buy price.
        - Move `right` one step at a time through the array.
        - Return the maximum profit found during the traversal.
    """
    max_profit = 0
    left, right = 0, 1  # left is buy day, right is sell day

    while right < len(prices):
        if prices[left] < prices[right]:
            # Potential profit exists
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            # Found a lower price to buy
            left = right

        right += 1

    return max_profit


def main():
    # Test - 1
    prices1 = [7,1,5,3,6,4]
    print(f"output-1: {maxProfit(prices1)}")

    # Test - 2
    prices2 = [7,6,4,3,1]
    print(f"output-2: {maxProfit(prices2)}")

if __name__ == "__main__":
    main()
