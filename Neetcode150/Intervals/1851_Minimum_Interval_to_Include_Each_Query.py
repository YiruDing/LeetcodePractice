class Solution:

    def minInterval(self, intervals: List[List[int]],
                    queries: List[int]) -> List[int]:

        intervals.sort()
        minHeap = []
        res = {}  #A hashMap to be vonverted to a list later.
        i = 0

        for q in sorted(queries):
            # 1
            # Customize the minHeap
            while i < len(intervals) and intervals[i][0] <= q:
                # Adding intervals as long as q is bigger than the left value of the inner list/array
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
                # 2
                # Pop the invalid value from the minHeap until get the one
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
            # 轉為list,並按照原本順序呈現
        return [res[q] for q in queries]
