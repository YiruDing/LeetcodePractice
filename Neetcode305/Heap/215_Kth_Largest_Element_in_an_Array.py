# 8/6 哇！我解開了！
# 11/29 minHeap of size K
# 12/6 題目從int改為str所以解答調整了


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nn = [-1 * int(n) for n in nums]
        heapq.heapify(nn)

        while k > 1:
            heapq.heappop(nn)
            k -= 1
        return str(-nn[0])


# Neetcode1


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)


# Neetcode2
class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        def __init__(self, k: int, nums: List[int]):
            self.minHeap = nums
            self.k = k
            heapq.heapify(self.minHeap)

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