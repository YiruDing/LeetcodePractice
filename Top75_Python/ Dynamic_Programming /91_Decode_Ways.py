class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            # 跟DP不同處，在於有res儲值
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            # 最後update dp[i]的職為res
            dp[i] = res
            return res

        return dfs(0)

# Dynamic Programming
# Similar to House Robber
class Solution:
    def numDecodings(self, s: str) -> int:
      dp={len(s):1}
      
    #   If we do the recursion,than this is the Base case
    # Otherwise it would be a cache
        # mapping
        
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                dp[i]=0
                # We cannot include 0
            else:
                dp[i]=dp[i+1]
                
            if(i+1<len(s) and (s[i]=='1' or s[i]=='2' and s[i+1] in '0123456')):
                # A or B(s[i]=='2' and s[i+1] in '0123456')
                # Then we can go further
                dp[i]+=dp[i+2]
        
        return dp[0]