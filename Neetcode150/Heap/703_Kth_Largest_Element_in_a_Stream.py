# Stream?
# In computer science, a stream is a sequence of data elements made available over time. A stream can be thought of as items on a conveyor belt being processed one at a time rather than in large batches

# https://www.tibco.com/reference-center/what-is-data-streaming
# ????為什麼the stream data might be a mix of different formats，
# 但Ｎeetcode卻可以直接把它當array來使用


# build the min heap of size k
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        # array 轉heap
        # https://docs.python.org/3/library/heapq.html
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
# Pop and return the smallest item from the heap,

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