# 8/6 哇！我解開了！
# 11/29 minHeap of size K


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nn = [-n for n in nums]
        heapq.heapify(nn)

        while k > 1:
            heapq.heappop(nn)
            k -= 1
        return -nn[0]


# Neetcode
class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        def __init__(self, k: int, nums: List[int]):
            self.minHeap = nums
            self.k = 
            heapq.heapify(self.minHeap)
            # 11/29 記得heapify!!
            while len(self.minHeap) > k:
                heapq.heappop(self.minHeap)

        def add(self, val: int) -> int:
            heapq.heappush(self.minHeap, val)
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)
            return self.minHeap[0]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # https://docs.python.org/3/library/heapq.html
        # heapq.heappush(heap, item)
        # Push the value item onto the heap, maintaining the heap invariant.
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)