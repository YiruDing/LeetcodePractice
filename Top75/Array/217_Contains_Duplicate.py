class Solution:
  def containsDuplicate(self, nums: list[int]) -> bool:
      hashset = set()
      
      for n in nums:
          if n in hashset:
              return True
          hashset.add(n)
      return False


# My JS solution
# var containsDuplicate = function(nums) {
#     let counter = {}
#     for(let i = 0; i < nums.length; i++){
#         let currentNum = nums[i] 
#         if(counter[currentNum] >= 1){
#             return true
#         }else{
#             counter[currentNum] = 1
#         }
        
#     }
#      return false
# };

