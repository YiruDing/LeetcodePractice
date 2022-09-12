# bottom up 為什麼省時很多？(50%)

class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        # 為了之後能update和return，有必要在外面宣告一個值
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
                # newRow[j + 1]為右方的值 row[j]為下方的值
            row = newRow
        return row[0]


# 順序
# 1
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j - 1] + aux[i - 1][j]
        return aux[-1][-1]


# 2 Ｔime complexity差好多耶(8%)！為什麼呢？
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1] if m and n else 0