# Neetcode 3:02 解釋為何可以從list轉pragh, 就會往右一格
class Solution:

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])

        def posToVal(r, c):
            # 2-D to 1-D
            return r * N + c

        def valToPos(v):
            # 1-D to 2-D
            return [v // N, v % N]  # r, c

        # 3/6 不是Ｍ喔！

        res = [[0] * N for i in range(M)]
        for r in range(M):
            for c in range(N):
                newVal = (posToVal(r, c) + k) % (M * N)
                # + k!!
                # % (M * N)：make sure it will not out of the grid
                newR, newC = valToPos(newVal)
                res[newR][newC] = grid[r][c]
                # 3/6 別寫反啦！
        return res
