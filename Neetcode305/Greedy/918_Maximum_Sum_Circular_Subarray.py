# Neetcode
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        # 用此來儲存某個位數或是某段的值
        total = 0

        for n in nums:
            curMax = max(n, curMax + n)
            curMin = min(n, curMin + n)
            total += n
            globalMax = max(curMax, globalMax)
            globalMin = min(curMin, globalMin)
        return max(globalMax, total -
                   globalMin) if globalMax > 0 else globalMax
        # total - globalMin 意味著截斷一部分的總和，這在circlalar subarray裡面是可以這樣做的
        # 如果globalMax <= 0, 那就return 某個/某段的值