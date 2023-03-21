# 1
class Solution:

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return sorted(nums, key=lambda x: x - pivot and (1, -1)[x < pivot])
# JM: x < pivot可為真(1)或假(0),故可以從（1, -1）中取出不同的值


# 2
class Solution:

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivotFreq, ans = 0, []

        for num in nums:
            if num < pivot:
                ans.append(num)
            elif num == pivot:
                pivotFreq += 1

        ans.extend([pivot] * pivotFreq)

        for num in nums:
            if num > pivot:
                ans.append(num)

        return ans
