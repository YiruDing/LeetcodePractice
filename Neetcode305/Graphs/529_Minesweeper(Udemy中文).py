# https://www.youtube.com/watch?v=zPmuqLKPbE8


class Solution:

    def updateBoard(self, board: List[List[str]],
                    click: List[int]) -> List[List[str]]:
        r, c = click
        rows = len(board)
        cols = len(board[0])

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        directions = [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1),
                      (0, -1), (0, 1)]

        def dfs(r, c):
            if board[r][c] != 'E':
                return

            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == 'M':
                        count += 1
            if count > 0:
                board[r][c] = str(count)
                return
            # 如果count == 0,註記為‘B’
            board[r][c] = 'B'

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc)

        dfs(r, c)
        return board
