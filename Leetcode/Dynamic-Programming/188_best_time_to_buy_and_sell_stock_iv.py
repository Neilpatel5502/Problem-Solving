# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

from functools import lru_cache

# Time Complexity: O(n * 2 * k) = O(n), where n is the length of prices
# Space Complexity: O(n * 2 * k) due to memoization
def maxProfit_top_down(k, prices):
    """
    Approach:
        - Use recursion with memoization to try all possible decisions at each day.
        - At any day `i`, we can either buy, sell, or skip depending on our current state.
        - The `buy` flag tells if we are allowed to buy (True) or need to sell (False).
        - `cap` is the number of transactions (max k) we can perform.
        - Base case: if we reach the end of the array or cap is 0, return 0.
        - Recurrence:
            - If we can buy:
                - Either buy the current stock and subtract its price, or skip.
            - If we need to sell:
                - Either sell and add the price, decreasing cap, or skip.
    """

    if not prices:
        return 0

    n = len(prices)

    @lru_cache
    def dfs(i, buy, cap):
        # Base case: no more days or no more transactions
        if i == n or cap == 0:
            return 0

        profit = 0
        if buy:
            # Option 1: Buy the stock today
            take = -prices[i] + dfs(i + 1, False, cap)
            # Option 2: Skip buying today
            not_take = dfs(i + 1, True, cap)
            profit = max(take, not_take)
        else:
            # Option 1: Sell the stock today
            take = prices[i] + dfs(i + 1, True, cap - 1)
            # Option 2: Skip selling today
            not_take = dfs(i + 1, False, cap)
            profit = max(take, not_take)

        return profit

    return dfs(0, True, k)


# Time Complexity: O(n * 2 * k) = O(n), where n is the number of days
# Space Complexity: O(n * 2 * k) = O(n), for the 3D DP table
def maxProfit_bottom_up(k, prices):
    """
    Approach:
        - Use bottom-up dynamic programming with tabulation.
        - Create a 3D DP table where:
            - `dp[i][buy][k]` represents the max profit from day `i` with:
                - `buy = 1` if we can buy, `0` if we need to sell
                - `k` remaining transactions
        - Initialize all dp values with 0 (base case: profit is 0 when day == n).
        - Iterate backwards through the days to fill the table:
            - If in buy state:
                - Choose to buy the stock or skip
            - If in sell state:
                - Choose to sell the stock or skip
        - Final answer is at dp[0][1][k] — start at day 0, in buy state, with k transactions allowed.
    """

    n = len(prices)
    dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n + 1)]

    # Fill the table from day n-1 down to 0
    for i in range(n - 1, -1, -1):
        for buy in range(2):
            for cap in range(1, k + 1):  # transaction capacity from 1 to k
                if buy:
                    # Option 1: Buy the stock today and switch to sell state
                    # Option 2: Skip buying today
                    dp[i][buy][cap] = max(
                        -prices[i] + dp[i + 1][0][cap],
                        dp[i + 1][1][cap]
                    )
                else:
                    # Option 1: Sell the stock today and use up one transaction
                    # Option 2: Skip selling today
                    dp[i][buy][cap] = max(
                        prices[i] + dp[i + 1][1][cap - 1],
                        dp[i + 1][0][cap]
                    )

    return dp[0][1][k]



def main():
    # Test - 1
    k1 = 2
    prices1 = [2,4,1]
    maxProfit_bottom_up
    print(f"Top-Down output-1: {maxProfit_top_down(k1, prices1)}")
    print(f"Bottom-Up output-1: {maxProfit_bottom_up(k1, prices1)}\n")

    # Test - 2
    k2 = 2
    prices2 = [3,2,6,5,0,3]
    print(f"Top-Down output-2: {maxProfit_top_down(k2, prices2)}")
    print(f"Bottom-Up output-2: {maxProfit_bottom_up(k2, prices2)}")

if __name__ == "__main__":
    main()
