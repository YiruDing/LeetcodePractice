# n XOR 0 is going to be n
# duplicate always cancel out
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for n in nums:
            res=n^res
        return res
# [4,1,2,1,2]
# res: 4
# res: 5
# res: 7
# res: 6
# res: 4
# 不一樣就加進來，一樣就減出去

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
    # reduce(fun,seq) 