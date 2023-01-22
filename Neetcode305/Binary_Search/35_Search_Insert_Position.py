# My solution
class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] == target or (nums[i] > target
                                     and nums[i - 1] < target):
                return i


# 也可以這樣寫
# for i in range(len(nums) - 1):
#             if nums[i] == target :
#                 return i
#             elif (nums[i] < target and nums[i + 1] > target):
#                 return i + 1


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l

    # 不管是大於最大值，或小於最小值，l都會變得大於r，所以return l...例子見neetcode影片
