class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        # https://www.geeksforgeeks.org/defaultdict-in-python/
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        # 如果不加tuple,會出錯（unhashable type:list）
        # !!!Key必須為immutable
        # The Python "TypeError: unhashable type: 'list'" occurs when we use a list as a key in a dictionary or an element in a set. To solve the error, convert the list to a tuple, e.g. tuple(my_list) as list objects are mutable and unhashable.
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
            # !!difaultdic在此應該是有妙用！如果不存在，可以直接給個0
        return res