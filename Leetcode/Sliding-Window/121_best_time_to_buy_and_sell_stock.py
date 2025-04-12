# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Time Complexity: O(n) – single pass through the array
# Space Complexity: O(1) – constant space used

def maxProfit(prices):
    """
    Approach:
        - Use two pointers: `left` as the buying day, and `right` as the selling day.
        - Traverse the prices:
            - If prices[right] > prices[left], calculate profit and update max profit.
            - If prices[right] <= prices[left], move the buying day to right.
        - This ensures you always buy low and sell high in the future.
    """

    max_profit = 0
    left, right = 0, 1  # Left = buy day, Right = sell day

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right  # Shift buy day to a cheaper price
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
