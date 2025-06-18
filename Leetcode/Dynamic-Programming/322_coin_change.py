# Problem: https://leetcode.com/problems/coin-change

from functools import lru_cache

# Time Complexity: O(amount * len(coins)) → Memoization ensures we compute each total_sum at most once
# Space Complexity: O(amount)             → For recursion stack and memoization cache
def coinChange_top_down(coins, amount):
    """
    Approach:
        - Use top-down recursion with memoization to minimize overlapping calculations.
        - At each step, try taking each coin and recurse with the updated sum.
        - If a path leads to the target amount, return the number of coins used.
        - Use cache to avoid recomputation for the same subproblem (total_sum).
    """
    @lru_cache
    def dfs(total_sum):
        # Base case: if we reach the exact amount, no more coins are needed
        if total_sum == amount:
            return 0

        # Initialize min_coins as infinity to track minimum required
        min_coins = float('inf')

        # Try using each coin if it doesn't exceed the amount
        for c in coins:
            if c + total_sum <= amount:
                # Recursively calculate the coins needed after using coin `c`
                min_coins = min(min_coins, 1 + dfs(c + total_sum))

        # Return the best option found for this total_sum
        return min_coins

    # Start recursion from sum = 0
    out = dfs(0)

    # If no solution found, return -1
    return -1 if out == float('inf') else out


# Time Complexity: O(amount * n), where n is the number of coins
# Space Complexity: O(amount)
def coinChange_bottom_up(coins, amount):
    """
    Approach:
        - Use bottom-up dynamic programming starting from the target amount.
        - dp[i] represents the minimum number of coins needed to reach amount `i`.
        - Initialize dp[amount] = 0, as 0 coins are needed to form amount itself.
        - Iterate backwards from amount to 0 and update the dp table by subtracting each coin.
        - At the end, dp[0] will hold the minimum number of coins required to make the amount.
        - If dp[0] is still infinity, return -1 as it's not possible to form the amount.
    """
    dp = [float('inf')] * (amount + 1)  # Initialize DP table with infinity
    dp[amount] = 0                      # Base case: 0 coins needed to form 'amount'

    # Traverse backwards from 'amount' to 0
    for total in range(amount, -1, -1):
        if dp[total] == float('inf'):
            continue  # Skip if this total is not reachable

        for c in coins:
            next_total = total - c
            if next_total >= 0:
                # Update dp[next_total] with minimum coins needed
                dp[next_total] = min(dp[next_total], 1 + dp[total])

    out = dp[0]  # Minimum coins needed to form original amount
    return -1 if out == float('inf') else out


def main():
    # Test 1:
    coins1 = [1, 2, 5]
    amount1 = 11

    print(f"Top- Down output-1: {coinChange_top_down(coins1, amount1)}")
    print(f"Bottom-UP output-1: {coinChange_bottom_up(coins1, amount1)}\n")

    # Test 2:
    coins2 = [2]
    amount2 = 3

    print(f"Top- Down output-2: {coinChange_top_down(coins2, amount2)}")
    print(f"Bottom-UP output-2: {coinChange_bottom_up(coins2, amount2)}\n")

    # Test 3:
    coins3 = [1]
    amount3 = 0

    print(f"Top- Down output-3: {coinChange_top_down(coins3, amount3)}")
    print(f"Bottom-UP output-3: {coinChange_bottom_up(coins3, amount3)}")

if __name__ == "__main__":
    main()
