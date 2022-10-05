class Solution:

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False


# My solution...
# To be fixed...
# class Solution:

#     def canJump(self, nums: List[int]) -> bool:
#         res = [[False] * len(nums)]
#         res[-1] = True
#         #舉例來說 [2,3,1,0,4]
#         for i in range(len(nums) - 2, -1, -1):
#             if i - nums[i] > 0:
#                 # 3>0
#                 n = nums[i]
#                 #如果n=0就跑不動了
#                 while n:
#                     res[i - n] = True
#                     # Leetcode 回傳的訊息是 list assignment index out of range…
#                     n -= 1
#         return res[0]
