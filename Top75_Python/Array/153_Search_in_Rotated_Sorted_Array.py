# https://www.youtube.com/watch?v=nIVW4P8b1VA

class Solution:
  
    def findMin(self, nums: list[int]) -> int:
      result = nums[0]
      l,r = 0, len(nums)-1
      
      while l <= r:
        if nums[l] < nums[r]:
          result = min(result,nums[l])
          break
        # If it's sorted...
        
        # Otherwise we gotta do the binary search
        middle = (l+r)//2
        result = min(result,nums[middle])
        if nums[middle] >= nums[l]:
          l = middle+1
        else:
          r = middle-1
      return result
    # Pay attention on the indentation...
      

# var findMin = function (nums) {
#   let middle = Math.round(nums.length / 2);
#   let min = nums[middle];

#   while (min < nums[middle + 1]) {
#     min = Math.min(min, nums[middle]);
#     middle += 1;
#   }
#   return min;
# };

#  But what if the right part is longer then the left?

