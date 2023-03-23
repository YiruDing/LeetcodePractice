# Neetcode
# Do the  simultaneously dfs
class Solution:

    def countSubIslands(self, grid1: List[List[int]],
                        grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid2[r][c] == 0
                    or (r, c) in visited):
                return True

        # 這不代表grid2[r][c] == 0不能屬於subisland, 所以先return True,再用接下來的condition來做最後決定...

            visited.add((r, c))
            res = True
            if grid1[r][c] == 0:
                # 如果grid1[r][c]==0代表grid2[r][c]並非sub island
                res = False

            res = dfs(r - 1, c) and res
            res = dfs(r + 1, c) and res
            res = dfs(r, c + 1) and res
            res = dfs(r, c - 1) and res
            # 如果grid1[r][c]==0 代表 grid2[r][c]並非sub island
            # 為何不能寫成 res = dfs(r-1,c) and dfs(r+1,c) and dfs(r,c+1) and dfs(r,c-1) and res
            return res

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r, c) not in visited and dfs(r, c):
                    # dfs(r,c) means it has a corresponding island in grid1
                    count += 1
        return count