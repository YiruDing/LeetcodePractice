# https://www.youtube.com/watch?v=ykQ6WFuqQfE

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('inf')
        # https://www.geeksforgeeks.org/python-infinity/
        profit1=0
        buy2=float('inf')
        profit2=0
        
        for price in prices:
            buy1 = min(buy1,price)
            profit1=max(profit1,price-buy1)
            buy2 = min(buy2,price-profit1)
            profit2=max(profit2,price-buy2)
            
        return profit2
    
    # https://www.youtube.com/watch?v=1zxgH-YVBbw
    
    # https://last2win.com/2020/01/30/LeetCode-123-Best-Time-to-Buy-and-Sell-Stock-III/?fbclid=IwAR22pSJ4vUqN6Zq_8_h-wVPMgDNnbHwO0zKf-3LIanS2GsNVa_uzys1Rd1E