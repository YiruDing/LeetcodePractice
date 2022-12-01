class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
            # Python will sort the first value by default

        heapq.heapify(minHeap)
        result = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            # K Closest Points
            k -= 1

        return result


# Leetcode 另解(11/29 這個比較好！)
# Maintain a heap with length K, with maximum distance element stored on top
# Since python api is min-heap, we use negative distance here
# When the heap reaches length K, if next distance is smaller than current largest distance, the top element could be updated
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []

        for i, j in points:
            x = i * i + j * j

            if len(res) < k:
                heapq.heappush(res, (-x, [i, j]))
            else:
                heapq.heappushpop(res, (-x, [i, j]))

        return [x[1] for x in res]