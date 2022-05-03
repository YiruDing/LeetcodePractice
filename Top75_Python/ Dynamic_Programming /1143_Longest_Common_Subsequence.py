class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D matrix, bottum up
        # similiar:62
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
                    # go diagonally
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]
