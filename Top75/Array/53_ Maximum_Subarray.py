class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentSum = 0
        
        for n in nums:
            if currentSum < 0:
                currentSum = 0
                # What if there are only nagtive nums in this arr!?
                # That's why I think this is better...
                # https://www.youtube.com/watch?v=7J5rs56JBs8
            currentSum += n
            maxSub = max(currentSum,maxSub)
        return maxSub