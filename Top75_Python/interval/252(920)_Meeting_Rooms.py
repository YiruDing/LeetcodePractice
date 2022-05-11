# https://www.lintcode.com/problem/920/

# https://www.youtube.com/watch?v=PaJxqZVPhbg

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# Leetcode 252
# Lintcode 920
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals):
        intervals.sort(key=lambda i:i.start)
        # Sorted by the start time
        
        for i in range(1,len(intervals)):
            i1=intervals[i-1]
            i2=intervals[i]
            
            if i1.end > i2.start:
                return False
            
        return True
        
    
