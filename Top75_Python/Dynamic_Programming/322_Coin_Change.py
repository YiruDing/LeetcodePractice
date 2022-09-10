# https://www.youtube.com/watch?v=H9bfqozjoqs


class Solution:

    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        # coins.sort(reverse=True) June 11時間沒有省太多耶...
        coins.sort(reverse=True)
        # Use the biggest number first

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != (amount + 1) else -1
