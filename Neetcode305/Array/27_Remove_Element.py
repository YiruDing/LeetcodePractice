# 1
def removeElement(self, nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i


# 2
class Solution:

    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1
        return start


# 3
class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

        i, k = 0, 0

        while k < len(nums):
            if nums[k] != val:
                nums[i] = nums[k]
                i += 1
            k += 1

        return i


# 4
class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)