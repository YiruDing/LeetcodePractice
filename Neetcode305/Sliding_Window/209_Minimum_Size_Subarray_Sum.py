# Sliding window


class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")

        for i in range(len(nums)):
            total += nums[i]
            # 10/26 這行不要放錯地方囉
            while total >= target:
                res = min(i - l + 1, res)
                # 10/26 這行不要放錯地方囉...要先記錄下來目前的狀況，再去update
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res
