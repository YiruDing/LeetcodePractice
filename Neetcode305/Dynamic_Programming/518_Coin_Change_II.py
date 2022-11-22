# https://github.com/neetcode-gh/leetcode/blob/main/518-coin-change-2.py


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        # MEMOIZATION
        # Time: O(n*m)
        # Memory: O(n*m)
        cache = {}

        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            # dfs(i, a + coins[i])是要update這格的amount
            # dfs(i + 1, a)是把下方的值加進來
            return cache[(i, a)]

        return dfs(0, 0)

        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n*m)
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        # 9/12???
        dp[0] = [1] * (len(coins) + 1)
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                # 9/12 "inherit" from the right?
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
                # update with the value in the difference
                # Backtracking
        return dp[amount][0]

        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n) where n = amount
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                # store the value and explore the next one
                # Cause we do one row at a time, the space complexity could be smaller
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]
