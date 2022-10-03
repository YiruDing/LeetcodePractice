class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            # !!Look for the diagonal point對角線的點
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                # It x,y could't form the square or it's the same as ponit
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
            # 5:44
            # !!These are the other 2 points that could form the square!!
            # Consider that there might be duplicate...
        return res