# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

# Time Complexity: O(n)              # One pass through the prices array
# Space Complexity: O(1)             # No extra space used

def maxProfit(prices):
    """
    Approach:
        - Use a greedy approach to accumulate all profitable differences.
        - Loop through prices from day 1 to the end:
            - If today's price is greater than yesterday's, it means a profit opportunity.
            - Add the difference to total profit.
        - This simulates buying before every rise and selling at every peak.
        - Return the total profit collected from all such increases.
    """
    profit = 0

    for i in range(1, len(prices)):
        if prices[i - 1] < prices[i]:
            profit += prices[i] - prices[i - 1]  # Accumulate profit from every upward move

    return profit


def main():
    # Test - 1
    prices1 = [7,1,5,3,6,4]
    print(f"output-1: {maxProfit(prices1)}")

    # Test - 2
    prices2 = [1,2,3,4,5]
    print(f"output-2: {maxProfit(prices2)}")

    # Test - 3
    prices3 = [7,6,4,3,1]
    print(f"output-3: {maxProfit(prices3)}")

if __name__ == "__main__":
    main()
