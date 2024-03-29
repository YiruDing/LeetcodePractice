# https://www.youtube.com/watch?v=pV2kpPD66nE

# 547
# https://www.youtube.com/watch?v=YbCpAU5g0rg


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            # not recurssive. it's a iterative
            q = collections.deque()
            # https://www.geeksforgeeks.org/deque-in-python/
            visit.add((r, c))
            q.append((r, c))
            # https://blog.csdn.net/weixin_43790276/article/details/107749745

            while q:
                # !!Then we are going to expend the island
                row, col = q.popleft()
                # 11:20 Change to DFS? pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    # To check the value we just popped up...
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols)
                            and grid[r][c] == '1' and (r, c) not in visit):
                        q.append((r, c))
                        # So that we can explore its neighbor
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    # in Leetcode, it's a string instead of a number
                    bfs(r, c)
                    islands += 1

        return islands

# DFS
Status
Problem	
Difficulty
Video Solution
Code
Number of Islands	
Clone Graph	
Max Area of Island	
Pacific Atlantic Water Flow	
Surrounded Regions	
Rotting Oranges	
Walls And Gates	
Course Schedule	
Course Schedule II	
Redundant Connection	
Number of Connected Components In An Undirected Graph	
Graph Valid Tree	
Word Ladder	
View on Github
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands