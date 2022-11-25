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
