# Bottom up
# DP
# Neetcode 14:19
class Solution:

    def minDistance(self, word1: str, word2: str) -> int:

        cache = [[float("inf")] * (len(word2) + 1)
                 for i in range(len(word1) + 1)]

        #Below:initializing the base case
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1],
                                          cache[i + 1][j + 1])
            # delete(i+1,j)移動到word1的字母index
            # insert (i,j+1)移動到word2的字母index
            # replace(i+1,j+1)兩個字的字母index都有變動
        return cache[0][0]
