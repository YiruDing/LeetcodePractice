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
        # 2/7 為何要加board而不能直接return呢？

        directions = [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1),
                      (0, -1), (0, 1)]

        # 2/7 為何不能 directions: = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        # invalid syntax
        def dfs(r, c):
            if board[r][c] != 'E':
                return
            # 2/7 別忘上兩行！

            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    # 2/7 不是while!!
                    if board[nr][nc] == 'M':
                        count += 1
                    # 不必加減一到八的數字！
            if count > 0:
                # 2/7 loop 完才加的！
                board[r][c] = str(count)
                return
            # 2/7 記得這裡return
            # 如果count == 0,註記為‘B’
            board[r][c] = 'B'

            for dr, dc in directions:
            # 這是在dfs內的！
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    # 2/7 不是while!!
                    dfs(nr, nc)

        dfs(r, c)
        return board
