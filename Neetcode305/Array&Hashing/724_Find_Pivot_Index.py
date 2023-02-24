class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums) 
        #會花O(n) time 反正這本來就是要花的

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1