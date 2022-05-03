class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Decision Tree -> Cache ->DP(button-up approach) less than hasing
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        # https://www.youtube.com/watch?v=Sx9NNgInc3A
        # 7:53 If we are able to match till the end of the string...

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # Faster then checking each and every letter in s
                if (i + len(w) <= len(s)) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                    # We could change the index/pointer and check the letter/word after this word 
                if dp[i]:
                    break
                # We don't have to check again

        return dp[0]
    # See if we can break the word starting from the very begining
