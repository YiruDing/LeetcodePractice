class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: (i[0], -i[1]))
        # 第二個value須取遞減的，但這不代表原本list被改囉！
        # sort by smallest left point and then the larger right point
        res = 0
        right = 0
        for start, end in intervals:
            res += end > right
            right = max(right, end)
        return res
