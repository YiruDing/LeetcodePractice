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


# My to-be-fixed solution:
#     result = 1

#     for i in range(0,culen(nums)):
#         if nums[i] == 0:
#             result = 1

#         result = max(result, nums[i - 1] * nums[i],nums[i])

#     return result
