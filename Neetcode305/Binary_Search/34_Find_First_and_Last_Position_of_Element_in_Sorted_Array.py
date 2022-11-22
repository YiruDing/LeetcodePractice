class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    # leftBias=[True/False], if False,res is rightBiased
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                # i = m要放在這裡！
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i


# 待修
class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                res.append(m)
                continue
            elif nums[m] < target:
                l += 1
            else:
                r -= 1

        if len(res) > 2:
            return [res[0], res[-1]]
        else:
            return [-1, -1]
