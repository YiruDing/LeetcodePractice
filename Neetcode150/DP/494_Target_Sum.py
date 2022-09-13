# 參考解答：
# https://buptwc.github.io/2018/07/03/Leetcode-494-Target-Sum/


# 參考解答二
class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i])
            return dp[(i, total)]

        return backtrack(0, 0)


# To be fixed...
class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        total = sum(nums)

        if nums == [] or total < target or (len(nums) == 1
                                            and nums[0] != target):
            return 0

        if len(nums) == 1 and nums[0] == target or total == target:
            return 1

        for i in range(len(nums)):
            tmpSum = total

            while tmpSum > target:
                tmpSum -= nums[i]
                if tmpSum == target:
                    res += 1

        return res
