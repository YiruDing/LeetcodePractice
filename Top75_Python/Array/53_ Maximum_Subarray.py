class Solution:

    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        currentSum = 0

        for n in nums:
            if currentSum < 0:
                currentSum = 0
                # What if there are only nagtive nums in this arr!?
                # That's why I think this is better...
                # https://www.youtube.com/watch?v=7J5rs56JBs8
            currentSum += n
            maxSub = max(currentSum, maxSub)
        return maxSub


# JS solution: https://www.youtube.com/watch?v=WdK1Uhsza_I
# function maxSubArr(nums){
#     let solution = nums[0]
#     for(let i = 1; i < nums.length; i++){
#         nums[i] = Math.max(nums[i]+ num[i-1], num[i]);
#         solution = Math.max(solution, nums[i])
#    //This is how we accumulate current value(with solution)
#    // Don't set a currentSum to hold nums[i]
#    // It would just store the wrong value
#     }
#     return solution
# }