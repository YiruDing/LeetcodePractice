class Solution:

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res = 1
        # 記得res的起始值為1!
        prev = ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                # time to reset
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                # 3/14 記得l = r - 1
                prev = ""
        return res