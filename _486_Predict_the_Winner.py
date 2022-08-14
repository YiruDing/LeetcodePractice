class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
# JS version
# var PredictTheWinner = function(nums) {
#     const winner=(nums,start,end)=>{
#         if(start===end) return nums[start]
#         let a = turn * nums[start]+ winner(nums,start+1,end)
#         let b = turn * nums[end]+winner(nums,start,end-1)
#         return turn * Math.max(turn*a,turn*b)
#     }
#     return winner(nums,0,nums.lenth-1)>=0
# };