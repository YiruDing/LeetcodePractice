class SeatManager:

    def __init__(self, n: int):  # O(n)
        self.unres = [i for i in range(1, n + 1)]
        # 1 minHeap for the unreserved table(s)
        # 亦可作self.unres = list(range(1, n + 1))
    def reserve(self) -> int:
        return heapq.heappop(self.unres)
        # O(nlogn)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unres, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)