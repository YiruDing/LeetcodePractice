# https://www.youtube.com/watch?v=WnPLSRLSANE
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result += (i - nums[i])
        
        return result
# e.g
# Sum([0,1,2,3])-Sum([0,1,3])