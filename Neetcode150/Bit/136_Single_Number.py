# n XOR 0 is going to ne n
# duplicate always cancel out
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for n in nums:
            res=n^res
        return res
    
    # My solution:
    # class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     if len(nums)==1:
    #         return nums[0]
        
    #     visit={}
        
    #     for i in nums:
    #         if i not in visit:
    #             visit[i]=1
    #         else:
    #             visit[i]+=1
        
    #     for i in visit:
    #         if visit[i]==1:
    #             return i