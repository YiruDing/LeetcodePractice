# https://www.youtube.com/watch?v=73r3KWiEvyk

class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0,0
        
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            # So that in the next loop, we'll get the n+rob2
            rob2 =temp
            # Store the max value
        return rob2



# My JS solution:

# var rob = function(nums) {
#     let maxA=0
#     let maxB=0
  
#     for(let i = 0; i < nums.length; i+=2){
#         maxA += nums[i]
#     }
    
#     for(let i = 1; i < nums.length; i+=2){
#         maxB += nums[i]
#     }
    
#     return maxA > maxB? maxA:maxB
# };