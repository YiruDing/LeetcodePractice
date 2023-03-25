# BFS from multiple source, just like Rotting orange
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = collections.deque()

        # FIFO

        def addRooms(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit
                    or rooms[r][c] == -1):
                # 3/24 勿忘rooms[r][c]== -1
                return
            visit.add((r, c))
            q.append([r, c])

        # install the (r,c) of the gates as the start points
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    # the gate to start
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                # 3/24 記得這行！
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1
