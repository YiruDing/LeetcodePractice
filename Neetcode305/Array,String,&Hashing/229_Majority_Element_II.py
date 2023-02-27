# 2/23 自己解的：Ｄ
class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:
        ct = collections.Counter(nums)
        res = []

        for n in ct:
            if ct[n] > len(nums) // 3:
                res.append(n)
        return res