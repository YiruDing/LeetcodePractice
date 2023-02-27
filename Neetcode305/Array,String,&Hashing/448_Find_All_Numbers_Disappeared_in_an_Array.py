# 感謝讚美主！我第一次做就解出來了


class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numSet = set(nums)
        res = []

        for i in range(1, len(nums) + 1):

            if i not in numSet:
                res.append(i)

        return res