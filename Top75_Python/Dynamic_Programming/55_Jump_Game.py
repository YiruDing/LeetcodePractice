class Solution:

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False


# My solution...
# To be fixed...
class Solution:

    def canJump(self, nums: List[int]) -> bool:
        res = [[False] * len(nums)]
        res[-1] = True
        for i in range(len(nums) - 1, -1, -1):
            if i - nums[i] > 0:
                n = nums[i]
                while n:
                    res[i - n] = True
                    # list assignment index out of range
                    n -= 1
        return res[0]
