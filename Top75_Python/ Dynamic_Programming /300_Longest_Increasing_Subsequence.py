class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1]* len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            # From the end...
            for j in range(i+1, len(nums)):
                # Check every position backward
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i],1+LIS[j])
        return max(LIS)
        # The longest list (value??)