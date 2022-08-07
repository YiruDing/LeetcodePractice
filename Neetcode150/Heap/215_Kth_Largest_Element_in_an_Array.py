# 8/6 哇！我解開了！

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nn = [-n for n in nums]
        heapq.heapify(nn)

        while k > 1:
            heapq.heappop(nn)
            k -= 1
        return -nn[0]
    
# Neetcode
