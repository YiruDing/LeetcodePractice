class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Decision Tree -> Cache ->DP
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        # https://www.youtube.com/watch?v=Sx9NNgInc3A
        # 7:53 If we are able to match till the end of the string...

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
                # We don't have to check again

        return dp[0]
