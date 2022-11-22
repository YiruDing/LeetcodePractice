class Solution:

    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        # n是上限
        res = 0

        while l <= r:
            mid = (l + r) // 2
            # 來算算 1,2,3,...mid的總和
            if mid / 2 * (mid + 1) > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res