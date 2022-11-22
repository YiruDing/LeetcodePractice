# https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
# https://www.adamsmith.haus/python/answers/how-to-use-a-max-heap-in-python

#!!!我的問題：8/6 用 _heapify_max和_heappop_max，反而跑不出答案...Why???
# 8/8 JM 因為沒有搭配的_heappush_max啊！


# Get the MAX heap
class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
                # heapq.heappush(heap, item)
        stones.append(0)
        # "At the end,there is at most 1 stone left.Return its weight"
        # To handle the eade case
        # (that the stones is empty)
        return abs(stones[0])

    # because we *-1 in the begining
