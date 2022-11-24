# 10:12
class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            # Add 2 lines above !

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                    or word[i] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))
            result = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(
                r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r, c))
            # 7:45 the reason of cleaning up (r,c)
            return result

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True

        return False
