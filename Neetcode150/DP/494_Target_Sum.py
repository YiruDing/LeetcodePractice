import collections
# 參考解答：
# https://buptwc.github.io/2018/07/03/Leetcode-494-Target-Sum/

# 參考解答二
# class Solution:

#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         dp = {}  # (index, total) -> # of ways

#         def backtrack(i, total):
#             if i == len(nums):
#                 return 1 if total == target else 0
#             if (i, total) in dp:
#                 return dp[(i, total)]

#             dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
#                 i + 1, total - nums[i])
#             return dp[(i, total)]

#         # No need to loop!

#         return backtrack(0, 0)

# A better one
# https://leetcode.com/problems/target-sum/discuss/97439/JavaPython-Easily-Understood


class Solution:

    def findTargetSumWays(self, nums, target):

        count = collections.Counter({0: 1})
        print("count: ", count)
        # count:  Counter({0: 1})
        for x in nums:
            step = collections.Counter()
            # print("step: ", step)
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            print("step: ", step)
            # step:  Counter({1: 1, -1: 1})
            # step:  Counter({1: 2, -1: 2})
            count = step
        return count[target]


tmp = Solution()
tmp.findTargetSumWays([1, 0], 1)

# ([1,1,1,1,1], 3)
# count:  Counter({0: 1})
# step:  Counter({1: 1, -1: 1}) 二種可能
# step:  Counter({0: 2, 2: 1, -2: 1}) 四種可能
# step:  Counter({1: 3, -1: 3, 3: 1, -3: 1}) 八種可能
# step:  Counter({0: 6, 2: 4, -2: 4, 4: 1, -4: 1}) 十六種可能
# step:  Counter({1: 10, -1: 10, 3: 5, -3: 5, 5: 1, -5: 1}) 三二種可能

# 3
# Try[1,0] target:1
# class Solution(object):
#     def findTargetSumWays(self, nums, S):
#         if not nums:
#             return 0
#         dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
#         # {1:1,0:1}
#         for i in range(1, len(nums)):
#             tdic = {}
#             for d in dic:
#                 tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
#                 # tdic[1+0]=tdic.get(1)+dic.get(1)=1+1=2
#                 tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
#                 # tdic[1-0]=tdic.get(1-0)+dic.get(0)=1+1=2
#             dic = tdic
#         return dic.get(S, 0)
# dic[1]

# To be fixed...
# You gotta go both way(+,-) to deal with array like [1,0]
# class Solution:

#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         res = 0
#         total = sum(nums)

#         if nums == [] or total < target or (len(nums) == 1
#                                             and nums[0] != target):
#             return 0

#         if len(nums) == 1 and nums[0] == target or total == target:
#             return 1

#         for i in range(len(nums)):
#             tmpSum = total

#             while tmpSum > target:
#                 tmpSum -= nums[i]
#                 if tmpSum == target:
#                     res += 1

#         return res
