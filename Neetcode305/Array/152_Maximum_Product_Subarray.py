class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            # Because we will need the previous curMax value ...
            curMin = min(tmp, n * curMin, n)
            result = max(result, curMax)
        return result