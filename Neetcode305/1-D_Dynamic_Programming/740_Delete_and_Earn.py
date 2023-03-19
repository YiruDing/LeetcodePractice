class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)Combination
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0
        for i, n in enumerate(nums):
            curEarn = n * count[n]
            if i > 0 and nums[i] == nums[i - 1] + 1:
                tmp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = tmp
            else:
                tmp = earn2
                earn2 = earn2 + curEarn
                earn1 = tmp
        return earn2