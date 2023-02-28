class Solution:

    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = float('inf')
        if len(nums) == 1:
            return 0
        nums.sort()
        l, r = 0, k - 1
        # Cause we want the window to be (of) the size k
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1

        return res