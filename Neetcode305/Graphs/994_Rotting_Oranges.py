# 難在multi source BFS
# BFS(So that we can do the search  simultaneously...)及其夥伴Ｑueue

from collections import deque


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    # elif也沒差
                    q.append([r, c])
                    # Or ((r,c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # 亦可作（[0, 1], [0, -1], [1, 0], [-1, 0]）
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                # 不是處理新加的！是處理之前的，所以要popleft
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == len(grid) or col < 0
                            or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    # make sure it's in bounds and it's a fresh orange(1)
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            # input:[[2,1,1],[1,1,0],[0,1,1]]
            # 這裡的q分別長這樣：
                              # q: deque([[1, 0], [0, 1]])
                              # q: deque([[1, 1], [0, 2]])
                              # q: deque([[2, 1]])
            time += 1
            # 問題：這個位置是for i in range(len(q)) loop結束之後跳出來的？
            # 答案：對。把一批次的q解決掉，再處理第二批次的q...
        return time if fresh == 0 else -1
