# Capture everything except the unsurrounded regions
# For example, the top/botton row and the most left/most right column

# 我的解答...目前還沒想通...為何不行呢？
# 8/15 你沒有call dfs啊！
# 而且要處理兩種不同的“Ｏ”（框框/內容）

#class Solution:
# def solve(self, board: List[List[str]]) -> None:
#     """
#     Do not return anything, modify board in-place instead.
#     """
#     ROWS=len(board)
#     COLS=len(board[0])
#     zero=set()

#     def dfs(r,c):
#         if r<0 or c<0 or r==ROWS or c==COLS or board[r][c]=="X" or (r,c) in zero:
#             return
#         zero.add((r,c))
#         dfs(r+1,c)
#         dfs(r-1,c)
#         dfs(r,c+1)
#         dfs(r,c-1)

#     for r,c  in zero:
#         for row in range(ROWS):
#             for col in range(COLS):
#                 if (row,c) not in zero or (r,col) not in zero:
#                     board[r][c]="X"

#     return board

# 1. (DFS) Capture unsurrounded regions(O->U)
# 2. Capture surrounded regions(O=>X)
# 3.Uncapture unsurrounded regions(U->O)


# Neetcode 解答：
class Solution:

    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1]
                                           or c in [0, COLS - 1]):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"


#8/15 solution:
class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        zero = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][
                    c] == "X" or (r, c) in zero:
                return
            zero.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1]
                                           or c in [0, COLS - 1]):
                    dfs(r, c)

        # for r,c  in zero:
        #     for row in range(ROWS):
        #         for col in range(COLS):
        #             if (row,c) not in zero or (r,col) not in zero:
        #                 board[r][c]="X"

        for row in range(ROWS):
            for col in range(COLS):
                if not (row, col) in zero:
                    board[row][col] = 'X'

        return board