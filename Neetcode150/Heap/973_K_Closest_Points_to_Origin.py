class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
            # Python will sortthe first value by default

        heapq.heapify(minHeap)
        result = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            # K Closest Points 
            k -= 1

        return result