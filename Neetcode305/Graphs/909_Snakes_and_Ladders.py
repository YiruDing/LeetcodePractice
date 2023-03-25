# 12/3 本題難處在於座標和數字中間不斷進行換算....
class Solution:

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        # https://www.programiz.com/python-programming/methods/list/reverse
        # 從這樣：[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
        # 變這樣： [[-1, 15, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1]]

        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            # 12/5 length!!
            if r % 2:
                c = length - 1 - c
                # 12/3: 是r % 2！！
            return [r, c]

        q = deque()
        q.append([1, 0])  #[sqaure, moves（How many steps it take to get here）]
        visit = set()
        # 12/3 要存nextSquare！！！
        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                nextSquare = square + i
                # !!12/5 紀錄擲骰子可能出現的所有可能
                r, c = intToPos(nextSquare)
                #12/3 ;!!!算出"接下來"可能的位置
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    # 是nextSquare而非board[r][c]
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1


# 看不懂的解答...
class Solution:

    def snakesAndLadders(self, board):
        arr, nn, q, seen, moves = [0], len(board)**2, [1], set(), 0
        for i, row in enumerate(board[::-1]):
            arr += row[::-1] if i % 2 else row
        while q:
            new = []
            for sq in q:
                if sq == nn: return moves
                for i in range(1, 7):
                    if sq + i <= nn and sq + i not in seen:
                        seen.add(sq + i)
                        new.append(sq + i if arr[sq + i] == -1 else arr[sq +
                                                                        i])
            q, moves = new, moves + 1
        return -1


# 另解
class Solution(object):

    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        board_2 = [0]
        rows, cols = len(board), len(board[0])
        row = rows - 1

        while row >= 0:
            for col in range(cols):
                board_2.append(board[row][col])
            row -= 1
            if row >= 0:
                for col in range(cols - 1, -1, -1):
                    board_2.append(board[row][col])
                row -= 1

        visited = [0 for i in range(len(board_2))]
        stack = collections.deque()
        #stack = []
        stack.append([1, 0])
        while stack:
            curr_ind, curr_dist = stack.popleft()
            for i in range(1, 7):
                next_ind = min(rows * cols, curr_ind + i)
                if board_2[next_ind] != -1:
                    next_ind = board_2[next_ind]
                if next_ind == rows * cols:
                    return curr_dist + 1
                if visited[next_ind] == 0:
                    visited[next_ind] = 1
                    stack.append([next_ind, curr_dist + 1])

        return -1


'''
convert board to 2d
keep visited list initalize all to false
create stack - vertex and distance, intialize it
logic for bfs starting from node 1
'''