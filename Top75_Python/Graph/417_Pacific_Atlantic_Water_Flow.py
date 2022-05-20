# https://www.youtube.com/watch?v=s-VkcjHqkGI


class Solution:

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r == ROWS or c == COLS
                    or heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            # Check the top row
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        #  Check the lowest row

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            # Check the left most column
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
            # Check the right most column

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])
        return result
