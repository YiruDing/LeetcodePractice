# 可參考array27


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r - 1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l