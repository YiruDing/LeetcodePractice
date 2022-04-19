class Solution:
    def rob(self, nums: list[int]) -> int:
       
        return max(nums[0],self.helper(nums[1:]),self.helper[nums[:-1]])
    #  Why do we include nums[0]?Because there might just be 1 house
       
class Solution:
    def rob(self, nums: list[int]) -> int:
       
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    #  Why do we include nums[0]?Because there might just be 1 house
       
    def helper(self,nums):
        rob1,rob2=0,0
            
        for i in nums:
            temp = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        
        
        
        