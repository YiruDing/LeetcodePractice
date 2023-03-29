class Solution:

    def findMin(self, nums: list[int]) -> int:
        result = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            middle = (l + r) // 2
            result = min(result, nums[middle])
            if nums[middle] >= nums[l]:
                l = middle + 1
            else:
                r = middle - 1
            # result = min(result, nums[middle])亦可放這裡
        return result
