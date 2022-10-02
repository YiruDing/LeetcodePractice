import heapq
from collections import OrderedDict

# My solution...
# To be fixed...


class Solution:

    def minInterval(self, intervals, queries):

        size = {}
        res = []

        for i in range(len(intervals)):
            left, right = intervals[i][0], intervals[i][1]
            # 10/1 ？？？本來寫成這樣
            #   for i, v in enumerate(intervals):
            # left, right = intervals[v][1], intervals[v][0]
            # 結果出問題：
            # The Python "TypeError: list indices must be integers or slices, not list"
            # https://stackoverflow.com/questions/30890707/python-typeerror-list-indices-must-be-integers-not-list
            if right - left + 1 not in size:
                size[right - left + 1] = [(right - left + 1, right)]
            else:
                size[right - left + 1].append((right - left + 1, right))
            # 這個問題是，如果同size，只能儲存一個值
        OrderedDict(sorted(size.items()))
        # https://stackoverflow.com/questions/22264956/how-to-sort-dictionary-by-key-in-numerical-order-python

        # size長這樣 {4: [(1, 4), (3, 6)], 3: [(2, 4)], 1: [(4, 4)]}

        for j in range(len(queries)):
            currentRes = []
            for i in range(len(size)):
                if queries[j] <= intervals[i][1] and queries[j] >= intervals[
                        i][0]:
                    key = intervals[i][1] - intervals[i][0] + 1
                    currentRes.append(size[key][0])
                    # 如果是res.append(),變成所有可能的解都存下來了...
                res.append(min(currentRes))
                print("res in my solution: ", res)

        return res


# res in my solution:  [(4, 4)]
# res in my solution:  [(4, 4), (3, 4)]
# res in my solution:  [(4, 4), (3, 4), (3, 4)]
# res in my solution:  [(4, 4), (3, 4), (3, 4), (4, 4)]
# res in my solution:  [(4, 4), (3, 4), (3, 4), (4, 4), (3, 4)]
# res in my solution:  [(4, 4), (3, 4), (3, 4), (4, 4), (3, 4), (3, 4)]
# res in my solution:  [(4, 4), (3, 4), (3, 4), (4, 4), (3, 4), (3, 4), (4, 4)]
# res in my solution:  [(4, 4), (3, 4), (3, 4), (4, 4), (3, 4), (3, 4), (4, 4), (3, 4)]
# res in my solution:  [(4, 4), (3, 4), (3, 4), (4, 4), (3, 4), (3, 4), (4, 4), (3, 4), (3, 4)]

# class Solution:

    def minInterval(self, intervals, queries):
        intervals.sort()
        minHeap = []
        res, i = {}, 0
        for q in sorted(queries):
            # !!!ㄧ定要sorted
            # 否則[[2,3],[2,5],[1,8],[20,25]],[2,19,5,22]的答案會變成[2,-1,-1,6]而非[2,-1,4,6]
            # 10/1 但是為什麼呢...
            while i < len(intervals) and intervals[i][0] <= q:
                # 收納所有可能的值
                left, right = intervals[i]
                heapq.heappush(minHeap, (right - left + 1, right))
                # (sizeOftheArr,rightValue)
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
            print("res[q]:", res[q])
            print("res:", res)
        return [res[q] for q in queries]

tmp = Solution()
tmp.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5])
# res[q]: 3
# res: {2: 3}
# res[q]: 3
# res: {2: 3, 3: 3}
# res[q]: 1
# res: {2: 3, 3: 3, 4: 1}
# res[q]: 4
# res: {2: 3, 3: 3, 4: 1, 5: 4}