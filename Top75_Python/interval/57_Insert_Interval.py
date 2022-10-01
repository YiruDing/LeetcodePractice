class Solution:

    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                #    They don't overlap
                result.append(newInterval)
                return result + intervals[i:]
            
            elif newInterval[0] > intervals[i][1]:
                #    They don't overlap,either
                result.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        result.append(newInterval)
        #    Deal with the case that newInterval[0]>intervals[-1][1] Or when input = [] [5,7]
        # just in case you get duplicate...
        # line 11 already return the result
        # line 17-20 only modify the newInterval
        return result
