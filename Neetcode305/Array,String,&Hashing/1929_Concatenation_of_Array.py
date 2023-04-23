# 4/23 廢到笑...休息一週後，以此暖身，自信都回來了呢！
# 就不用手抄啦
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n * 2):
            res.append(nums[i % n])
        return res