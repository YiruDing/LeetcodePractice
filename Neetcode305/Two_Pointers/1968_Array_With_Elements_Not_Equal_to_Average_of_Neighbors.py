# Neetcode
# 可以用間隔的方式來insert list
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        l, r = 0, len(nums) - 1
        while len(res) != len(nums):
            res.append(nums[l])
            l += 1
            if l <= r:
                res.append(nums[r])
                r -= 1
        return res
    
#  O(1) space 
 class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Algorithm: Time = O(n); Space = O(1); Algo Credits @bangoc
        # 1. We don't want any ascending or descending patterns among 
        #    3 consequtive elements, so we need to break them by swapping
        # 2. Get the 3 elements, (prev, cur, nxt)
        # 3. If these three are in ascending or descending order
        #    i,e. prev < cur < nxt or prev > cur > nxt
        #    then swap the cur and nxt elements
        # 4. Repeat this for entire array

        def swap(l, r):
            nums[l], nums[r] = nums[r], nums[l]
            
        n = len(nums)
        for i in range(1, n-1):
            prev, cur, nxt = nums[i-1], nums[i], nums[i+1]

            if prev < cur < nxt or prev > cur > nxt:
                swap(i+1, i)
                
        return nums

#    下面這個解法不行...因為[1,7,5,3] Expected:[5,1,7,3]
    #     nums.sort()
    #     r = len(nums) - 1
    #     l = 0
    #     for i in range(1, len(nums) - 1):
    #         if nums[i] * 2 == nums[i - 1] + nums[i + 1]:
    #             nums[i], nums[r] = nums[r], nums[i]
    #             r -= 1
            
    #     if nums[-2] * 2 == nums[-3] + nums[-1]:
    #         nums[0], nums[-1] = nums[-1], nums[0]
    #     return nums
   
