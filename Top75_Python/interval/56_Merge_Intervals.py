class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        # !! Deal with the first value of the array
        output = [intervals[0]]
        # !! make it easier to update the second value of the inner array(s)
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            #    The first one will be the second value of intervals[0]...
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            #    Modify the second value if necessary
            else:
                output.append([start, end])
        return output
