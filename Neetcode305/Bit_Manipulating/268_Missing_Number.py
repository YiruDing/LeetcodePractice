# My solution(贏過81.12趴):
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        listLen=len(nums)
        expectSum= listLen*(listLen+1)/2     
        return int(expectSum-sum(nums))
# My solution(贏過31趴):
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return nums[i]-1

# https://www.youtube.com/watch?v=WnPLSRLSANE
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result += (i - nums[i])
        
        return result
# e.g
# Sum([0,1,2,3])-Sum([0,1,3])