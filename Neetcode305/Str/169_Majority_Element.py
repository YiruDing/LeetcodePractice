class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        nonDupl = list(set(nums))
        for i in nonDupl:
            if nums.count(i) > len(nums) / 2:
                return i