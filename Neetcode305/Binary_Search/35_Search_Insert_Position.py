# My solution O(n)須改善，題目說必須要O(log n)
class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] == target or (nums[i] > target
                                     and nums[i - 1] < target):
                return i


# 也可以這樣寫
# for i in range(len(nums) - 1):
#             if nums[i] == target :
#                 return i
#             elif (nums[i] < target and nums[i + 1] > target):
#                 return i + 1


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l

    # 不管是大於最大值，或小於最小值，l都會變得大於r，所以return l...例子見neetcode影片

    # Neetcode另外一個有點讓人困惑的解
    class Solution:

        def searchInsert(self, nums: List[int], target: int) -> int:
            l, r = 0, len(nums)

            while l < r:
                # 3/2 不能是l <= r 喔，因為可能即使l = r 也永遠找不到該值
                mid = l + (r - l) // 2
                if target <= nums[mid]:
                    # 3/2 target < nums[mid] 會超時，因為沒法改變l或r的值
                    r = mid
                    # 3/2  為什麼 r 不能是 mid -1?
                elif target > nums[mid]:
                    l = mid + 1
                # 3/2 為什麼以下兩行可有可無呢？
                # else:
                # return mid
            return l
