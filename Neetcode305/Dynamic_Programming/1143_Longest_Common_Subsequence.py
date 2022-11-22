class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D matrix, bottum up
        # similiar:Leetcode 62
       dp = [[0 for j in range(len(text2) + 1)]
              for i in range(len(text1) + 1)]
    # if len(text2) =3,len(text1) =5
    #    [0,0,0]
    #    [0,0,0]
    #    [0,0,0]
    #    [0,0,0]
    #    [0,0,0]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                    # If you found the same letter,go diagonally
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
                    # Otherwise, check the number on either the right side or below
        return dp[0][0]
    
    # 2
     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]