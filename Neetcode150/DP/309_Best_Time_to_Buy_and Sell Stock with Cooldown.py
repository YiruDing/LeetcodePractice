# The tricky part is that we can cooldown anytime...
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  #key=(i,buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            # The cooldown state
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                # in Python, not ... can return a booleen
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)
    
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/466271/Python-DP-beat-99-with-detail-explanation
    # HS[i]  max profit at day i, if holding stock after market closes.
# NHS[i] max profit at day, if not holding stock after market closes
# NHS_CD:  NHS cooldown
    class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        HS = -prices[0]
        NHS = NHS_CD = 0
        for p in prices:
            cur_HS = max(HS, NHS-p)
            cur_NHS = max(NHS_CD, HS+p)
            HS = cur_HS
            NHS, NHS_CD = NHS_CD, cur_NHS
        return NHS_CD
