# Haven't run yet...

# https://www.lintcode.com/problem/919/
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    # What if [5,10][10,15]?
    # +=1
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        result = 0
        count = 0
        s = 0
        e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
                # there would be 1 meeting
            else:
                e += 1
                # 有一間會議室空出來了
                count -= 1
            result = max(result, count)
        return result
# 另解
 def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x: x[0])    # sort the intervals
        res = 0
        heap, heap_size = [], 0         # heap of meeting ending times
        for interval in intervals:      # move the vertical line from left to right
		    # pop all ended meetings from the heap
            while heap and heap[0] <= interval[0]:
                # heap[0]是最近的end time
                heapq.heappop(heap)
                heap_size -= 1
            heapq.heappush(heap, interval[1])
            heap_size += 1
            res = max(res, heap_size)
        return res