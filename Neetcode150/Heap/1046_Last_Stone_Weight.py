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
        stones.append(0)
        # "At the end,there is at most 1 stone left.Return its weight"
        # To handle the eade case(that the stones is empty)
        return abs(stones[0])

    # because we *-1 in the begining
